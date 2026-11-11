# Vyhledávač IOL v DOCTISu

Generátor vyhledávacího kódu nitrooční čočky (AT TORBI, AT LISA TRI, AT LISA TRI toric, LuxSmart EDOF, LuxSmart EDOF toric).

- Web: https://vyhledavac-iol-doctis.web.app
- Aplikace: `public/index.html` (statická stránka, nic neukládá ani neodesílá)
- Historie verzí: [CHANGELOG.md](CHANGELOG.md)

## Nasazení (Windows PowerShell, na PC s přihlášeným Firebase CLI)

```powershell
irm "https://raw.githubusercontent.com/OFTALMED/WebApp/vyhledavac-iol-doctis/deploy.ps1" | iex
```

Skript stáhne aktuální soubory z této větve do `%USERPROFILE%\vyhledavac-iol-doctis` a spustí `firebase deploy --only hosting`.
