import hashlib

def combocreator(username, password):
    encoded = password.encode()
    passwordEncrypted = hashlib.sha512(encoded).hexdigest()
    combo = username+":"+passwordEncrypted+"\n"
    return combo