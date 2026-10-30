#!/usr/bin/env python3
"""Build the 4K addon pack (content/addons/4k) from the HD pack (mm-hd).

Every image is upscaled exactly 2x (nearest neighbour: each pixel becomes a
2x2 block), so the pack looks identical to HD and can be improved image by
image later. Everything else is converted to match:

  *.png          2x; colour type, bit depth, palette, transparency and all
                 other chunks are kept exactly (only IHDR size and IDAT change)
  *.ani          hotspot offsets (fields 4 and 5) doubled
  kerndat.fnt    header pixel values (leading, char space, kern amount,
                 vertical align) doubled; kerning classes left alone
  *.rmp, *.txt   'addons/mm-hd/' paths changed to 'addons/4k/'
  mm-hd.rmp      renamed to 4k.rmp; uqmpack.nfo renamed to the new pack
  anything else  copied as is

Needs Pillow and pypng.  Builds these packs (each from content/addons/<hd> to content/addons/<4k>):
  mm-hd -> 4k, 3do-mode-hd -> 3do-mode-4k, dos-mode-hd -> dos-mode-4k

Usage:
  python -I tools/make-4k-pack.py [--force]
"""

import argparse
import io
import multiprocessing
import os
import shutil
import struct
import sys
import time
import zlib

from PIL import Image
import png

PACKS = [('mm-hd', '4k'), ('3do-mode-hd', '3do-mode-4k'),
		('dos-mode-hd', 'dos-mode-4k')]
PNG_SIG = b'\x89PNG\r\n\x1a\n'

# (colour type, bit depth) -> Pillow mode, for the formats Pillow can
# encode at the same depth. Everything else uses the built-in encoder.
PIL_MODES = {(0, 1): '1', (0, 8): 'L', (2, 8): 'RGB', (3, 8): 'P',
		(4, 8): 'LA', (6, 8): 'RGBA'}
PLANES = {0: 1, 2: 3, 3: 1, 4: 2, 6: 4}


# --- PNG chunk helpers ---

def read_chunks (data):
	if data[:8] != PNG_SIG:
		raise ValueError ('not a PNG file')
	chunks, i = [], 8
	while i < len(data):
		n, ctype = struct.unpack ('>I4s', data[i:i + 8])
		chunks.append ((ctype, data[i + 8:i + 8 + n]))
		i += 12 + n
	return chunks

def make_chunk (ctype, body):
	return (struct.pack ('>I', len(body)) + ctype + body +
			struct.pack ('>I', zlib.crc32 (ctype + body) & 0xffffffff))

def ihdr_info (chunks):
	w, h, depth, ctype, comp, filt, interlace = struct.unpack (
			'>IIBBBBB', chunks[0][1])
	return w, h, depth, ctype, interlace

def idat (chunks):
	return b''.join (body for t, body in chunks if t == b'IDAT')

def rebuild (src_chunks, new_idat):
	"""Same chunks in the same order; doubled IHDR size, new IDAT."""
	out, idat_done = [PNG_SIG], False
	for ctype, body in src_chunks:
		if ctype == b'IHDR':
			w, h = struct.unpack ('>II', body[:8])
			body = struct.pack ('>II', 2 * w, 2 * h) + body[8:]
		elif ctype == b'IDAT':
			if idat_done:
				continue
			body, idat_done = new_idat, True
		out.append (make_chunk (ctype, body))
	return b''.join (out)


# --- Pixel doubling ---

def double_rows_samples (rows, planes):
	"""rows of samples (pypng) -> doubled rows of samples."""
	out = []
	for row in rows:
		row = list (row)
		wide = []
		for x in range (0, len(row), planes):
			px = row[x:x + planes]
			wide += px + px
		out.append (wide)
		out.append (wide)
	return out

def pack_rows (rows, depth):
	"""Sample rows -> raw PNG scanlines (filter 0)."""
	raw = bytearray ()
	for row in rows:
		raw.append (0)
		if depth == 16:
			raw += struct.pack ('>%dH' % len(row), *row)
		elif depth == 8:
			raw += bytes (row)
		else:
			per = 8 // depth
			for i in range (0, len(row), per):
				b = 0
				for j, s in enumerate (row[i:i + per]):
					b |= s << (8 - depth * (j + 1))
				raw.append (b)
	return zlib.compress (bytes (raw), 9)

