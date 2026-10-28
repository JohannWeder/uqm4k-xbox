# Packages the UWP build of UQM.
#
# Run after building build\uwp\UrQuanMastersUWP.vcxproj.  Produces, under
# build\uwp\out\<Platform>\<Configuration>\:
#   layout\                 the unpacked app (exe, SDL2.dll, assets, content)
#   UQM-MegaMod.msix        the signed package, for Xbox Device Portal
#   UQM-MegaMod-dev.cer     the signing certificate (public part)
#
# -Register  registers layout\ on this PC (needs Windows Developer Mode),
#            so it can be launched from the Start menu without signing.
# -NoSign    skips creating/signing the .msix (layout only).

param(
	[string]$Configuration = 'Release',
	[string]$Platform = 'x64',
	[switch]$Register,
	[switch]$NoSign
)

$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
$repo = Resolve-Path (Join-Path $here '..\..')
$out = Join-Path $here "out\$Platform\$Configuration"
$app = Join-Path $out 'app'
$layout = Join-Path $out 'layout'
$sdkBin = 'C:\Program Files (x86)\Windows Kits\10\bin\10.0.26100.0\x64'
$publisher = 'CN=Johann'     # must match Identity/@Publisher in Package.appxmanifest
$pfxPassword = 'uqm-dev'     # local self-signed dev certificate only

if (-not (Test-Path "$app\UrQuanMasters.exe"))
{ throw "Build UrQuanMastersUWP.vcxproj ($Configuration|$Platform) first." }

# --- Assemble the layout ---
Write-Host "Assembling layout in $layout"
New-Item -ItemType Directory -Force $layout | Out-Null
foreach ($f in 'UrQuanMasters.exe', 'AppxManifest.xml', 'resources.pri')
{ Copy-Item "$app\$f" $layout -Force }
$sdlDll = Get-ChildItem "$out\sdl" -Recurse -Filter SDL2.dll | Select-Object -First 1
if (-not $sdlDll) { throw "SDL2.dll not found under $out\sdl" }
Copy-Item $sdlDll.FullName $layout -Force
New-Item -ItemType Directory -Force "$layout\Assets" | Out-Null
Copy-Item "$here\Assets\*.png" "$layout\Assets" -Force
Copy-Item "$repo\LICENSE" "$layout\COPYING.txt" -Force

# Content is large (~28k files); robocopy only copies what changed.
robocopy "$repo\content" "$layout\content" /MIR /XF .gitignore README.md /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "robocopy failed copying content ($LASTEXITCODE)" }

if ($Register)
{
	Write-Host 'Registering layout on this PC'
	Add-AppxPackage -Register "$layout\AppxManifest.xml" -ForceApplicationShutdown
}

if ($NoSign) { return }

# --- Signing certificate (self-signed, reused between runs) ---
$cert = Get-ChildItem Cert:\CurrentUser\My |
		Where-Object { $_.Subject -eq $publisher -and $_.FriendlyName -eq 'UQM UWP dev signing' -and $_.NotAfter -gt (Get-Date) } |
		Select-Object -First 1
if (-not $cert)
{
	Write-Host "Creating self-signed certificate $publisher"
	$cert = New-SelfSignedCertificate -Type Custom -Subject $publisher `
			-FriendlyName 'UQM UWP dev signing' -KeyUsage DigitalSignature `
			-CertStoreLocation Cert:\CurrentUser\My `
			-TextExtension @('2.5.29.37={text}1.3.6.1.5.5.7.3.3', '2.5.29.19={text}')
}
$pfx = Join-Path $out 'UQM-MegaMod-dev.pfx'
$cer = Join-Path $out 'UQM-MegaMod-dev.cer'
Export-PfxCertificate -Cert $cert -FilePath $pfx -Password (ConvertTo-SecureString $pfxPassword -AsPlainText -Force) | Out-Null
Export-Certificate -Cert $cert -FilePath $cer | Out-Null

# --- Pack and sign ---
$msix = Join-Path $out 'UQM-MegaMod.msix'
Write-Host "Packing $msix"
& "$sdkBin\makeappx.exe" pack /d $layout /p $msix /o /h SHA256 | Out-Null
if ($LASTEXITCODE -ne 0) { throw "makeappx failed ($LASTEXITCODE)" }
& "$sdkBin\signtool.exe" sign /q /fd SHA256 /f $pfx /p $pfxPassword $msix
if ($LASTEXITCODE -ne 0) { throw "signtool failed ($LASTEXITCODE)" }

Write-Host ("Done: {0} ({1:N0} MB)" -f $msix, ((Get-Item $msix).Length / 1MB))
