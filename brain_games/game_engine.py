import prompt

WIN_SCORE = 3

def launch_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name?:')
    print(f'Hello, {name}')
    print(game.RULE_OF_GAME)

    SCORE = 0

    while SCORE < WIN_SCORE:
        correct_answer, question = game.lets_play()
        print(f'Qusetions: {question}')
        player_answer = prompt.string('You answer: ')

        if player_answer == correct_answer:
            print('Correct')
            SCORE += 1
        else:
            print(f"'{player_answer}' is wrong answer ;(." 
              f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

