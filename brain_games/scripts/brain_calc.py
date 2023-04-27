from brain_games.scripts import letscalc


def main():
    print("Welcome to the Brain Games!")
    _name = letscalc.welcome_user()
    
    print('What is the result of the expression?')
    _calc = letscalc.lets_play(_name)
    print(_calc)
    
   
   



   


if __name__ == '__main__':
    main()
