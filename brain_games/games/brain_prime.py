from random import randint
from math import sqrt


def prime():
    condition = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = randint(2, 100)
    index = 2
    while index <= sqrt(question):
        if question % index == 0:
            correct = "no"
            break
        index += 1
    else:
        correct = "yes"
    return condition, question, correct
