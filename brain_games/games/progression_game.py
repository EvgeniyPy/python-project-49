from random import randint


RULE_OF_GAME = "What number is missing in the progression?"


def get_random_progression():
    pass


def get_game():
    """Функция создае рандомную прогресиию
    и возвращает ее с пропущенным элементом(...)"""
    start = randint(1, 50)
    step = randint(2, 7)
    length = randint(5, 10)
    _progression = list(range(start, start + step * length, step))
    random_index = randint(0, len(_progression) - 1)

    correct_answer = _progression[random_index]
    _progression[random_index] = '..'
    question = " ".join(map(str, _progression))
    return str(correct_answer), question
