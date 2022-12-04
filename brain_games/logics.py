import prompt

MAX_ROUNDS = 3


def start_of_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.DESCRIPTION)
    index = 1
    while index <= MAX_ROUNDS:
        question, correct = game.generate_round()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct:
            print('Correct!')
        else:
            print(f"'{user_answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct}'. Let's try again, {name}!")
            break
        index += 1
    if correct == user_answer:
        print(f'Congratulations, {name}!')
