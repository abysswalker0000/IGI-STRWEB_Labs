import func_task1
import random


def input_list():
    lst = []
    n = int(input("Enter num of elements in list: "))
    for i in range(n):
        while True:
            try:
                num = float(input(f"Enter {i+1} element: "))
                lst.append(num)
                break
            except ValueError:
                print("Error, incorrect input.")
    return lst

def find_product_positive(lst):
    product = 1
    for num in lst:
        if num > 0:
            product *= num
    return product

def init_with_random_generator(length, start, end):
    return [random.randint(start, end) for _ in range(length)]

def find_sum_before_min_abs(lst):
    min_abs_index = lst.index(min(lst, key=abs))
    sum_before_min = sum(lst[:min_abs_index])
    return sum_before_min

def print_list(lst):
    print("List:")
    for i, num in enumerate(lst, 1):
        print(f"{i}. {num}")


@func_task1.decorator_for_menu
def input_for_task5():
    range = 5
    sequence = init_with_random_generator(range,-10, 6)
    print("Init with generator:", sequence)
    product_positive = find_product_positive(sequence)
    sum_before_min_abs = find_sum_before_min_abs(sequence)
    
    print_list(sequence)
    print(f"Muti-res: {product_positive}")
    print(f"Sum-res: {sum_before_min_abs}")


    elements = input_list()
    
    product_positive = find_product_positive(elements)
    sum_before_min_abs = find_sum_before_min_abs(elements)
    
    print_list(elements)
    print(f"Muti-res: {product_positive}")
    print(f"Sum-res: {sum_before_min_abs}")