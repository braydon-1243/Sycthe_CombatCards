import PySimpleGUI as sg
cards = ["5", "4", "3"]
sg.theme('DarkBlue1')   # Add a touch of color
closePopup = 0
while closePopup == 0:
    # All the stuff inside your window.
    layout1 = [ [sg.Text('Username'), sg.InputText(key='-USR-')],
                [sg.Text('Password'), sg.InputText(key='-PWR-',password_char='*')],
                [sg.Button('Login',bind_return_key=True), sg.Button('Cancel')] ]

    # Create the Window
    window = sg.Window('User Login', layout1)
    # Event Loop to process "events" and get the "values" of the inputs
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
            closePopup = 1
            break
        username = values['-USR-']
        password = values['-PWR-']
        if (username =='Braydon' and password == '123'):
            window.close()
            layout2 = [  [sg.Text('Cards')],
                        [sg.Text(cards, size=(40,1), key='-CARDS-')],
                        [sg.Button('Choose Card(s)', key='CHOOSE'),sg.CloseButton('Close')] ]
            window = sg.Window(username + '\'s Card Information', layout2)
            while True:
                event, values = window.read()

                if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                    break

                if event == 'CHOOSE':
                    layout3 = [ [sg.Text('Cards')],
                                [ sg.InputCombo(('Combobox 1', 'Combobox 2'), size=(20, 1)),
                                sg.Slider(range=(0, 7), orientation='h', size=(34, 20), default_value=1)],
                                [sg.Checkbox('Checkbox', size=(10,1)),sg.Button('Cancel')] ]
                    window = sg.Window('Choose Cards', layout3)
                    while True:
                        event, values = window.read()  
                        if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
                            window.close()
                            break 
        else:
            sg.popup("You have entered incorrect login credentials")

window.close()