name = input('What is your first name? ')
print('ok ' + name.title())

last = input('What is your last name? ')
color = input(f'{name.title()} {last.title()} what is your favorite color? ')

print(f'{name.title()} likes ' + color)

born = input('When were you born? ')
age = 2025 - int(born)

month = input(f'Are you going to be {age}? (yes/no) ').strip().lower()

if month == "yes":
    print(f'{name.title()} {last.title()} will be {age} years old.')
if month == "yep":
    print(f'{name.title()} {last.title()} will be {age} years old.')
else:
    print(f'Oh, so you are still {age - 1} years old!!')