import func_task1


def is_binary_number(input_str):
    for char in input_str:
        if char not in ['0', '1']:
            return False
    return True


@func_task1.decorator_for_menu
def input_for_task3():
    print("Enter string: ")
    user_input=input()
    if is_binary_number(user_input):
        print("String is a binary number.")
    else:
        print("string is not a binary number")
   
