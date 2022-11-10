import games.logics
from random import randint, choice
import prompt


def calc():
    games.logics.welcome_user()
    question = 'What is the result of the expression?'
    games.logics.question()
    index = 1 
    while index <= 3:
        random_number1 = randint(1, 100)
        random_number2 = randint(1, 100)
        random_operator = choice('-*+')
        print(f'Question: {random_number1} {random_operator} {random_number2}')
        user_answer = prompt.string('Your answer: ')
        subtraction = random_number1 - random_number2
        addithion = random_number1 + random_number2
        multiplication = random_number1 * random_number2 
        if random_operator == '-' and user_answer == str(subtraction):
            correct_asnwer = str(subtraction)
            print('Correct!')
        elif random_operator == '+' and user_answer == str(addithion):
            correct_asnwer = str(addithion)
            print('Correct!')
        elif random_operator == '*' and user_answer == str(multiplication):
            correct_asnwer = str(multiplication)
            print('Correct!') 
        else:
            if random_operator == '-':
                correct_asnwer = subtraction
            elif random_operator == '+':
                correct_asnwer = addithion
            elif random_operator == '*':
                correct_asnwer = multiplication
            print(f''''{user_answer}' is wrong answer ;(. Correct answer was '{correct_asnwer}'.
Let's try again, {name}!''')
            break
        index += 1
    games.logics.finish()
