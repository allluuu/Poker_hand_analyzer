import random
import collections


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.card = self.rank, self.suit

    def __repr__(self):
        return str(self.rank) + ' of ' + self.suit


class Deck:
    def __init__(self):

        #List of all cards in whole deck
        self.available_cards = []

        #List of card that have been dealt
        self.dealt_cards = []


        #generate all types of cards in the deck
        for suit in ['Hears', 'Diamonds', 'Clubs', 'Spades']:
            for rank in range(1, 14):
                self.available_cards.append(Card(rank, suit))

    #used to check if deck contains all cards
    def get_len(self):
        return len[self.available_cards]

    #used to suffle deck, because at first it is in order
    def shuffle(self):
        return random.shuffle(self.available_cards)

    #is used to take last item of available cars and put it into dealt_cards list
    def deal_card(self):
        self.dealt_cards.append(self.available_cards.pop())

def check_straight(hand):

    suit_set = {card.suit for card in hand}
    #set is used to get ranks in order
    rank_set = {card.rank for card in hand}
    #print used to debuging and testing
    #print(rank_set)

    #is straight if difference between min and max is 4
    if (max(rank_set) - min(rank_set)) == 4 and len(suit_set) == 5:
        return True
    else:
        return False


def check_flush(hand):
    #suit_set is used to removing 'duplicates' out from list
    suit_set = {card.suit for card in hand}

    #if lenght of the set is 1 all cards are same suit
    if (len(suit_set)) == 1:
        return True
    else:
        return False


def check_straight_flush(hand):
    if check_flush(hand) and check_straight(hand):
        return True
    else:
        return False


def check_two_pairs(hand):
    rank_set = {card.rank for card in hand}

    rank_list = [card.rank for card in hand]

    card_one_count = rank_list.count(rank_list.pop())
    card_two_count = rank_list.count((rank_list.pop()))
    card_three_count = rank_list.count(rank_list.pop())

    if card_one_count == 1 and card_two_count == 1 or card_one_count == 1 and card_three_count == 1 or card_two_count == 1 and card_three_count == 1:
        return True
    else:
        return False


'''
    #Hand containts two pairs, if there are only 3 different ranks in hand
    if len(rank_set) == 3:
        return True
    else:
        return False
'''

def get_score(hand):
    score = 0
    if check_straight_flush(hand):
        score =+ 5
    elif check_flush(hand):
        score =+ 3
    elif check_straight(hand):
        score =+ 2
    elif check_two_pairs(hand):
        score =+ 1
    else:
        score = 0
    return score

def get_highest(hand):
    rank_set = {card.rank for card in hand}

    return max(rank_set)



#Create deck
deck = Deck()

#Sufle the deck
deck.shuffle()

#deal 15 cards in one list
for i in range(15):
    deck.deal_card()

#Take 5 cards each from dealt_cards list
hand1 = deck.dealt_cards[0:5]
hand2 = deck.dealt_cards[5:10]
hand3 = deck.dealt_cards[10:15]


'''
In this application player will get 'points' by having some poker hands

having two pairs will give 1 point
having straight will give 2 points
having flush will give 3 points
having straight flush give 5 points


these points are used to calculate winner of the game


print('Player one: ' + str(get_score(hand1)) + ' points')
print('Player two: ' + str(get_score(hand2)) + ' points')
print('Player tree: ' + str(get_score(hand3)) + ' points')
'''


print('Player 1 hand: ' + str(hand1))
print('Player 2 hand: ' + str(hand2))
print('Player 3 hand: ' + str(hand3))

if get_score(hand1) > get_score(hand2) and get_score(hand1) > get_score(hand3):
    if get_score(hand1) == 1:
        print('Player 1 won with two pairs')
    elif get_score(hand1) == 2:
        print('Player 1 won with straight')
    elif get_score(hand1) == 3:
        print('Player 1 won with flush')
    elif get_score(hand1) == 5:
        print('Player 1 won with straight flush')

    print(hand1)

elif get_score(hand2) > get_score(hand1) and get_score(hand2) > get_score(hand3):
    if get_score(hand2) == 1:
        print('Player 2 won with two pairs')
    elif get_score(hand2) == 2:
        print('Player 2 won with straight')
    elif get_score(hand2) == 3:
        print('Player 2 won with flush')
    elif get_score(hand2) == 5:
        print('Player 2 won with straight flush')

    print(hand2)

elif get_score(hand3) > get_score(hand1) and get_score(hand3) > get_score(hand2):
    if get_score(hand3) == 1:
        print('Player 3 won with two pairs')
    elif get_score(hand3) == 2:
        print('Player 3 won with straight')
    elif get_score(hand3) == 3:
        print('Player 3 won with flush')
    elif get_score(hand3) == 5:
        print('Player 3 won with straight flush')

    print(hand3)

elif get_score(hand1) == get_score(hand2):
    if get_highest(hand1) > get_highest(hand2):
        print('Player 1 wins with higher card')
        print(hand1)
    else:
        print('Player 2 wins with higher card')
        print(hand2)

elif get_score(hand1) == get_score(hand3):
    if get_highest(hand1) > get_highest(hand3):
        print('Player 1 wins with higher card')
        print(hand1)
    else:
        print('Player 3 wins with higher card')
        print(hand3)

elif get_score(hand2) == get_score(hand3):
    if get_highest(hand2) > get_highest(hand3):
        print('Player 2 wins with higher card')
        print(hand2)
    else:
        print('Player 3 wins with higher card')
        print(hand3)

