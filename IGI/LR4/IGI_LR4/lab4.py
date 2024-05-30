from input_check import input_int
import task1, task2, task3, task4, task5

def main():
    '''Вызов меню'''
    print("Выберите задание: ")
    print("1 Задание")
    print("2 Задание")
    print("3 Задание")
    print("4 Задание ")
    print("5 Задание")
    print()

    task = 0
    while(task < 1 or task > 6): 
        task = input_int()
        
    if task == 1: task1.task1()
    elif task == 2: task2.task2()
    elif task == 3: task3.task3()
    elif task == 4: task4.task4()
    elif task == 5: task5.task5()

if __name__ == "__main__":
    while True:
        main()
        exit = input("Хотите завершить программу?").lower() in ("да")
        if exit: break