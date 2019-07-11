import random

card_dic = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'K':10, 'J':10, 'Q':10, 'A':'1'}

class deck:
    def __init__(self):
        card = list(card_dic.keys())
        self.deck = card + card + card + card
        random.shuffle(self.deck)
        self.pointer = 0
    def print_dec(self):
        for i in range(self.pointer,52,1):
            print(self.deck[i])
    def draw_card(self):
        self.pointer += 1
        return(self.deck[self.pointer-1])

class player:
    def __init__(self):
        self.cards = []
        # what's the minimal score assuming all Aces are 1, if min_score > 21, player is busted.
    def min_score(self):
        self.score = sum([int(card_dic[card]) for card in self.cards])
    def get_card(self,card):
        self.cards.append(card)
    def print_cards(self):
        print(self.cards)
        # what's the best score given all Aces can be used as 1 or 11 independently.
    def best_score(self):
        # number of Ace
        nAce = self.cards.count('A')
        # This is no Ace card
        if  nAce == 0:
            self.bscore = self.score
        else:
            # create a set for all possible scores by varying how many Ace cards will be used as 11
            all_scores = set([self.score + i * (11 - 1) for i in range(nAce + 1)])
            self.bscore = max([score for score in all_scores if score <= 21])

# create a deck
deck = deck()

# create 2 players, deal each two cards
p1 = player()
card = deck.draw_card()
p1.get_card(card)
card = deck.draw_card()
p1.get_card(card)
p1.min_score()
p1.print_cards()

p2 = player()
card = deck.draw_card()
p2.get_card(card)
card = deck.draw_card()
p2.get_card(card)
p2.min_score()
p2.print_cards()

keepgoing = True
while(keepgoing):

    p1_hit = input("player 1, hit or not (y/n)")
    if p1_hit == 'y':
        card = deck.draw_card()
        p1.get_card(card)
        p1.min_score()
        p1.print_cards()

    p2_hit = input("player 2, hit or not (y/n)")
    if p2_hit == 'y':
        card = deck.draw_card()
        p2.get_card(card)
        p2.min_score()
        p2.print_cards()

    keepgoing = ((p1_hit == 'y') or (p2_hit == 'y')) and ((p1.score <= 21) and (p2.score <= 21))

# game over
print('player1 cards are ')
p1.print_cards()
print('player2 cards are ')
p2.print_cards()

p1.best_score()
print('player1 best score is', p1.bscore)
p2.best_score()
print('player2 best score is', p2.bscore)

if p1.score > 21:
    print("player 1 is busted")
    if p2.score > 21:
        print("player 2 is also busted, it's a draw")
    else:
        print('player 2 won')
else:
    if p2.score > 21:
        print("player 2 is busted, player 1 won")
    else:
        if p1.bscore > p2.bscore:
            print('player 1 won')
        elif p1.bscore < p2.bscore:
            print('player 2 won')
        else:
            print("it's a draw")
