from random import randint
import math


def gcd():
    condithion = 'Find the greatest common divisor of given numbers.'
    random_number1 = randint(1, 100)
    random_number2 = randint(1, 100)
    question = f'{random_number1} {random_number2}'
    correct_answer = str(math.gcd(random_number1, random_number2))
    return condithion, question, correct_answer
