import func_task1

def check_number(x):
    try:
        int(x)

    except:
        print("Error, enter number")
        return False

    return True


def check_for_task2(values):
    counter = 0 
    for value in values:  
        if value > 12:
            counter += 1
    return counter



@func_task1.decorator_for_menu
def input_for_task2():
    values = []
    while True:
        print("Enter numbers, enter 0 to exit :")
        n=input()
        if not check_number(n):
            continue
        n=int(n)
        if n==0:
            break
        values.append(n)
    return check_for_task2(values)



