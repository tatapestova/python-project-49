from random import randint, choice


def progression():
    condithion_game = 'What number is missing in the progression?'
    start_number = randint(1, 100)
    finish_number = randint(100, 200)
    length = randint(5, 10)
    step = randint(1, 10)
    l = list(range(start_number, finish_number, step))
    progression = l[:length]
    random_number = choice(progression)
    index = progression.index(random_number)
    correct_answer = str(random_number)
    progression[index] = '..'
    questhion = ' '.join(map(str, progression))
    return condithion_game, questhion, correct_answer
