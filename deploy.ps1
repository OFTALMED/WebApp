# Nasazeni aplikace Vyhledavac IOL - DOCTIS na Firebase Hosting.
# Spousteni: irm "https://raw.githubusercontent.com/OFTALMED/WebApp/vyhledavac-iol-doctis/deploy.ps1" | iex
$ErrorActionPreference = "Stop"
$base = "https://raw.githubusercontent.com/OFTALMED/WebApp/vyhledavac-iol-doctis"
$d = Join-Path $env:USERPROFILE "vyhledavac-iol-doctis"
New-Item -ItemType Directory -Force (Join-Path $d "public") | Out-Null
$t = [DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
foreach ($f in @("public/index.html", "firebase.json", ".firebaserc")) {
  Invoke-WebRequest -UseBasicParsing -Uri "$base/$($f)?t=$t" -OutFile (Join-Path $d $f)
}
Set-Location $d
Write-Host "Stazena nejnovejsi verze, nasazuji na Firebase..." -ForegroundColor Cyan
firebase deploy --only hosting
