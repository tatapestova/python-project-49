import prompt

rounds = 3


def start_of_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    condithion, question, correct_answer = game()
    print(condithion)
    index = 1
    while index <= rounds:
        condithion, question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
        else:
            print(f''''{user_answer}' is wrong answer ;(.
Correct answer was '{correct_answer}'.
Let's try again, {name}!''')
            break
        index += 1
    if correct_answer == user_answer:
        print(f'Congratulations, {name}!')
