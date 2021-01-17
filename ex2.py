import re
string = input('Введите номер телефона: ')
pattern = r'^[(]?[+]?(?:38){0,1}[)]?[- ]?([\d]{3})[- ]?([\d]{3})[- ]?([\d]{2})[- ]?([\d]{2})$'
try:
    (d1, d2, d3, d4) = re.findall(pattern, string)[0]
    print('(+38)' + ' ' + d1 + ' ' + d2 + '-' + d3 + '-' + d4)
except IndexError:
    print('Невозможно определить номер')