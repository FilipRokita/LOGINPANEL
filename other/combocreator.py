def combocreator(username, password):
    import hashlib
    encoded = password.encode()
    passwordEncrypted = hashlib.sha512(encoded).hexdigest()
    combo = username+":"+passwordEncrypted+"\n"
    return combo