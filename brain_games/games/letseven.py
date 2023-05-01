from random import randint

rule_of_game = 'Answer "yes" if the number is even, otherwise answer "no".'


def lets_play() -> str:
    question = randint(1, 100)

    if question % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'

    return  correct_answer, question

