def checkcred(username, password, database):
    import string

    def checkusername():
        for i in range(len(username)):
            if username[i] == ":":
                score = 0
                break
            else:
                score = 1
        return score

    def checkpass():
        special = "!@#$%^&*()-_=+"
        has_digits = 0
        has_ascii_lowercase = 0
        has_ascii_uppercase = 0
        has_special = 0
        for i in range (len(password)):
            for j in range(len(string.digits)):
                if password[i] == string.digits[j]: has_digits = 1
            for j in range(len(string.ascii_lowercase)):
                if password[i] == string.ascii_lowercase[j]: has_ascii_lowercase = 1
            for j in range(len(string.ascii_uppercase)):
                if password[i] == string.ascii_uppercase[j]: has_ascii_uppercase = 1
            for j in range(len(special)):
                if password[i] == special[j]: has_special = 1
        score = has_digits + has_ascii_lowercase + has_ascii_uppercase + has_special
        return score
    
    def checkdb():
        users = []
        f = open(database)
        for line in f:
            line = line[:-1]
            user = line.split(":")
            users.append(user[0])
        if len(users) == 0:
            score = 1
            return score
        for i in range(len(users)):
            if username == users[i]:
                score = 0
                break
            else:
                score = 1
        return score

    if checkusername() + checkpass() + checkdb() == 6:
        return True