# Trailer Cam
Das Live Video Streaming-Projekt ermöglicht die Übertragung eines Videos von einem Raspberry Pi mit einer Raspberry Pi-Kamera in Echtzeit auf ein Zugfahrzeug, das ein iPhone als Monitor verwendet. Die Software basiert auf Flask und bietet eine einfache Benutzeroberfläche zur Anzeige des Live-Video-Streams. Das Projekt ermöglicht es Benutzern, das Video in den Vollbildmodus zu schalten und anpassbare Einstellungen wie Kameraauflösung und -konfiguration vorzunehmen.

### Installation dependencies
um das Projekt zu installieren müssen folgende Dependencies installiert werden:

Pip3: sudo apt install python3-pip

Flask: pip install flask
picamera: pip install picamera

### Files
1. Klonen Sie das Repository:
git clone 


### Install as Deamon
Um den Befehl `python app.py` als Daemon auf dem Raspberry Pi hinzuzufügen, können Sie eine Systemd-Serviceeinheit erstellen. Hier ist eine Schritt-für-Schritt-Anleitung:

1. Erstellen Sie eine Serviceeinheitsdatei für den Daemon mit dem Befehl `sudo nano /etc/systemd/system/app.service`.

2. Geben Sie den folgenden Inhalt in die Serviceeinheitsdatei ein:
```plaintext
[Unit]
Description=PeerAudio App
After=network.target

[Service]
ExecStart=/usr/bin/python /Pfad/zur/app.py
WorkingDirectory=/Pfad/zum/Verzeichnis
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=peeraudio
User=pi
Group=pi
Restart=always

[Install]
WantedBy=multi-user.target
```
- Ersetzen Sie `/Pfad/zur/app.py` durch den tatsächlichen Pfad zur `app.py`-Datei.
- Ersetzen Sie `/Pfad/zum/Verzeichnis` durch den tatsächlichen Pfad zum Verzeichnis, in dem sich die `app.py`-Datei befindet.
- Passen Sie den `User` und `Group` an, je nachdem, unter welchem Benutzer der Daemon ausgeführt werden soll.

3. Speichern und schließen Sie die Datei (`Ctrl + X`, dann `Y` und `Enter`).

4. Aktivieren Sie den Service mit dem Befehl `sudo systemctl enable app.service`.

5. Starten Sie den Service mit dem Befehl `sudo systemctl start app.service`.

Jetzt wird der Python-Code aus der `app.py`-Datei als Daemon gestartet und automatisch beim Systemstart ausgeführt. Der Standardausgabe- und Standardfehler-Output wird in das Syslog protokolliert.

Sie können den Status des Dienstes überprüfen mit `sudo systemctl status app.service`, und Sie können den Dienst mit `sudo systemctl stop app.service` stoppen.

Bitte stellen Sie sicher, dass Sie die Pfade und Konfigurationen entsprechend Ihrer spezifischen Umgebung anpassen.