def encode_with_pillow (img, mode, depth, ctype):
	"""IDAT for a doubled Pillow image, if Pillow keeps the same format."""
	big = img.resize ((2 * img.width, 2 * img.height), Image.NEAREST)
	if mode == 'P':
		big.putpalette (bytes (range (256)) * 3)  # IDAT only holds indices
	buf = io.BytesIO ()
	big.save (buf, 'PNG', compress_level=9)
	chunks = read_chunks (buf.getvalue ())
	_, _, pdepth, pctype, _ = ihdr_info (chunks)
	if (pdepth, pctype) != (depth, ctype):
		return None
	return idat (chunks)


# --- Per-file conversion ---

def convert_png (src, dst):
	data = open (src, 'rb').read ()
	chunks = read_chunks (data)
	w, h, depth, ctype, interlace = ihdr_info (chunks)
	if interlace:
		raise ValueError ('interlaced PNGs are not supported')

	new_idat, img = None, None
	mode = PIL_MODES.get ((ctype, depth))
	if mode:
		img = Image.open (io.BytesIO (data))
		img.load ()
		if img.mode == mode:
			new_idat = encode_with_pillow (img, mode, depth, ctype)
		else:
			img = None
	if new_idat is None:
		img = None
		_, _, rows, _ = png.Reader (bytes=data).read ()
		new_idat = pack_rows (double_rows_samples (rows, PLANES[ctype]), depth)

	out = rebuild (chunks, new_idat)
	open (dst, 'wb').write (out)
	verify_png (data, out, img)
	return len(out)

def verify_png (src_data, out_data, src_img):
	"""The output must be the source, pixel-doubled, in the same format.

	src_img is the decoded source when Pillow handled it (fast C compare);
	otherwise both files are decoded with pypng."""
	sc, oc = read_chunks (src_data), read_chunks (out_data)
	sw, sh, sd, st, _ = ihdr_info (sc)
	ow, oh, od, ot, _ = ihdr_info (oc)
	if (ow, oh, od, ot) != (2 * sw, 2 * sh, sd, st):
		raise ValueError ('header mismatch')
	strip = lambda cs: [(t, b) for t, b in cs if t not in (b'IHDR', b'IDAT')]
	if strip (sc) != strip (oc):
		raise ValueError ('ancillary chunks changed')
	if src_img is not None:
		out_img = Image.open (io.BytesIO (out_data))
		out_img.load ()
		big = src_img.resize ((ow, oh), Image.NEAREST)
		if out_img.mode != src_img.mode or out_img.tobytes () != big.tobytes ():
			raise ValueError ('pixel mismatch')
		return
	_, _, srows, _ = png.Reader (bytes=src_data).read ()
	_, _, orows, _ = png.Reader (bytes=out_data).read ()
	expected = double_rows_samples (srows, PLANES[st])
	for e, o in zip (expected, orows):
		if list (o) != e:
			raise ValueError ('pixel mismatch')

def convert_ani (src, dst):
	out = []
	for line in open (src, 'rb').read ().splitlines (keepends=True):
		body = line.rstrip (b'\r\n')
		end = line[len(body):]
		f = body.split ()
		if len(f) == 5:
			f[3] = str (2 * int (f[3])).encode ()
			f[4] = str (2 * int (f[4])).encode ()
			body = b' '.join (f)
		out.append (body + end)
	open (dst, 'wb').write (b''.join (out))

def convert_fnt (src, dst, clamped):
	lines = open (src, 'rb').read ().splitlines (keepends=True)
	if lines:
		body = lines[0].rstrip (b'\r\n')
		end = lines[0][len(body):]
		f = body.split ()
		if len(f) == 5:
			# Leading, CharSpace, KernAmount: %hhu (0..255); VertAlign: %hhd
			limits = [(0, 255), (0, 255), (0, 255), (-128, 127)]
			for i, (lo, hi) in enumerate (limits, start=1):
				v = 2 * int (f[i])
				if not lo <= v <= hi:
					clamped.append ('%s: field %d %d -> %d' % (
							os.path.basename (os.path.dirname (src)), i, v,
							max (lo, min (hi, v))))
					v = max (lo, min (hi, v))
				f[i] = str (v).encode ()
			lines[0] = b' '.join (f) + end
	open (dst, 'wb').write (b''.join (lines))

