import random

def comp_choice():
  choices = list(range(6))
  return random.choice(choices)

def winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return True
  else:
    return False

def play_game():
  while True:
   user_choice = int(input("Guess a number between 0 and 5: "))
   computer_choice = comp_choice()
   print(f'Computer chose {computer_choice}')
   if winner(user_choice, computer_choice):
     print('You guessed it right!')
     break
   else:
     print('Not quite! One more game.')

play_game()
