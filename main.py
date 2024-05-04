
#import choice from python library
from random import choice

#define the choices
choices = ['rock', 'paper', 'scissors']

#defining game_winner function and rules of the game
def game_winner(computer_choice , user_choice):
    if computer_choice == user_choice:
        return 'it is a tie'
    elif((computer_choice == 'rock' and user_choice == 'scissors' ) or
        (computer_choice == 'paper' and user_choice == 'rock') or 
        (computer_choice == 'scissors' and user_choice == 'paper')):
       return 'computer wins!'
    else:
        return 'user wins!' 
    
#Get computer_choice
#computer_choice = choice (['rock', 'paper', 'scissors'])

#Get user_choice 
#user_choice = input ("Please enter 'rock', 'paper', or 'scissors': ")

# Calling the result
#result = game_winner(computer_choice, user_choice)   
#print(result)

def play_game (max_rounds):
    computer_score = 0
    user_score = 0
    round_count = 0

    while round_count < max_rounds:
        round_count += 1
        computer_choice = choice(choices)
        user_choice = input(f"round {round_count}: 'rock', 'paper' or 'scissors': ")

        if user_choice not in choices:
            print('Invalid choice. Try again')
            continue

        result = game_winner(computer_choice, user_choice)

        if result == 'computer wins!':
            computer_score += 1
            print(f"You chose {user_choice}, and the computer chose {computer_choice}. The computer wins this round: ")

        elif result == 'user wins!' :
            user_score += 1
            print(f"You chose{user_choice}, and the computer chose {computer_choice}. You win this round: ")
             
        else:
            print(f'You both chose {user_choice}. It is a tie!')
        
        print(f"score: You {user_score} - computer {computer_score}")

        
        if user_score > computer_score:
            print('congratulations! You win the game')
        elif user_score < computer_score:
            print('sorry, the computer wins the game')
        else:
            print('It is a tie game!')

play_game(3)

