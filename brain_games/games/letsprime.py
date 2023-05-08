from random import randint 
import math

rule_of_game = 'Answer "yes" if given number is prime. Otherwise answer "no"'

def is_prime(a):
        number_sqrt = int(math.sqrt(a)) 
        divisors = range(2, (number_sqrt + 1))
    # Если число не простое, то в отрезке от 1 до квадратного корня числа, точно будут его делители.
        for element in divisors:
            if a % element == 0:
                 return 'no'
        return 'yes'


def lets_play():
    a = randint(3, 15)
    question = f"{a}"
    correct_answer = is_prime(a)
    
    return correct_answer, question