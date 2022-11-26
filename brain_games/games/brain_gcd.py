from random import randint
import math


def gcd():
    condition = 'Find the greatest common divisor of given numbers.'
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_number2}'
    correct = str(math.gcd(random_number1, random_number2))
    return condition, question, correct
