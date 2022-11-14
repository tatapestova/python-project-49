from random import randint
from math import sqrt


def prime():
    condithion_game = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    question = randint(1, 100)
    index = 2
    while index <= sqrt(question):
        if question % index == 0:
            correct_answer = "no"
            break
        index += 1
    else:
        correct_answer = "yes"
    return condithion_game, question, correct_answer
