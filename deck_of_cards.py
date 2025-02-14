# This program uses a dictionary as a deck of cards.

import random


def main():
    # Create a deck of cards.
    deck = create_deck()

    
    # get the number of players
    num_players = int(input('How many players are there? '))
    num_players = int(num_players + 1)

    

    # Get the number of cards to deal.
    num_cards = int(input('How many cards should I deal? '))
    print()



    # Deal the cards.
    '''
    deal_cards(deck, num_cards)
    '''
    deal_cards(deck, num_cards, num_players)
    
    
    

# The create_deck function returns a dictionary
# representing a deck of cards.
def create_deck():
    # Create a dictionary with each card and its value
    # stored as key-value pairs.
    deck = {'Ace of Spades':1, '2 of Spades':2, '3 of Spades':3,
            '4 of Spades':4, '5 of Spades':5, '6 of Spades':6,
            '7 of Spades':7, '8 of Spades':8, '9 of Spades':9,
            '10 of Spades':10, 'Jack of Spades':10,
            'Queen of Spades':10, 'King of Spades': 10,
            
            'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3,
            '4 of Hearts':4, '5 of Hearts':5, '6 of Hearts':6,
            '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9,
            '10 of Hearts':10, 'Jack of Hearts':10,
            'Queen of Hearts':10, 'King of Hearts': 10,
            
            'Ace of Clubs':1, '2 of Clubs':2, '3 of Clubs':3,
            '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6,
            '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9,
            '10 of Clubs':10, 'Jack of Clubs':10,
            'Queen of Clubs':10, 'King of Clubs': 10,
            
            'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3,
            '4 of Diamonds':4, '5 of Diamonds':5, '6 of Diamonds':6,
            '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
            '10 of Diamonds':10, 'Jack of Diamonds':10,
            'Queen of Diamonds':10, 'King of Diamonds': 10}

    # Return the deck.
    return deck



# The deal_cards function deals a specified number of cards
# from the deck.
'''     
def deal_cards(deck, num_cards):
'''
def deal_cards(deck, num_cards, num_players):

    # Initialize an accumulator for the hand value.
    '''
    hand_value = 0
    '''
    
    for num_players in range(num_players):
        hand_value = f"hand_value{num_players + 1}"
    
    
    # DATA VALIDATION
    # Make sure the number of cards to deal is not
    # greater than the number of cards in the deck (52).
    hands_delt = 0
    not_valid = True
    while not_valid:
        total_cards = num_cards * num_players
        if total_cards > 52:
            print("You can't deal more than 52 cards.")
            num_cards = int(input('How many cards should I deal? '))
            print()
        else:
            not_valid = False

    
    for player in range(num_players):
        print(f"Player {player + 1}")
        print("-" * 30)
        hand_value = 0
        for card in range(num_cards):

            random_card = random.choice(list(deck.items()))
            print(f"{random_card[0]}")
            hand_value += random_card[1]
            hands_delt += 1
            del deck[random_card[0]]
        print(f'The value of your hand is {hand_value}.')
        print()
        print('*' * 30)
        print()
        input("Press enter to continue")
        print()
        print('*' * 30)

    # Deal the cards and accumulate their values.
    '''
    for card in range(num_cards):

            random_card = random.choice(list(deck.items()))
            print(f"{random_card[0]}")
            hand_value += random_card[1]
            del deck[random_card[0]]
    

    # Display the value of the hand.
    print(f'The value of your hand is {hand_value}.')
    
    '''

# Call the main function.
main()
