import numpy as np

f = open('data/poker.txt', 'r')

def card_number(s):
    try:
        result = int(s)
    except ValueError:
        if s == 'J':
            return 11
        elif s == 'Q':
            return 12
        elif s == 'K':
            return 13
        else:
            #s == 'A'
            return 14

def score_hand(hand):
    #Scores hand returning a number
    #0 - High card
    #1 - One pair
    #2 - Two pairs
    #3 - Three of a kind
    #4 - Straight
    #5 - Flush
    #6 - Full house
    #7 - Four of a kind
    #8 - Straight flush
    #9 - Royal flush
    
    values = [card_number(card[0]) for card in hand]
    suits = [card[1] for card in hand]
    
    ordered_values = sorted(values)
    
    if len(set(suits)) == 1:
        #Flush hands
        if ordered_values == [10, 11, 12, 13, 14]:
            return 9
        elif all([diff == 1 for diff in np.diff(ordered_values)]):
            return 8
        else:
            return 5
    elif all([diff == 1 for diff in np.diff(ordered_values)]):
        #Standard straight
        return 4
    