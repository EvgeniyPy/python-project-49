from brain_games.scripts import letsplay


def main():
    print("Welcome to the Brain Games!")
    _name = letsplay.welcome_user()
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    _number = letsplay.lets_play(_name)
    print(_number)
    # aswer = letsplay.even_num()

    # _result = letsplay.condition(aswer, _number, _name)
    # print(_result)

   
   



   
    
"""  """

if __name__ == '__main__':
    main()
