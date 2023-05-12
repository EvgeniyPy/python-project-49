from random import randint, choice
from operator import add, sub, mul

RULE_OF_GAME = 'What is the result of the expression?'

OPERATION = [("+", add), ("-", sub), ("*", mul)]


def get_game():
    '''
    Функция генерирует случайное арифметическое выражаение.
    Запрашивает ответ у пользователя. Возвращает результат
    '''
    random_number_1 = randint(1, 10)
    random_number_2 = randint(1, 10)

    operator, func = choice(OPERATION)  # tuple(str, Callable)
    correct_answer = str(func(random_number_1, random_number_2))
    question = f'{random_number_1} {operator} {random_number_2}'
    return correct_answer, question
