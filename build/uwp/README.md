# UWP / Xbox build

Builds UQM MegaMod as a UWP app, so it can run on a PC or on an Xbox in
Developer Mode.

## Prerequisites

- Visual Studio 2022 (or Build Tools) with the **Universal Windows Platform
  build tools** workload (`Microsoft.VisualStudio.Workload.UniversalBuildTools`)
  and toolset v143.
- Windows SDK 10.0.26100.0.
- The library sources, unpacked under `dev-lib\uwp-src\` (ignored by git):

  | Folder | Source |
  |---|---|
  | `SDL2\SDL-release-2.32.10` | https://github.com/libsdl-org/SDL/archive/refs/tags/release-2.32.10.zip |
  | `zlib\zlib-1.3.1` | https://github.com/madler/zlib/archive/refs/tags/v1.3.1.zip |
  | `libpng\libpng-1.6.43` | https://github.com/pnggroup/libpng/archive/refs/tags/v1.6.43.zip |
  | `libogg\ogg-1.3.5` | https://github.com/xiph/ogg/archive/refs/tags/v1.3.5.zip |
  | `libvorbis\vorbis-1.3.7` | https://github.com/xiph/vorbis/archive/refs/tags/v1.3.7.zip |

OpenAL is not used. The UWP build uses the SDL mixer, which is the default
sound driver.

## Build

```powershell
# Only needed after adding/removing sources in build\msvs2019\UrQuanMasters.vcxproj
.\build\uwp\make-vcxproj.ps1

& "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\MSBuild\Current\Bin\amd64\MSBuild.exe" `
    build\uwp\UrQuanMastersUWP.vcxproj /p:Configuration=Release /p:Platform=x64 /m

.\build\uwp\package.ps1              # layout + signed UQM4K-Xbox.msix
.\build\uwp\package.ps1 -Register    # also register the layout on this PC
.\build\uwp\package.ps1 -Version 2026.1.1.0   # use a specific version
```

`package.ps1` stamps the package version with the packaging time,
`YYYY.MM.DD.HHMM` (for example `2026.10.29.1530`). Every package is newer
than the last, so it installs as an update. `Package.appxmanifest` keeps a
placeholder version; only the packaged copy is stamped.

The build also builds SDL (via `SDL-UWP.vcxproj`) and `deps\uqm-deps.vcxproj`
(zlib, libpng, ogg, vorbis as one static lib). Everything goes to
`build\uwp\out\` (ignored by git).

## Files

| File | Purpose |
|---|---|
| `UrQuanMastersUWP.vcxproj.in` | Project template. Edit this, not the generated `.vcxproj`. |
| `make-vcxproj.ps1` | Fills the template with the desktop project's source list. |
| `Package.appxmanifest` | App identity (`UQM4K.Xbox`), tiles and capabilities. `Publisher` must match the signing cert. Changing `Name` or `Publisher` makes it a different app, with separate saves. |
| `package.ps1` | Builds the layout and the signed `.msix`, and can register it on the PC. |
| `deps\` | Static-lib project for zlib/libpng/ogg/vorbis, plus `pnglibconf.h`. |
| `include\SDL2\` | Forwarding headers so ImGui's `<SDL2/...>` includes resolve. |
| `src\msgbox_uwp.c` | Replaces `msgbox_win.c`, since `MessageBox` isn't available in UWP. |

## Differences from the desktop build

- **Config folder:** config, saves and `uqm.log` live in the app's LocalState
  folder, not `%APPDATA%\UQM-MegaMod`. On a PC that's
  `%LOCALAPPDATA%\Packages\UQM4K.Xbox_<id>\LocalState`.
- **Content:** read from the package's install folder (`content\`).
- **Clipboard screenshots:** not available.

## Installing on Xbox (Developer Mode)

1. Put the console into Developer Mode (Xbox Dev Mode app plus a Partner
   Center developer account).
2. Open Device Portal: in Dev Home, note the address and browse to it from
   your PC.
3. **Add** an app, choose `UQM4K-Xbox.msix`, and add the dependency
   `C:\Program Files (x86)\Microsoft SDKs\Windows Kits\10\ExtensionSDKs\Microsoft.VCLibs\14.0\Appx\Retail\x64\Microsoft.VCLibs.x64.14.00.appx`.
4. In Dev Home, set the app's type to **Game** (under View details), so it
   gets game-level CPU, GPU and memory.

Builds made before the rename used the identity `UQM.MegaMod`. That's a
separate app: uninstall it by hand if it's still installed.
