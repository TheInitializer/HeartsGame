from cards import Card, Deck
from players import AI, Player

print "Welcome to the Hearts Game."
print "Setting up..."

deck = Deck()
player = Player()
cpus = [AI("CPU 1"), AI("CPU 2"), AI("CPU 3")]    # The CPUs are each in a list, making them easier to be referred to

for i in cpus:
    deck = i.deal(deck, 52 / 4)     # Deal to CPU
deck = player.deal(deck, 52 / 4)    # Deal to player

done = False
playerOrder = [player, cpus[0], cpus[1], cpus[2]]
heartsBroken = False

while not done:             # main loop
    cardsPlayed = []
    leading = True                 # being lazy here
    print "\n--- New Trick ---\n"
    for i in playerOrder:
        if len(i.hand) == 0:
            done = True
            break
        play = i.play(leading, heartsBroken, cardsPlayed, 4)
        print play[0]
        cardsPlayed.append(play[1])
        leading = False

    if done: break

    # Decide who won the trick
    winningCard = cardsPlayed[0]
    
    for card in cardsPlayed:
        if card.suit == cardsPlayed[0].suit and card.rank > winningCard.rank:
            winningCard = card
    for player in playerOrder:
        if player.lastPlay == winningCard:
            winner = player
        

    # Give winner the points (if any)
    for card in cardsPlayed:
        if card.suit == 0:
            winner.points += 1
        if card.suit == 2 and card.rank == 11:
            winner.points += 13

    # New leader is winner
    playerOrder = playerOrder[playerOrder.index(winner):]+playerOrder[:playerOrder.index(winner)]

    print "\n--- %s won trick ---\n"%winner.name

# Compare points
winner = playerOrder[0]
for i in playerOrder:
    if i.points < winner.points:
        winner = i

print "\n### Winner: %s ###"%winner.name
