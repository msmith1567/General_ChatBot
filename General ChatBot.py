# Author: Maximillian Smith
# Date Created: 12/1/2025
# Date Last Modified: 12/1/2025

# This is a small chatbot project I made

bot_name: str = 'Rockwell'
print(f' Hello! My name is {bot_name}! I am your helpful assistant, how may I help you?')

while True:
    user_input: str = input('You: ').lower()

    if user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hello there! what is the plan for today?')
    elif user_input in ['goodbye', 'bye']:
        print(f'{bot_name}: Fairwell!')
    elif user_input in ['+', 'add', 'please help add']:
        print(f'{bot_name}: Sure! Lets add!')
        try:
            num1: float = float(input(f'Enter a number: '))
            num2: float = float(input(f'Enter a second number: '))
            print(f'{bot_name}: Easy! here is the answer: {num1 + num2}')
        except ValueError:
            print(f'{bot_name}: Sorry, I didn\'t understand your input!')
    elif user_input in['subtract', '-', 'please help subtract']:
        print(f'{bot_name}: That is no problem, go ahead and input your first number you\'d like to subtract')
        try:
            num1: float = float(input(f'Enter a number: '))
            num2: float = float(input(f'Enter a second number: '))
            print(f'{bot_name}: Easy! here is the answer: {num1 - num2}')
        except ValueError:
            print(f'{bot_name}: Sorry, I didn\'t understand your input!')
    else:
        print(f'{bot_name}: Sorry, I don\'t understand what you\'re saying')