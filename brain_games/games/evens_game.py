from random import randint

RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def get_game() -> str:
    number = randint(1, 100)
    if is_even(number):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, number
