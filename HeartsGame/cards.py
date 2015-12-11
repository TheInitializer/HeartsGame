import random

class Card:
    suitNames = (
        "Hearts",
        "Spades",
        "Diamonds",
        "Clubs"
    )
    rankNames = (
        "A",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K"
    )
    def __init__(self, suit, rank):
        if self.validateSuit(suit):
            self.suit = suit
        if self.validateRank(rank):
            self.rank = rank

    def validateSuit(self, suit):                  # Suit is an integer from 0 to 3
        if isinstance(suit, int): return True      # (0=hearts, 1=diamonds, 2=spades, 3=clubs)
        if suit > 3 or suit < 0: return False
        return True

    def validateRank(self, rank):
        if isinstance(rank, int): return True      # Rank is an integer from 0 to 12
        if rank > 12 or rank < 0: return False     # (0=A, 10=J, 11=Q, 12=K)
        return True

    def getSuit(self):
        return self.suitNames[self.suit]

    def getRank(self):
        return self.rankNames[self.rank]

    def getLongName(self):                   # 5 of Hearts
        return self.getRank() + " of " + self.getSuit()

    def getShortName(self):                  # 5H
        return self.getRank() + self.getSuit()[0]

class Deck:
    deck = []

    def __init__(self):
        for i in range(4):
            for j in range(13):
                self.deck.append(Card(int(i), int(j))) 
        self.shuffle()

    def shuffle(self):
        oldDeck = self.deck
        self.deck = []
        for i in range(52):
            c = random.choice(oldDeck)
            oldDeck.remove(c)
            self.deck.append(c)

    def popCard(self):
        card = self.deck[0]
        self.deck.remove(card)
        return card
