import PySimpleGUI as sg
import myfunctions

sg.theme('DarkBlue1')   # Add a touch of color
players = {"Braydon": { "password" : "354", "cards": ["2", "2", "3"] }, "Matt": { "password" : "123", "cards": ["2", "4", "5"]}}
cardPile = ['2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','2','3','3','3','3','3','3','4','4','4','4','4','4','5','5','5','5']
dicardPile = []

def displayLogInScreen():
    currentUser = ''
    currentUser = displayUserLogInScreenPopUp(players)

    return currentUser

def displayUserLogInScreenPopUp():
    currentUser = -1
    # All the stuff inside your window.
    userScreenPopUpLayout = [ [sg.Text('Username:',size=(8, 1)), sg.InputText(key='-USR-')],
            [sg.Text('Password:',size=(8, 1)), sg.InputText(key='-PWR-',password_char='*')],
            [sg.Button('Login',bind_return_key=True),sg.Button('New User'),sg.Button('Close Program',button_color='Red')] ]
    # Create the Window
    window = sg.Window('Main Login', userScreenPopUpLayout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            currentUser = 0
            break
        if event == 'Close Program':
            if(sg.popup_ok_cancel('Are you sure you want to end the program') == 'OK'):
                if(sg.popup_ok_cancel('Are you really sure') == 'OK'):
                    currentUser = -1
                    break
        if event == 'New User':
            players = createNewUserScreenPopUp(players)

        elif event == 'Login':
            username = values['-USR-']
            password = values['-PWR-']
            if(myfunctions.checkUserCredentials(players, username, password)):
                currentUser = username
                break

    window.close()
    return currentUser

def displayUserScreen(userName):
    # All the stuff inside your window.
    userScreenPopUpLayout = [[sg.Text('Cards:'), sg.Text(players.get(userName).get('cards'))],
        [sg.Button('Logout',button_color='Red')]]
    # Create the Window
    window = sg.Window(userName + '\'s information', userScreenPopUpLayout, size=(325,75))
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # if user closes window or clicks cancel
            currentUser = 0
            break
        if event == 'Logout':
            currentUser = -1
            break


    window.close()
    return 0

def createNewUserScreenPopUp():
    # All the stuff inside your window.
    createUserPopUpLayout = [ [sg.Text('Username:',size=(14, 1)), sg.InputText(key='-USR-')],
            [sg.Text('Password:',size=(14, 1)), sg.InputText(key='-PWR-',password_char='*')],
            [sg.Text('Confirm Password:',size=(14, 1)), sg.InputText(key='-PWRCONFIRM-',password_char='*')],
            [sg.Button('Create',bind_return_key=True), sg.Button('Cancel')] ]
    # Create the Window
    window = sg.Window('Create User', createUserPopUpLayout)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            break
        
        if event == 'Create':
            username = values['-USR-']
            password = values['-PWR-']
            passwordConfirm = values['-PWRCONFIRM-']
            if(myfunctions.checkNewUserInformation(players, username, password, passwordConfirm)):
                players = myfunctions.createNewUser(players, username, password)
                break

    window.close()
    return players
