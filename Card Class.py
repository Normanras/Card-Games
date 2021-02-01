#Card Class with 3 main properties
# Class should understand: Suit, Rank, and Value (in relation to rank)

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 
          'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 
          'Queen':12, 'King':13, 'Ace':14}

