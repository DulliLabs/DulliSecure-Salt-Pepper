from auth import register_user, verify_login

print("1.) Registrieren\n2.) Login")
choice = input("Auswahl: ")

username = input("Name: ")
password = input("Passwort: ")

if choice == "1":
    if register_user(username, password):
        print("Registrierung erfolgreich.")
    else:
        print("Existiert bereits.")
elif choice == "2":
    if verify_login(username, password):
        print("Login erfolgreich!")
    else:
        print("Login fehlgeschlagen!")
else:
    print("Ungültige Auswahl.")
