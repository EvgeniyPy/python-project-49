from random import randint

RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return right_answer


def get_game() -> str:
    number = randint(1, 100)
    correct_answer = is_even(number)
    return correct_answer, number
