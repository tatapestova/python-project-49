from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_round():
    question = randint(1, 100)
    if question % 2 == 0:
        correct = "yes"
    else:
        correct = "no"
    return question, correct
