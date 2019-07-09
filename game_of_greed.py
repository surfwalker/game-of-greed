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
*************************************
Play again or bank what you have?
Type 'P' to play and 'B' to bank.
(opting to bank will result in being
asked to select die you want to keep)
*************************************
"""

# ask the user which dice they would like to bank
bank_dice = """
*************************************
Which numbers would you like to bank?
*************************************
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

# dice dictionary
dice = {
    '1' : 0,
    '2' : 0,
    '3' : 0,
    '4' : 0,
    '5' : 0,
    '6' : 0,
}

# print welcome message, rules of the game and promt the user as to whether they would like to play
print(welcome, rules, play_game)