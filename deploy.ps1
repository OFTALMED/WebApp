# Nasazeni aplikace Vyhledavac IOL v DOCTISu na Firebase Hosting.
# Spousteni: irm "https://raw.githubusercontent.com/OFTALMED/WebApp/vyhledavac-iol-doctis/deploy.ps1" | iex
$ErrorActionPreference = "Stop"
$repo = "OFTALMED/WebApp"; $branch = "vyhledavac-iol-doctis"
# Presny posledni commit vetve (obchazi zpozdeni cache raw.githubusercontent.com)
$sha = (Invoke-RestMethod -UseBasicParsing -Uri "https://api.github.com/repos/$repo/commits/$branch" -Headers @{ "User-Agent" = "deploy-iol" }).sha
$base = "https://raw.githubusercontent.com/$repo/$sha"
$d = Join-Path $env:USERPROFILE "vyhledavac-iol-doctis"
New-Item -ItemType Directory -Force (Join-Path $d "public") | Out-Null
foreach ($f in @("public/index.html", "firebase.json", ".firebaserc")) {
  Invoke-WebRequest -UseBasicParsing -Uri "$base/$f" -OutFile (Join-Path $d $f)
}
$ver = ([regex]::Match((Get-Content (Join-Path $d "public/index.html") -Raw), 'name="app-version" content="([^"]+)"')).Groups[1].Value
Set-Location $d
Write-Host "Stazena verze $ver (commit $($sha.Substring(0,7))), nasazuji na Firebase..." -ForegroundColor Cyan
firebase deploy --only hosting
Write-Host "Hotovo: verze $ver je na https://vyhledavac-iol-doctis.web.app (obnovte Ctrl+F5)" -ForegroundColor Green
