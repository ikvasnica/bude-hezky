# Bude Hezky?
Chceš vědět, zda zítra můžeš během dne na kolo a jsi líný/á zapnout aplikaci Počasí? 

Tento nástroj v příkazové řádce je určen přímo pro Tebe. Nejen, že zobrazí, jestli bude zítra hezky, ale ještě Tě na to upozorní i e-mailem a/nebo zprávou na Telegramu!

Speciálně věnováno pro [Honza Javorek](https://github.com/honzajavorek).

## Použití
Pokud chceš dostávat pravidelné informace o hezkém počasí v Praze, [přidej se do skupiny na Telegramu](https://t.me/budeVPrazeHezky)! Informaci odesílá bot každý den v 19:00 a to pouze v případě, že bude následující den hezky.

## Vývoj
### Prerekvizity:
+ Python (alespoň verze `3.8.0`)
+ pipenv

V terminálu prostě spustíš: `pipenv install`

### Jak spustit aplikaci
1. Zaregistruj se na [OpenWeatherMap](https://openweathermap.org) a vygeneruj si API klíč.
2. *(optional, pouze pokud chceš posílat e-maily)* Zaregistruj se na [Sendgrid](https://sendgrid.com) a vygeneruj si API klíč.
3. *(optional, pouze pokud chceš posílat Telegram zprávy)* Vytvoř Telegram bota - [návod](https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e), [API dokumentace](https://core.telegram.org/bots/api)
4. Přejmenuj soubor `.env.example` na `.env` a vlož vygenerované klíče.
5. Opět otevři terminál a zkopíruj tam tohle (příklad pro Prahu). Kód země je důležitý, pokud existuje více měst se shodným názvem.

    `pipenv run python -m bude_hezky.main Prague,CZ`

### Seznam volitelných argumentů
+ `--email`: E-mailová adresa, na kterou se odešle informace o hezkém počasí
+ `--chat`: Telegram chat ID, na kterou se odešle informace o hezkém počasí. [API dokumentace ke zjištění Telegram Chat ID](https://core.telegram.org/bots/api#getupdates)
