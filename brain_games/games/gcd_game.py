from random import randint
from math import gcd

RULE_OF_GAME = "Find the greatest common divisor of given numbers."


def get_game():
    random_number_1 = randint(1, 100)
    random_number_2 = randint(1, 100)
    question = f"{random_number_1} {random_number_2}"
    correct_answer = str(gcd(random_number_1, random_number_2))
    return correct_answer, question
