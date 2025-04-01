while True:
    name = input('What is your name? ')
    fst_name = name + ' '

    scnd_name = input('\nWhat is your last name? ')

    full_name = fst_name.upper() + scnd_name.upper()
    print('\n' + full_name)
    confirmation = input('Is your name correct? (YES/NO) ').strip().lower()

    if confirmation == 'yes':
        print('\nThank you!')
        break

    else:
        print('\nRestarting\n')

while True:
    color = input('\nWhat is yor favorite color? ')
    color_confirmation = color + ' '

    confirmation_color = input('\nDo you realy like the color? (YES/NO) ' + color_confirmation).strip().lower()

    if confirmation_color == 'yes':
        print('\nThank you')
        break

    else:
        print('\nRestarting')