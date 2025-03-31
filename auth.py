import json, hashlib, os

DB_FILE = 'db.json'

PEPPER = os.getenv("PEPPER_SECRET", "default_pepper")

def load_db():
    with open(DB_FILE, 'r') as f:
        return json.load(f)

def save_db(data):
    with open(DB_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def generate_salt(length=16):
    return os.urandom(length).hex()

def hash_password(password, salt):
    return hashlib.sha256((password + PEPPER + salt).encode()).hexdigest()

def register_user(username, password):
    db = load_db()
    if any(user['username'] == username for user in db['users']):
        return False  # Benutzer existiert schon

    salt = generate_salt()
    hashed = hash_password(password, salt)
    db['users'].append({'username': username, 'salt': salt, 'hash': hashed})
    save_db(db)
    return True

def verify_login(username, password):
    db = load_db()
    user = next((u for u in db['users'] if u['username'] == username), None)
    if not user:
        return False

    computed_hash = hash_password(password, user['salt'])
    return computed_hash == user['hash']
