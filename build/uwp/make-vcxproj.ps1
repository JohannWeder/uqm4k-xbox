# Generates UrQuanMastersUWP.vcxproj from the desktop project
# (build\msvs2019\UrQuanMasters.vcxproj), so both share one source list.
# Re-run this whenever source files are added to or removed from the
# desktop project.

$ErrorActionPreference = 'Stop'
$here = $PSScriptRoot
$desktop = Join-Path $here '..\msvs2019\UrQuanMasters.vcxproj'
$outFile = Join-Path $here 'UrQuanMastersUWP.vcxproj'

# Desktop-only sources that cannot be built for UWP; replacements live in
# build\uwp\src.
$excluded = @(
	'..\..\src\libs\log\msgbox_win.c'
)
# The UWP build uses the SDL mixer (the default sound driver), not OpenAL.
$excludedPattern = '\\libs\\sound\\openal\\'

$x = [xml](Get-Content $desktop)
$isExcludedForX64 = {
	param($item)
	foreach ($n in $item.ChildNodes)
	{
		if ($n.Name -eq 'ExcludedFromBuild' -and
				$n.Condition -match "Release\|x64" -and $n.InnerText -eq 'true')
		{ return $true }
	}
	return $false
}

$compile = $x.Project.ItemGroup.ClCompile |
		Where-Object { -not (& $isExcludedForX64 $_) } |
		ForEach-Object { $_.Include } |
		Where-Object { $excluded -notcontains $_ -and $_ -notmatch $excludedPattern } |
		Sort-Object -Unique
$headers = $x.Project.ItemGroup.ClInclude | ForEach-Object { $_.Include } |
		Where-Object { $_ -notmatch $excludedPattern } |
		Sort-Object -Unique

$sb = New-Object System.Text.StringBuilder
foreach ($f in $compile) { [void]$sb.AppendLine("    <ClCompile Include=`"$f`" />") }
$compileItems = $sb.ToString().TrimEnd()
$sb.Clear() | Out-Null
foreach ($f in $headers) { [void]$sb.AppendLine("    <ClInclude Include=`"$f`" />") }
$headerItems = $sb.ToString().TrimEnd()

$template = Get-Content (Join-Path $here 'UrQuanMastersUWP.vcxproj.in') -Raw
$result = $template.Replace('@CLCOMPILE_ITEMS@', $compileItems).Replace('@CLINCLUDE_ITEMS@', $headerItems)
[IO.File]::WriteAllText($outFile, $result, (New-Object System.Text.UTF8Encoding $true))
"Wrote $outFile ($($compile.Count) sources, $($headers.Count) headers)"
