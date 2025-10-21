def haunted_login(username, password):
    credentials = {
    "ghost": "boo123", 
    "witch": "spellbound", 
    "zombie": "brains!"
    }
    if username in credentials:
        if credentials[username] == password:
            print("welcome back from the grave,", username)
        else:
            print("Incorrect password. Try again, if you dare.")
    else:
        print("user not found. Register through the proper ritual...")

haunted_login("ghost", "boo123")
haunted_login("vampire", "fangs!")
haunted_login("witch", "spellbound")