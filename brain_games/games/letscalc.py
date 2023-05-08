from random import randint, choice
from operator import add, sub, mul

RULE_OF_GAME = 'What is the result of the expression?'


def lets_play():
    '''
    Функция генерирует случайное арифметическое выражаение.
    Запрашивает ответ у пользователя. Возвращает результат
    '''
    a = randint(1, 10)
    b = randint(1, 10)
    operation = [("+", add), ("-", sub), ("*", mul)]
    operator, func = choice(operation)  # tuple(str, Callable)
    correct_answer = str(func(a, b))
    question = f'{a} {operator} {b}'
    return correct_answer, question
