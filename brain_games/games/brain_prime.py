from random import randint
from math import sqrt


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime(number):
    index = 2
    while index <= sqrt(number):
        if number % index == 0:
            return False
        index += 1
    else:
        return True


def generate_round():
    question = randint(2, 100)
    result = prime(question)
    if result is False:
        correct = 'no'
    else:
        correct = 'yes'
    return question, correct
