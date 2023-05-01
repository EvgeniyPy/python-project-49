from random import randint
from math import gcd

rule_of_game = "Find the greatest common divisor of given numbers."


def lets_play():
    a = randint(1, 100)
    b = randint(1, 100)
    question = f"{a} {b}"
    correct_answer = str(gcd(a, b))
    return  correct_answer, question