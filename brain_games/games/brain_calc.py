from random import randint, choice


def calc():
    condithion_game = 'What is the result of the expression?'
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_operator = choice('-*+')
    questhion = f'{random_number1} {random_operator} {random_number2}'
    subtraction = random_number1 - random_number2
    addithion = random_number1 + random_number2
    multiplication = random_number1 * random_number2
    if random_operator == '-':
        correct_answer = str(subtraction)
    elif random_operator == '+':
        correct_answer = str(addithion)
    elif random_operator == '*':
        correct_answer = str(multiplication)
    return condithion_game, questhion, correct_answer
