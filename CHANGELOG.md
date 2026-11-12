# Historie verzí – Vyhledávač IOL v DOCTISu

Verze se číslují `HLAVNÍ.VEDLEJŠÍ.OPRAVA`:
- **HLAVNÍ** – zásadní změna ovládání nebo formátu kódů,
- **VEDLEJŠÍ** – nová funkce nebo viditelná úprava,
- **OPRAVA** – oprava chyby bez jiných změn.

Každá verze má v gitu značku (tag) `vX.Y.Z`. Aktuální číslo verze je vidět v patičce aplikace.

## 2.1.1 – 12. 11. 2026
- Aktualizován katalog čoček podle nové tabulky IOLs.xlsx (sjednocené názvy, opravené hodnoty u 4 čoček AT TORBI a 3 čoček AT LISA TRI toric, nově AT LISA TRI 839MP DPT 22.0 – 003500-0006-051).
- AT TORBI 719MP zůstávají vyloučené.

## 2.1.0 – 12. 11. 2026
- Katalogové číslo se už nekopíruje automaticky – jen kliknutím na tlačítko **Kopírovat**; pod ním se zeleně ukáže „Byl zkopírován kód: …“.
- Z vyhledávání vyloučeny čočky **AT TORBI 719MP** (`EXCLUDE_MODELS` v `tools/build_data.py`).

## 2.0.0 – 12. 11. 2026
- **Místo vyhledávacího kódu aplikace najde čočku v katalogu** (tabulka IOLs.xlsx, listy LuxSmart, AT TORBI, AT LISA – 4 889 položek) a nabídne ke zkopírování **katalogové číslo** (sloupec J) s přesným názvem čočky (sloupec E).
- Má-li čočka v katalogu víc provedení (např. AT TORBI 719M a 719MP), zobrazí se všechna, každé s vlastním tlačítkem Kopírovat. Jediné provedení se zkopíruje samo.
- Dlaždice dioptrií, které v katalogu pro zvolený typ nejsou, jsou zašedlé. Cylindry se nabízejí podle katalogu (u LuxSmart toric 0,75 / 1,0 / 1,5 / 2,25 / 3,0 …).
- Aktualizace katalogu: `python3 tools/build_data.py IOLs.xlsx`.

## 1.2.3 – 12. 11. 2026
- AT LISA TRI: desetinná tečka místo čárky – `*AT LISA TRI 839MP DPT 18.0`.

## 1.2.2 – 11. 11. 2026
- Odstraněna legenda kódů pod aplikací.
- Nasazovací skript stahuje vždy přesně poslední verzi (bez zpoždění cache GitHubu).

## 1.2.1 – 11. 11. 2026
- Název aplikace v záhlaví je fialový (barva aplikace) a tučnější.

## 1.2.0 – 11. 11. 2026
- Název aplikace v záhlaví i v záložce prohlížeče: **Vyhledávač IOL v DOCTISu**.
- V patičce se zobrazuje číslo verze a datum vydání.
- Zavedeno verzování (tento soubor, git tagy).

## 1.1.0 – 11. 11. 2026
- AT LISA TRI: desetinná čárka místo tečky – `*AT LISA TRI 839MP DPT 27,5`.
- AT LISA TRI toric: znaménko před sférou, tečky – `*AT LISA TRI TORIC 949M SE+19.00 CYL03.0`.

## 1.0.0 – 10. 11. 2026
- První vydání na Firebase Hosting (https://vyhledavac-iol-doctis.web.app).
- Výběr typu IOL dlaždicemi, sféra (celé dioptrie + desetiny), cylindr u torických čoček.
- Automatické kopírování kódu, věta se souhrnem výběru, vzhled Levandule.
