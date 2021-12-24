import gui
currentUser = ''

while (currentUser != -1):
    # currentUser will be a username if the credentials are entered correctly
    # Otherwise currentUser will be -1
    currentUser = gui.displayLogInScreen()
    # print('(IN MAIN) Current User: ' + str(currentUser))
    # print('(IN MAIN) Player List: ' + str(players))
    if (currentUser != -1):
        gui.displayUserScreen(currentUser)

    # playerNames = getPlayerNames(numPlayers)

    # print(playerNames)

print("Program Finished")
