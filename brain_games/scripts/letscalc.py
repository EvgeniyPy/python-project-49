import prompt

from random import randint, choice
from operator import add, sub, mul


def welcome_user() -> str:
    '''Функция запрашивает имя и возвращает приветствие в ввиде Приветствие + имя '''
    _name = prompt.string('May I have your name?:')
    print(f'Hello, {_name}')
    return _name


def lets_play(_name) -> str:
    '''Функция генерирует случайное арифметическое выражаение. Запрашивает ответ у пользователя. Возвращает результат  '''
    score = 0
    while score < 3:
        a = randint(1, 10)
        b = randint(1, 10)
        operation = [("+", add), ("-", sub), ("*", mul)]
        operator, func = choice(operation)
        correct = func(a, b)

        print(f'Question: {a} {operator} {b}')
        _result = prompt.string('Your answer:')

        if int(_result) == correct:
            print("Correct!")
            score += 1

        else:
            print(f'"{_result}" is wrong answer ;(. Correct answer was "{correct}"')
            return f"Let's try again, {_name}"

    return f"Congratulations, {_name}"
