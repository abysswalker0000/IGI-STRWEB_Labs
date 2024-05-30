def input_int():
    '''Целое'''
    while True:
        try:
            int_num = int(input())
            return int_num
        except ValueError:
            print("Ошибка ввода: введите целое число!")
            continue


def input_float():
    '''Вещественное'''
    while True:
        try:
            float_num = float(input())
            return float_num
        except ValueError:
            print("Ошибка ввода: введите вещественное число!")
            continue
    
def input_positive_int(input_int):
    '''Положительное'''
    while True:
        num = input_int()
        if num > 0: return num
        else: print("Ошибка: введите положительное число!")