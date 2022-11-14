from random import randint


def even():
    condithion_game = 'Answer "yes" if the number is even, otherwise answer "no".'
    question = randint(1, 100)
    if question % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return condithion_game, question, correct_answer
