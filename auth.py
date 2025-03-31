import json, hashlib, os

# Pfad zur JSON-Datei (ersetzt Datenbank)
DB_FILE = 'db.json'

# "Pepper" wird aus einer sicheren Quelle geladen
def load_pepper():
    with open("pepper.json", "r") as f:
        data = json.load(f)
        return data["pepper"]

PEPPER = load_pepper()

# Lädt den Inhalt der JSON-Datei als Dictionary
def load_db():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

# Speichert das Dictionary zurück in die JSON-Datei
def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

# Erzeugt einen zufälligen Salt (hexadezimaler String)
def generate_salt(length=16):
    return os.urandom(length).hex()

# Erstellt den Passwort-Hash aus Passwort, Pepper und Salt
def hash_password(password, salt):
    return hashlib.sha256((password + PEPPER + salt).encode()).hexdigest()

# Registriert einen neuen Benutzer
def register_user(username, password):
    db = load_db()

    # Prüft, ob der Benutzername schon existiert
    if any(user['username'] == username for user in db['users']):
        return False  # Registrierung abgelehnt

    # Salt erzeugen und Passwort hashen
    salt = generate_salt()
    hashed = hash_password(password, salt)

    # Benutzerinformationen in die "Datenbank" schreiben
    db['users'].append({'username': username, 'salt': salt, 'hash': hashed})
    save_db(db)
    return True  # Registrierung erfolgreich

# Prüft, ob Login-Daten korrekt sind
def verify_login(username, password):
    db = load_db()

    # Suche nach dem Benutzer in der "Datenbank"
    user = next((u for u in db['users'] if u['username'] == username), None)
    if not user:
        return False  # Benutzer existiert nicht

    # Berechne den Hash mit eingegebenem Passwort und gespeicherten Salt
    computed_hash = hash_password(password, user['salt'])

    # Vergleich: ist der berechnete Hash gleich dem gespeicherten Hash?
    return computed_hash == user['hash']

