import random

def checkNewUserInformation(players, username, password, passwordConfirm):
    isValid = True
    if username in (players.keys()):
        isValid = False
        sg.popup("User already exists")
    if len(username) <= 1:
        isValid = False
        sg.popup("Username must be at least 2 characters")
    if len(password) <= 1:
        isValid = False
        sg.popup("Password must be at least 2 characters")
    if password != passwordConfirm:
        isValid = False
        sg.popup("Passwords do not match")

    return isValid

def checkUserCredentials(players, username, password):
    isCorrectCredentials = False
    try:
        if players[username]['password'] == password:
            isCorrectCredentials = True
        else:
            sg.popup("You have entered incorrect login credentials")
    except KeyError:
        sg.popup("User does not exist")
    return isCorrectCredentials

def createNewUser(players, username, password):
    try:
        players[username] = {}
        players[username]['password'] = password
        players[username]['cards'] = []
    except:
        sg.popup("Error creating user")
    return players

def shuffleCards (cards):
    random.seed()
    random.shuffle(cards)
    return cards