import random

# welcome prompt
welcome = """
*******************************
Play the Game of Greed!
Enter 'QUIT' at any time to exit.
*********************************
"""

# prompt user as to whether they would like to play
play_game = """
***********************
Would you like to play?
        Y or N
***********************
"""

# display rules and points system to the user
rules = """
*****************************************************************************************
1. Roll all 6 dice on your first turn.
2. Every turn must result in points being banked of the game is over.
3. You may bank as many dice/points per turn as you wish.
4. Once you bank points you may roll the remaining dice or decided to keep what you have.
5. If you roll again and get no points then your score becomes zero so choose wisely!
6. 1 scores 100 points. 5 scores 50 points. Three dice of the same number is x100 the 
number of the dice e.g. three 5s = 150 points. If you get three doubles then you get
1500 points. If every dice in one roll scores then you can roll all 6 dice again.
*****************************************************************************************
"""

# prompt user as to whether they would like to roll again or bank current points
play_or_bank = """
******************************************
Play again or bank what you have?
Type 'P' to play and 'B' to bank.
(opting to bank will result in being
asked to select die you want to set aside)
******************************************
"""

# ask the user which dice they would like to bank
bank_dice = """
********************************************
Which numbers would you like to bank?
(please enter numbers serparated by a space)
********************************************
"""

# prompt the user as to whether they would like to roll again
play_again_prompt = """
*********************************************
To play again type 'Y' or to exit type 'QUIT'
*********************************************
"""

# prompt the user to enter their score for that round
enter_score = """
*********************************************
Enter your score for this round (be honest!):
*********************************************
"""

# print welcome message, rules of the game and promt the user as to whether they would like to play
print(welcome, rules, play_game)

current_dice = [None] * 6
dice_in_bank = []
total_score = 0

# Application should simulate rolling between 1 and 6 dice
def roll_dice():
    for i in range(len(current_dice)):
        current_dice[i] = random.randint(1, 6)
    print(current_dice)

def bank_or_roll_again():
    print(play_or_bank)
    answer = str.capitalize(input())
    if answer == "P":
        roll_dice()
    elif answer == "B":
        capture_dice_banked()

# Application should allow user to set aside dice each roll
def capture_dice_banked():
    print(bank_dice)
    answer = input().split(' ')
    banked_dice(answer)

def banked_dice(arr):
    for dice in arr:
        dice_in_bank.append(dice)
    set_dice_aside(dice_in_bank)

def set_dice_aside(arr):
    for dice in arr:
        i = current_dice.index(int(dice))
        current_dice.pop(i)
    calculate_score()

def calculate_score():
    global total_score
    print(enter_score)
    answer = int(input())
    total_score += answer
    play_again()

def play_again():
    print(play_again_prompt)
    answer = str(input())
    """
    *************************
    WHERE I GOT TO LAST NIGHT
    *************************
    """
def track_scores():
    

def game_controller():
    roll_dice()
    bank_or_roll_again()

game_controller()