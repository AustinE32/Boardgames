# This program uses a dictionary as a deck of cards.

import random
import time


def main():
    # Create a deck of cards.
    dice = make_dice()

    # Get the number of players
    num_players = int(input('How many players are there? '))
    print('-----------------------------------')

    # Get the names of the players
    player_list = []
    for player in range(num_players):
        players = input(f"What is the name of Player{player + 1}? ")
        print('-----------------------------------')
        player_list.append(players)
        
    # Game start
    input("Press enter to begin the game.")
    print()
    print('*' * 30)

    # Roll the dice
    roll_dice(dice, player_list)

    

# The make_dice function returns a list representing rolling two dice
def make_dice():
    dice = {2,
            3, 3,
            4, 4, 4,
            5, 5, 5, 5,
            6, 6, 6, 6, 6,
            7, 7, 7, 7, 7, 7,
            8, 8, 8, 8, 8,
            9, 9, 9, 9,
            10, 10, 10,
            11, 11,
            12}

    # Return the dice.
    return dice


# The roll_dice function rolls the dice and displays the results.
def roll_dice(dice, player_list):
    dice_history = []
    roll_number = 0
    not_valid = True
    go = ""

    # loop to roll the dice 
    while not_valid:
        roll = random.choice(list(dice))
        roll_number += 1
        print(f'\nRoll #{roll_number}\nThe number rolled is {roll}.\n')
        print('*' * 30)

        # Add the roll to the dice history
        dice_history.append(roll)

        # Stops the rolling when a 7 is rolled for the robber
        if roll == 7:
            robber = random.choice(list(player_list))
            print(f"A seven was rolled. The chosen player is {robber}.")
            go = input("Press enter to continue")
            print('*' * 30)

        # shows the history of the dice rolled
        if go == "h":
            print(dice_history)
            go = input("Press enter to continue ")
            

        # Delay the rolling of the dice to allow for gameplay
        time.sleep(20)
        
        
    
# Call the main function.
main()
