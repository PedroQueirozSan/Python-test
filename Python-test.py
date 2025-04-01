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