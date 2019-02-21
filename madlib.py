print("Please enter a word, number or phrase in the prompts provided")

"""
A command Line Madlib program that takes in user input, writes into new file and prints to the screen.

"""

import re

def get_template():
    """
    Inital reading of the given file

    """
    with open('./initial_text.txt', 'r') as template:
        read_data = template.read()
    return read_data

def generate_prompts(str):
    """
    Using regex to pull out the defining words inbetween {}

    """
    words = []
    user_input = []
    words += re.findall(r"(?<={)[\w<>' -]+(?=})", str)
    for word in words:
        user_input.append(input('Please give me a new ' + word + ': '))
    return user_input

def generate_new_string(arr, str):
    """
    Adding new string to original file
    """
    emptied_string = re.sub((r"(?<={)[\w<>' -]+(?=})"), '', str)
    final_string = emptied_string.format(*arr)
    return final_string

def write_result(str):
    """
    Writing new output to a new file if file doesnt exist.
    """
    with open('./madlib_result.txt', 'w') as result:
        result.write(str)

if __name__ == "__main__":
    original_string = get_template()
    user_input = generate_prompts(original_string)
    final_string = generate_new_string(user_input, original_string)
    write_result(final_string)
    print(final_string)