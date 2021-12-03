import random

def generate_deck(num_decks=6):
    deck = []

    for decks in range(num_decks):
        for suits in range(4):
            for values in range(13):
                # add the deck values to the list. 1 is Ace
                if values > 9:
                    deck.append(10)
                else:
                    deck.append(values +1)

    random.shuffle(deck)
    return deck

def score_hand(hand):
    hand_sum = sum(hand)

    if hand.count(1) and hand_sum <= 11:
        hand_sum += 10

    return hand_sum

def gameloop(deck):
    winners = []
    
    while deck:
        dealer = []
        player = []
        print(winners)

        # Break out of loop if there are less than 30 cards in the deck.
        # This is to prevent any possibility of the deck running out of cards mid round
        if len(deck) < 30:
            break
        # Deals cards in alternating player order to simulate real gameplay
        player.append(deck.pop())
        dealer.append(deck.pop())
        player.append(deck.pop())
        dealer.append(deck.pop())

        # check if player or dealer has blackjack
        if score_hand(player) == 21 and not score_hand(dealer) == 21:
            winners.append(1.5)
            continue
        if score_hand(dealer) == 21 and not score_hand(player) == 21:
            winners.append(-1)
            continue
        if score_hand(player) == 21 and score_hand(dealer) == 21:
            winners.append(0)
            continue

        # player hit/stands
        while score_hand(player) <= 21:
            print("\nYour hand: " + str(player) + " " + str(score_hand(player)))
            print("Dealer hand: " + str(dealer) + " " + str(score_hand(dealer)))
            move = input("Hit or stay?\n")
            if move == "hit":
                player.append(deck.pop())
            if move == "stay":
                break
        
        # check if player bust
        if score_hand(player) > 21:
            winners.append(-1)
            continue

        # dealer must hit if hand is <= 16
        while score_hand(dealer) <= 16:
            dealer.append(deck.pop())

        # check if dealer bust
        if score_hand(dealer) > 21:
            winners.append(1)
            continue

        if score_hand(player) < score_hand(dealer):
            winners.append(-1)
        elif score_hand(dealer) < score_hand(player):
            winners.append(1)
        else:
            winners.append(0)

    return winners

if __name__ == '__main__':
    deck = generate_deck(1)

    winners = gameloop(deck)

    print(sum(winners))