import re
string = input('Enter password: ')
pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@+=-])[a-zA-Z0-9$#@+=-]{8,}$'
match = re.fullmatch(pattern, string)
print('Password is correct'if match else 'Password is incorrect, try again')