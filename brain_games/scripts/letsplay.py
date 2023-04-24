import prompt
from random import randint




def welcome_user() -> str:
    _name = prompt.string('May I have your name?:')
    print(f'Hello, {_name}')
    return _name

def lets_play(_name) -> str:
     score = 0
     while score < 3:
          _random = randint(1, 100)
          print('Question:', _random)
          _result = prompt.string('Your answer:')

          if (_result == 'yes' and _random % 2 == 0) or (_result == 'no' and _random % 2 != 0):
               score += 1
               print("Correct!")
               
          elif _result== 'yes' and _random % 2 !=0:
               return f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {_name}!"
          elif _result == 'no' and _random % 2 == 0:
               return f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {_name}!"
          else: 
               return "wrong answer"
     return f"Congratulations, {_name}"
    

     # return _random

# def even_num():
#       _result = prompt.string('Your answer:')
#       return _result


# def condition(even_num: str, _random: int, _name:str) -> str:
#      """
#      Проверяет условия
#      """
#      if (even_num == 'yes' and _random % 2 == 0) or (even_num == 'no' and _random % 2 != 0):
#           return "Correct!"
                
#      elif even_num == 'yes' and _random % 2 !=0:
#           return f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again,{_name}!"
#      elif even_num == 'no' and _random % 2 == 0:
#           return f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {_name}!"
#      else: 
#           return "wrong answer"
     
          

     
     


        
   



    
        

