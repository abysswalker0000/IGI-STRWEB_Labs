import func_task1

def count_uppercase_letters(text):  
    count = sum(1 for char in text if char.isupper())  
    return count

def find_first_word_with_z(text):
    words = text.replace(',', '').split()
    for i, word in enumerate(words):
        if 'z' in word.lower():
            return word, i+1
    return None, -1

def exclude_words_starting_with_a(text):
    words = text.replace(',', '').split()
    filtered_words = [word for word in words if not word.lower().startswith('a')]
    return ' '.join(filtered_words)


@func_task1.decorator_for_menu
def input_for_task4():
    text ="So she was considering in her own mind, zimbabwe as well as she could, for the hot day made her feel very sleepy and stupid, whether the pleasure of making a daisy-chain would be worth the trouble of getting up and picking the daisies, when suddenly a White Rabbit with pink eyes ran close by her."
    print("Choose task(1, 2 or 3):")
    task_choice = int(input())
    if task_choice == 1:
        print("Result: ",count_uppercase_letters(text))
    elif task_choice == 2:
        print("Result: ",find_first_word_with_z(text))
    elif task_choice == 3:
        print("Result: ", exclude_words_starting_with_a(text))
    else:
        print( "Inccorect input")

