# Vyhledávač IOL v DOCTISu

Vyhledání katalogového čísla nitrooční čočky (AT TORBI, AT LISA TRI, AT LISA TRI toric, LuxSmart, LuxSmart toric) podle typu, sféry a cylindru.

- Web: https://vyhledavac-iol-doctis.web.app
- Aplikace: `public/index.html` (statická stránka, nic neukládá ani neodesílá)
- Historie verzí: [CHANGELOG.md](CHANGELOG.md)

## Nasazení (Windows PowerShell, na PC s přihlášeným Firebase CLI)

```powershell
irm "https://raw.githubusercontent.com/OFTALMED/WebApp/vyhledavac-iol-doctis/deploy.ps1" | iex
```

Skript stáhne aktuální soubory z této větve do `%USERPROFILE%\vyhledavac-iol-doctis` a spustí `firebase deploy --only hosting`.

## Aktualizace katalogu čoček

Data jsou vložená přímo v `public/index.html`. Po změně tabulky IOLs.xlsx (listy LuxSmart, AT TORBI, AT LISA; sloupce E = název, F = doplněk, J = katalogové číslo):

```bash
python3 tools/build_data.py cesta/k/IOLs.xlsx
```

Skript vypíše počty čoček podle typu a řádky, které nerozpoznal.
