# Simple User Auth System (mit JSON & Pepper)

Ein einfaches Benutzer-Registrierungs- und Login-System in Python.  
Speichert Benutzer in einer `db.json` und verwendet Salt + Pepper zum sicheren Hashing.

## 🔧 Dateien

- `auth.py` – Logik für Registrierung & Login
- `main.py` – Benutzeroberfläche (CLI)
- `database.json` – Speicherung der Benutzer
- `pepper.txt` – Geheimer Schlüssel (Pepper) für Passwort-Hashing

## ▶️ Verwendung

1. `pepper.txt` erstellen mit einem geheimen String:
   ```
   superGeheimerPepper123!
   ```

2. `database.json` vorbereiten:
   ```json
   { "users": [] }
   ```

3. Programm starten:
   ```bash
   python main.py
   ```

## 🔒 Sicherheit

- Passwort-Hash = SHA256(Passwort + Salt + Pepper)
- Salt ist pro Nutzer unterschiedlich
- Pepper ist geheim und **nicht** in der Datenbank enthalten

## 📚 Lernziel

Dieses Projekt dient als Lernhilfe für:
- Passwort-Hashing mit Salt & Pepper
- JSON-Dateiverarbeitung
- Codeaufteilung & Struktur
