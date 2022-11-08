#!/usr/bin/env python3

from random import randint
import prompt


def is_even():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    index = 1
    while index <= 3:
        random_number = randint(1, 100)
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if random_number % 2 == 0 and user_answer == "yes":
            correct_asnwer = "yes"
            print('Correct!')
        elif random_number % 2 != 0 and user_answer == "no":
            correct_asnwer = "no"
            print('Correct!')
        else:
            if random_number % 2 != 0:
                correct_asnwer = "no"
            elif random_number % 2 == 0:
                correct_asnwer = "yes"
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{correct_asnwer}'.
Let's try again, {name}!''')
            break
        index += 1
    if correct_asnwer == user_answer:
        print(f'Congratulations, {name}!')


def main():
    is_even()


if __name__ == '__main__':
    main()
