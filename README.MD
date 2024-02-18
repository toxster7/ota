# Dokumentation zur Esp32Cam 
## Inhaltsverzeichnis 
1. Projektbeschreibung
1. Motivation 
1. Werkzeuge 
1. Vorbereitung
1. Over The Air Update 
1. Webserver 
1. Telegrambot 
1. Esp32Cam Foto
1. Probleme

## Projektbescreibung 

ESP32 mit einer Kamera, der sich selbst über WLAN aktualisiert und auf Anfrage Screenshot per Telegrammchat senden soll. Die Kameras können im MobileLab Bus installiert werden. Die Software ist skalierbar und erweitbar und kann auf andere Esp32-Kameras hochgeladen werden.

## Motivation
Das Ziel des Projekts war es, ein Instrument zu erstellen, das separat angewendet und erweitert werden kann und als einsatzfähiges Element für zukünftige Projekte dient. Dieses Projekt wurde auch ausgewählt, um Erfahrungen in der Anwendung von ESP32-Modulen und deren Programmierung mit MicroPython zu sammeln.

## Werkzeuge
Für dieses Projekt wurde benutzt:  
- Esp32 mit Kamera 
- USB-C Hub  
- USB-Kabel 
- Thonny IDE
## Vorbereitung
### 1. Download&Install Thonny IDE 
https://thonny.org/
### 2. Esp32 über USB/TTL mit Rechner verbinden
### 3. Firmware installieren 
- Laden Sie **micropython_v1.21.0_camera_no_ble.bin** Datei aus dem Repo herunter
- Öffnen Sie Thonny
- Tools->Options
- Interpreter->Install or Update Micropython(esptool)->...->Select local Micropython image->Install
- Wählen Sie unten rechts Micropython(ESP32) aus
 
## Over The Air Update
Als Beispiel wurde ugit, [ein Projekt](https://github.com/turfptax/ugit) von turfptax benutzt und umgeschrieben.
Nach jedem Neustart werden neue Commits aus dem Repository des Projekts auf ESP32 per WlAN hochgeladen.
#### Einstellung
Setzen sie In **ugit.py** folgende User Variables:

WLAN:
  `ssid = ""
   password = "" `

Gitlab Access Token:
    `token=""`

Dateien,die nicht bearbeitet/entfernt/hochgeladen werden müssen, in ignore_files mit '/' reinschreiben:

`ignore_files = ['/ugit.py','/updated.py','/boot.py']`

**Wichtig! '/ugit.py' nicht aus ignores_files entfernen!**

Gitlab APIs

repository tree:

`call_trees_url = f'https://gitlab.rz.htw-berlin.de/api/v4/projects/2797/repository/tree?path=Esp32-cam&ref=ProjStud_WS_23_24recursive=true'`

raw file path part1&part2:

`raw = f'https://gitlab.rz.htw-berlin.de/api/v4/projects/2797/repository/files/Esp32-cam'` 

`raw_2 = '/raw?ref=ProjStud_WS_23_24'`
## Webserver
Der Webserver wird automatisch gestartet, um den Stream von der ESP32-Kamera bereitzustellen.

Nach dem Start kopieren Sie die erste IP von ifconfig() im Terminal und  fügen die in den Browser hinzu.(In diesem Fall '192.168.4.1')  
![ifconfig](https://miro.medium.com/v2/resize:fit:1400/1*di7vfjdCWmUKGXxGMkmX3Q.png "a title")
## Telegrambot
Ein Telegrambot, der Anfragen ans Esp32Modul senden soll. Der Bot wurde durch [@BotFather](https://telegram.me/BotFather) erstellt.
Implementierung befindet sich in **utelegram.py** und **main.py**.
Starten Sie den [@MobileLabCamBot](https://t.me/MobileLabCamBot)  in Telegram.

`/ping` - Verbindung überprüfen.
 Der Bot soll mit `pong` antworten.

`/takePhoto` - die Kamera macht ein Foto und sendet an den Bot.

Wenn Sie einen anderen Bot verwenden möchten: in **config.py** utelegram_config{'token':'' } umstellen.

Um neue Befehle zu erstellen: in **main.py** `bot.register('/{your_command}',{your_respond_method})`

## Esp32Cam Foto
Die **sendImage.py**-Klasse nimmt ein Foto auf und sendet an den Telegrambot.
**Wichtig!** In der Methode `send_my_photo()` `chat_id=` mit ihrem Telegram-Id ergänzen.

## Probleme
Die Entwicklung und Implementierung der Esp32Cam-Software waren lehrreiche und herausfordernde Erfahrungen. Der Entwicklungsprozess brachte jedoch verschiedene Herausforderungen mit sich, insbesondere bei der Implementierung der APIs. Zum Beispiel ist das MicroPython-Paket urequest leider veraltet und wenig funktionsfähig. Es sollte im Vergleich zum request-Paket von Python erweitert werden. Darüber hinaus werden mehrere MicroPython-Bibliotheken nicht mehr gewartet und sind schlecht dokumentiert.Man könnte trozdem Lösungen für bestimmte Probleme von anderen Entwicklern finden und sie erfolgreich in die Software integrieren.

@Author Anton Kadushkin 575875 














  
