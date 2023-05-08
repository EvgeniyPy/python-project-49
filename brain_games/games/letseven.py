from random import randint

RULE_OF_GAME = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(question):
    right_answer = 'yes' if question % 2 == 0 else 'no'
    return right_answer




def lets_play() -> str:
    question = randint(1, 100)
    correct_answer = is_even(question)
    return  correct_answer, question
    

