
#import choice from python library
from random import choice

#defining a function and rules of the game
def game_winner(computer_choice , user_choice):
    if computer_choice == user_choice:
        return 'it is a tie'
    elif((computer_choice == 'rock' and user_choice == 'scissors' ) or
        (computer_choice == 'paper' and user_choice == 'rock') or 
        (computer_choice == 'scissors' and user_choice == 'paper')):
       return f'computer chose {computer_choice}. computer wins!'
    else:
        return f'computer chose {computer_choice}. user wins!' 
    
#Get computer_choice
computer_choice = choice (['rock', 'paper', 'scissors'])

#Get user_choice 
user_choice = input ("Please enter 'rock', 'paper', or 'scissors': ")
