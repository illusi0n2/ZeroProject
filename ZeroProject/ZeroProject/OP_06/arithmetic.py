def sum(a, b):
    '''Сумма 2 чисел'''
    return a + b

def diff(a, b):
    '''Разность 2 чисел'''
    return a - b

def prod(a, b):
    '''Произведение 2 чисел'''
    return a * b

def div(a, b):
    '''Частное 2 чисел'''
    try:
        return a / b
    except ZeroDivisionError:
        print('Деление на ноль запрещено')