def convert_text (src, dst, old_path, new_path):
	open (dst, 'wb').write (open (src, 'rb').read ().replace (old_path, new_path))

def convert_nfo (src, dst, is_main_pack):
	out = []
	for line in open (src, 'rb').read ().splitlines (keepends=True):
		key = line.split (b'=', 1)[0]
		body = line.rstrip (b'\r\n')
		end = line[len(body):]
		if key == b'name':
			line = (b'name=4K Content' if is_main_pack
					else body + b' (4K)') + end
		elif key == b'description':
			line = (b'description=2x upscale of the HD pack; '
					b'base for 4K art.' + end)
		out.append (line)
	open (dst, 'wb').write (b''.join (out))

def png_job (args):
	src, dst = args
	try:
		return src, convert_png (src, dst), None
	except Exception as e:
		return src, 0, '%s: %s' % (type (e).__name__, e)


def build_pack (addons_dir, src_name, dst_name, force):
	src_dir = os.path.join (addons_dir, src_name)
	dst_dir = os.path.join (addons_dir, dst_name)
	if not os.path.isdir (src_dir):
		print ('skipping %s: not found' % src_dir)
		return 0
	if os.path.exists (dst_dir):
		if not force:
			sys.exit ('%s exists; use --force to rebuild it' % dst_dir)
		shutil.rmtree (dst_dir)

	old_path = ('addons/%s/' % src_name).encode ()
	new_path = ('addons/%s/' % dst_name).encode ()
	start = time.time ()
	counts, clamped, pngs = {}, [], []
	for root, _, files in os.walk (src_dir):
		rel = os.path.relpath (root, src_dir)
		os.makedirs (os.path.join (dst_dir, rel), exist_ok=True)
		for name in files:
			src = os.path.join (root, name)
			ext = os.path.splitext (name)[1].lower ()
			if name == src_name + '.rmp':
				name = dst_name + '.rmp'
			dst = os.path.join (dst_dir, rel, name)
			counts[ext] = counts.get (ext, 0) + 1
			if ext == '.png':
				pngs.append ((src, dst))
			elif ext == '.ani':
				convert_ani (src, dst)
			elif name == 'kerndat.fnt':
				convert_fnt (src, dst, clamped)
			elif ext in ('.rmp', '.txt'):
				convert_text (src, dst, old_path, new_path)
			elif name == 'uqmpack.nfo':
				convert_nfo (src, dst, src_name == 'mm-hd')
			else:
				shutil.copy2 (src, dst)

	failures, out_bytes = [], 0
	with multiprocessing.Pool () as pool:
		for i, (src, size, err) in enumerate (
				pool.imap_unordered (png_job, pngs, chunksize=16), 1):
			out_bytes += size
			if err:
				failures.append ('%s: %s' % (os.path.relpath (src, src_dir), err))
			if i % 2000 == 0 or i == len(pngs):
				print ('  %s: %d/%d images' % (dst_name, i, len(pngs)), flush=True)

	total = sum (os.path.getsize (os.path.join (r, f))
			for r, _, fs in os.walk (dst_dir) for f in fs)
	print ('%s -> %s: %s' % (src_name, dst_name,
			', '.join ('%s %d' % kv for kv in sorted (counts.items ()))))
	print ('  %.0f MB (images %.0f MB) in %.0f s' % (
			total / 1e6, out_bytes / 1e6, time.time () - start))
	for c in clamped:
		print ('  Clamped (engine needs wider font fields):', c)
	for f in failures:
		print ('  FAILED', f)
	return len (failures)


def main ():
	repo = os.path.dirname (os.path.dirname (os.path.abspath (__file__)))
	ap = argparse.ArgumentParser (description=__doc__.split ('\n')[0])
	ap.add_argument ('--addons', default=os.path.join (repo, 'content', 'addons'),
			help='the content/addons directory')
	ap.add_argument ('--force', action='store_true',
			help='delete existing destination packs first')
	a = ap.parse_args ()

	failed = 0
	for src_name, dst_name in PACKS:
		failed += build_pack (a.addons, src_name, dst_name, a.force)
	return 1 if failed else 0


if __name__ == '__main__':
	sys.exit (main ())
