from random import randint


def even():
    condition = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        correct = "yes"
    else:
        correct = "no"
    return condition, question, correct
