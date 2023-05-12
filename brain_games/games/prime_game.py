from random import randint
import math

RULE_OF_GAME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(random_number):
    number_sqrt = int(math.sqrt(random_number))
    divisors = range(2, (number_sqrt + 1))

    for element in divisors:
        if random_number % element == 0:
            return 'no'
    return 'yes'


def get_game():
    random_number = randint(3, 15)
    question = f"{random_number}"
    correct_answer = is_prime(random_number)

    return correct_answer, question
