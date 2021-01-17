import re
string = input('Введите номер: ')
pattern = r'\b[АВЕІКМНОРСТХ|ABEIKMHOPCTX]{2}\d{4}[АВЕІКМНОРСТХ|ABEIKMHOPCTX]{2}\b'
match = re.fullmatch(pattern, string)
print('YES'if match else 'NO')