import cards

class AI:
    points = 0
    lastPlay = None
    hand = []

    def __init__(self, name):
        self.name = name

    def deal(self, deck, numcards):
        for i in range(numcards):
            self.hand.append(deck.popCard())
        return deck

    def play(self, leading, heartsBroken, cardsPlayed, numPlayers):
        hasOnlyHearts = True
        play = cards.Card(0, 0)
        if len(self.hand) == 0: return ["ran out of cards"]
        if leading:
            for card in self.hand:
                if card.suit != 0: 
                    hasOnlyHearts = False
                    break
            if len(self.hand) == 1 and self.hand[0].suit == 2 and self.hand[0].rank == 11:
                hasOnlyHearts = True

            if hasOnlyHearts:
                for card in self.hand:
                    if card.suit == 2 and card.rank == 11:
                        play = cards.Card(2, 11)
                        break
                if play.suit == 0:
                    play.rank = 13
                    for card in self.hand:
                        if card.rank < play.rank:
                            play = card
                            break
            else:
                for card in self.hand:
                    if card.rank > play.rank:
                        play = card
                        break
        else:
            hasSuit = False
            for card in self.hand:
                if card.suit == cardsPlayed[0].suit:
                    hasSuit = True
                    break

            if hasSuit:
                heartsOrQSPlayed = False
                for card in cardsPlayed:
                    if (card.suit == 0) or (card.suit == 2 and card.rank == 11):   # Have hearts/QS been played?
                        heartsOrQSPlayed = True
                        break
                if heartsOrQSPlayed:
                    highestCard = cardsPlayed[0]
                    for card in cardsPlayed:
                        if card.rank > highestCard.rank and card.suit == cardsPlayed[0].suit:
                            highestCard = card
                            break
                    for card in self.hand:
                        if card.rank > play.rank and card.suit == cardsPlayed[0].suit and card.rank < highestCard: #GLITCH
                            play = card
                            break
                    if play not in self.hand:
                        for card in self.hand:
                            if card.rank >= play.rank and card.suit == cardsPlayed[0].suit:
                                play = card
                                break
                else:
                    if len(cardsPlayed) == numPlayers - 1:
                        hasQS = cards.Card(2, 11) in self.hand
                        if hasQS:
                            if cardsPlayed[0].suit == 2:
                                playedHigherThanQS = False
                                for card in cardsPlayed:
                                    if card.suit == 2 and card.rank > 11:
                                        playedHigherThanQS = True
                                        break
                                if playedHigherThanQS:
                                    play = cards.Card(2, 11)
                                else:
                                    for card in self.hand:
                                        if card.rank >= play.rank and card.suit == cardsPlayed[0].suit:
                                            play = card
                                            break
                            else:
                                for card in self.hand:
                                    if card.rank >= play.rank and card.suit == cardsPlayed[0].suit:
                                        play = card
                                        break
                        else:
                            for card in self.hand:
                                if card.rank >= play.rank and card.suit == cardsPlayed[0].suit:
                                    play = card
                                    break
                    else:
                        # will implement more complex thingy later
                        for card in self.hand:
                            if card.rank >= play.rank and card.suit == cardsPlayed[0].suit:
                                play = card
                                break
            else:
                hasHearts = False
                hasQS     = False
                for card in self.hand:
                    if card.suit == 0:
                        hasHearts = True
                        break
                    elif card.suit == 2 and card.rank == 11:
                        hasQS = True
                        break
                if hasQS: play = cards.Card(2, 11)
                elif hasHearts:
                    highestHeart = cards.Card(0, 0)
                    for card in self.hand:
                        if card.suit == 0 and card.rank > highestHeart.rank:
                            highestHeart = card
                            break
                    play = highestHeart   
                else:
                    for card in self.hand:
                        if card.rank >= play.rank:
                            play = card
                            break

        self.hand.remove(play)
        self.lastPlay = play
        return (self.name + " played " + play.getLongName(), play)

class Player:
    points = 0
    lastPlay = None
    hand = []
    name = "Player"

    def deal(self, deck, numcards):
        for i in range(numcards):
            self.hand.append(deck.popCard())

    def play(self, leading, heartsBroken, cardsPlayed, numPlayers):
        # Notify player what's on the table
        print "Your turn!"
        if leading: print "You are leading."
        else:
            print "Cards played:"
            for i in cardsPlayed:
                print i.getShortName(),
            print "\nSuit led with: %s" % (cardsPlayed[0].suitNames[cardsPlayed[0].suit])
        print

        # Show the player their hand
        print "Your hand:"
        for i in self.hand:
            print i.getShortName(),
        print

        # Prompt them for their play
        done = False
        while not done:
            answer = raw_input("What do you want to play? [Format: 5H] ")

            # Validate play
            for card in self.hand:
                if answer == card.getShortName():
                    play = card
                    done = True
                    break
            if done == False:
                print "That's not a valid play - either that isn't a real card or it isn't in your hand. Try again."
                continue

        self.hand.remove(play)
        self.lastPlay = play
        return (self.name + " played " + play.getLongName(), play)