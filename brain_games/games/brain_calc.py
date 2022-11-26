from random import randint, choice


def calc():
    condition = 'What is the result of the expression?'
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    random_operator = choice('-*+')
    question = f'{random_number1} {random_operator} {random_number2}'
    if random_operator == '-':
        subtraction = random_number1 - random_number2
        correct = str(subtraction)
    elif random_operator == '+':
        addithion = random_number1 + random_number2
        correct = str(addithion)
    elif random_operator == '*':
        multiplication = random_number1 * random_number2
        correct = str(multiplication)
    return condition, question, correct
