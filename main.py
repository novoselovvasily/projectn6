"""Определение платежной системы карты"""
def platsys():
    n=input('Введите номер карты:')
    if n[0] == '4':
        print('Visa')
    elif n[0] == '5':
        print('MasterCard')
    elif n[:2] == '37':
        print('American Express')
    elif n[0] == '6':
        print('Discover')
    elif n[0] == '2':
        print('Мир')
    else:
        print('Неверный номер карты.')
platsys()
"""Определение правильности карты"""
def proper ():
    n=input('Введите номер карты:')
    if 13 <= len(n) <= 16:
        print('Номер карты правильный.')
    else:
        print('Номер карты неправильный.')
proper()