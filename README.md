# Bude Hezky?
Chceš vědět, zda zítra můžeš během dne na kolo a jsi líný/á zapnout aplikaci Počasí? Tento nástroj v příkazové řádce je určen přímo pro Tebe - nejenom, že zobrazí, jestli bude zítra hezky, ale ještě Tě na to upozorní i e-mailem!

Speciálně věnováno pro [Honza Javorek](https://github.com/honzajavorek).


## Instalace
**Prerekvizity:**
+ Python (alespoň verze 3.8.0)
+ pipenv

V terminálu prostě spustíš: `pipenv install`

A je to.

## Použití
Nemůže to být jednodušší! Opět otevři terminál a zkopíruj tam tohle (příklad pro Prahu). Kód země je důležitý, pokud existuje více měst se shodným názvem.

`pipenv run python -m bude_hezky.main Prague,CZ`

### Seznam volitelných argumentů
+ *--email*: E-mailová adresa, na kterou se odešle informace o počasí