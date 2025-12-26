"""
Number Guessing Game
Author: Satria Dwi Cahya
Purpose: Practice basic Python Logic
"""

import os
import random
os.system('cls')


print('Welcome to the Number Guessing Game!')
print('------------------------------------')

choice_mode = input('Do you want a specific value? (Y/N): ').lower()

control_variabel = 0
attempt = 0

if choice_mode == 'y':
    print('Select range of value for the number')
    minimum_number = input('Minimum Number: ')
    maximum_number = input('Maximum Number: ')

    right_number = random.randint(int(minimum_number), int(maximum_number))
    
    while control_variabel < 1:
        user = int(input(f'Guess the number (between {minimum_number} and {maximum_number}): '))

        if user > right_number:
                print('Too high! Try again.')
                attempt += 1
        elif user < right_number:
                print('Too low! Try again.')
                attempt += 1
        else:
                attempt += 1
                control_variabel += 1
                print('Congratulations! You guessed the number in ', attempt, ' attempts')
else:
    right_number = random.randint(1, 99)
    
    while control_variabel < 1:
        user = int(input('Guess the number (between 1 and 100): '))

        if user > right_number:
            print('Too high! Try again.')
            attempt += 1
        elif user < right_number:
            print('Too low! Try again.')
            attempt += 1
        else:
            attempt += 1
            control_variabel += 1
            print()
            print('Congratulations! You guessed the number in ', attempt, ' attempts')