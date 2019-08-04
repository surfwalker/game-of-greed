import math, csv, sys

default_rules = {
    "flush": 500,
    "straight": 300,
    "royal": 200,
}

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

class User:
    """This is a docstring."""

    def __init__(self):
        """Docstringing this."""
        self.round_score = []
        self.total_score = 0
        self.current_dice = [None] * 6
        self.banked_dice = []
        self.round = 0

    def roll(self, hand):
        """Docstring again."""
        for i in range(len(self.current_dice)):
        self.current_dice[i] = random.randint(1, 6)
        print(self.current_dice)
        bank_or_roll_again(arr1, arr2, num)

    def bank(self, choices):
        """Docstring againnnnnnn."""
        self.score = self.score + game.calculate_score()
        self.dice = self.dice - len(choices)

        if self.score >= 10000:
            print("Omg you won amazing how cool")
        else:
            self.roll(self.hand)

class Rules:
    """This is a docstring."""

    def __init__(self, ruleset):
        """Docstringing this."""
        self.flush = ruleset["flush"]
        self.straight = ruleset["straight"]
        self.royal = ruleset["royal"]

    def calculate_score(self, dice):
        """Docstringing this."""

        # Probably iterate over the provided dice to see if any values/combinations conform to the rules above.
        # Return the result.
        pass

def import_rules(file_path):
    try:
        # Read in your file here. Use a CSV file to make it easier to store it as a dictionary.
        # Import the csv module to do that.
        # Assign the resulting dictionary to some variable and return it.
        pass
    except Exception:
        print("File not found or uncorrect filetype; please check your filepath to a CSV.")
        what_rules()

def what_rules():
    answer = input('> ')
    global game
    try:
        if answer.lower() == 'yes':
            filepath = input('> ')
            custom_rules = import_rules(filepath)
            game = Rules(custom_rules)
        else:
            game = Rules(default_rules)
    except TypeError:
        print('invalid input. Enter yes or no.')

def main():
    print(welcome, rules, play_game)
    # print(welcome, rules, play_game)
    # global player
    # player = User()
    # # And probably some more intro stuff
    # what_rules()

    # # Something like this:
    # player.roll()


    # Don't forget to handle a KeyboardInterrupt!
main()


"""OLD CODE"""

# import random

# # welcome prompt
# welcome = """
# *******************************
# Play the Game of Greed!
# Enter 'QUIT' at any time to exit.
# *********************************
# """

# # prompt user as to whether they would like to play
# play_game = """
# ***********************
# Would you like to play?
#         Y or N
# ***********************
# """

# # display rules and points system to the user
# rules = """
# *****************************************************************************************
# 1. Roll all 6 dice on your first turn.
# 2. Every turn must result in points being banked of the game is over.
# 3. You may bank as many dice/points per turn as you wish.
# 4. Once you bank points you may roll the remaining dice or decided to keep what you have.
# 5. If you roll again and get no points then your score becomes zero so choose wisely!
# 6. 1 scores 100 points. 5 scores 50 points. Three dice of the same number is x100 the 
# number of the dice e.g. three 5s = 150 points. If you get three doubles then you get
# 1500 points. If every dice in one roll scores then you can roll all 6 dice again.
# *****************************************************************************************
# """

# # prompt user as to whether they would like to roll again or bank current points
# play_or_bank = """
# ******************************************
# Play again or bank what you have?
# Type 'P' to play and 'B' to bank.
# (opting to bank will result in being
# asked to select die you want to set aside)
# ******************************************
# """

# # ask the user which dice they would like to bank
# bank_dice = """
# ********************************************
# Which numbers would you like to bank?
# (please enter numbers serparated by a space)
# ********************************************
# """

# # prompt the user as to whether they would like to roll again
# play_again_prompt = """
# *********************************************
# To play again type 'Y' or to exit type 'QUIT'
# *********************************************
# """

# # prompt the user to enter their score for that round
# enter_score = """
# *********************************************
# Enter your score for this round (be honest!):
# *********************************************
# """

# def initialize_game():
#     current_dice = [None] * 6
#     dice_in_bank = []
#     total_score = 0
#     start_game(current_dice, dice_in_bank, total_score)

# def start_game(arr1, arr2, num):
#     print(welcome, rules, play_game)
#     answer = str.capitalize(input())
#     if answer == "Y":
#         roll_dice(arr1, arr2, num)
#     elif answer == "N":
#         handle_quit()
#     else:
#         handle_validation(answer)

# # Application should simulate rolling between 1 and 6 dice
# def roll_dice(arr1, arr2, num):
#     for i in range(len(arr1)):
#         arr1[i] = random.randint(1, 6)
#     print(arr1)
#     bank_or_roll_again(arr1, arr2, num)

# def bank_or_roll_again(arr1, arr2, num):
#     print(play_or_bank)
#     answer = str.capitalize(input())
#     print(answer)
#     if answer == "P":
#         roll_dice(arr1, arr2, num)
#     elif answer == "B":
#         capture_dice_banked(arr1, arr2, num)
#     elif answer == "QUIT":
#         handle_quit(answer)
#     else:
#         handle_validation()

# # Application should allow user to set aside dice each roll
# def capture_dice_banked(arr1, arr2, num):
#     print(bank_dice)
#     answer = input().split(' ')
#     banked_dice(answer, arr1, arr2, num)

# def banked_dice(answerArr, arr1, arr2, num):
#     for dice in answerArr:
#         arr2.append(dice)
#     set_dice_aside(answerArr, arr1, arr2, num)

# def set_dice_aside(answerArr, arr1, arr2, num):
#     for dice in answerArr:
#         i = arr1.index(int(dice))
#         arr1.pop(i)
#     calculate_score(arr1, arr2, num)

# def calculate_score(arr1, arr2, num):
#     print(enter_score)
#     round_score = int(input())
#     num += round_score
#     print(f'Score for this round is {round_score}. Total score is {num}')
#     play_again(arr1, arr2, num)

# def play_again(arr1, arr2, num):
#     print(play_again_prompt)
#     answer = str.capitalize(input())
#     print(answer)
#     if answer == "Y":
#         roll_dice(arr1, arr2, num)
#     elif answer == "QUIT":
#         handle_quit()
#     else:
#         handle_validation(answer)

# def handle_validation(str):
#     if str != "QUIT" or str != "P" or str != "B" or str != "Y" or str != "N":
#         print('Please enter an appropriate response or enter "Quit"')

# def handle_quit():
#     print(f'Ok. Hope to see you again soon')
#     exit()

# # def track_scores():

# def game_controller():
#     initialize_game()

# game_controller()
