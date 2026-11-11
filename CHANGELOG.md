# Historie verzí – Vyhledávač IOL v DOCTISu

Verze se číslují `HLAVNÍ.VEDLEJŠÍ.OPRAVA`:
- **HLAVNÍ** – zásadní změna ovládání nebo formátu kódů,
- **VEDLEJŠÍ** – nová funkce nebo viditelná úprava,
- **OPRAVA** – oprava chyby bez jiných změn.

Každá verze má v gitu značku (tag) `vX.Y.Z`. Aktuální číslo verze je vidět v patičce aplikace.

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
