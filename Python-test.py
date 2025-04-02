from datetime import datetime
while True:
    name = input('What is your name? ')
    fst_name = name + ' '

    scnd_name = input('\nWhat is your last name? ')

    full_name = fst_name.upper() + scnd_name.upper()
    print('\n' + full_name)
    confirmation = input('Is your name correct? (YES/NO) ').strip().lower()

    if confirmation == 'yes':
        print('\nThank you!')


    else:
        print('\nRestarting...\n')
        continue

    color = input('\nWhat is yor favorite color? ')
    color_confirmation = color + ' '

    confirmation_color = input(f'\nDo you realy like the color {color_confirmation}? (YES/NO) ').strip().lower()

    if confirmation_color == 'yes':
        print('\nThank you!')

    else:
        print('\nRestarting...')
        continue

    year = input('\nWhen were you born? ')
    age_by_year = datetime.now().year - int(year)

    confirmation_age = input(f'\nAre you {str(age_by_year)}? (YES/NO) ').strip().lower()

    if confirmation_age == 'yes':
        print('\nThank you!')


    else:
        neg_age_by_year = age_by_year - 1
        print('Thank you!')

    cat = input('\nDo you have a cat? (YES/NO) ').strip().lower()

    if cat == 'yes':
        cat_breed = input('\nWhat kind of cat? ')
        other_cat = input('\nWould you like to have another cat? ')
        number_cats = input('\nHow many? ')
        why_cats = input('\n why do you love cats? ')
        print('\nThank you!')

    else:
        print('\n:(')
        print('thanks.')
        break