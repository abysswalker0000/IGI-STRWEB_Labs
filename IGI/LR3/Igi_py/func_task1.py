import math

def using_power_series(x,epsilant):   #finding math

    n=0

    m_result=math.asin(x)
    func_result=0.0

    while n<=500.0 and m_result-func_result>epsilant:
        func_result += (math.factorial(2*n)/((pow(4,n)*pow(math.factorial(n), 2)*(2*n+1))))*pow(x,2*n+1)
        n +=1

    return func_result, m_result, n


def check_number(x):
    try:
        float(x)

    except:
        print("Error, enter number")
        return False

    return True


def decorator_for_menu(func):

    def wrapper():
       
        while True:
            print("If you want to exit - type 'yes', otherwise - type something ")
            n = input()
            if(n=='yes'):
                break

            print(func())

    return wrapper



@decorator_for_menu
def input_function_for_task1():
    print("Enter x: ")
    x=input()

    while not check_number(x) or math.fabs(float(x)) >= 1:
        print("Incorrect input, Enter x: ")
        x=input()
    x = float(x)

    print("Enter eps: ")
    eps = input()

    while not check_number(eps):
        print("Incorrect input, Enter eps: ")
        eps = input()
    eps = float(eps)
    print("Start Calculation..")
    print("x\tn\tf(x)\tmath f(x)\teps\n")
    func_result, math_result, n = using_power_series(x,eps)
    result_list = [x, n, func_result, math_result, eps]
    result_string =""
    for item in result_list:
        result_string+=str(item)
        result_string+= '\t'
    return result_string