import random
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return self.rank + " of " + self.suit
        # it is necessary to return a string here

# test
# two_hearts = Card(suits[0],ranks[2])
# print(two_hearts)
# print(two_hearts.rank)
# print(two_hearts.value)

#----------------------------------------------------------------------------------------------

class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                #creating the card object
                created_card = Card(suit, rank)
                self.all_cards.append(created_card)
    
    #just for testing purposes
    def display(self):
        for cards in self.all_cards:
            print(cards)

    def shuffle(self):
        random.shuffle(self.all_cards)
        # the thing to take into consideration over here is that the random.shuffle will not return anything,
        # instead it will just make the changes in the original list itself

    def deal_one(self):
        return self.all_cards.pop()
        
# obj = Deck()
# obj.shuffle()
# obj.display()

#----------------------------------------------------------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # this for a list of multiple card object
            self.all_cards.extend(new_cards)
        else:
            #this is for a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"player {self.name} has {len(self.all_cards)} cards"
    
# new_player = Player("Deep")
# print(new_player)

# --------------------------------------------------------------------------------------

# game logic

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

for card in player_one.all_cards:
    print (card)

print(len(player_one.all_cards))

# -----------------------------------------------------------------------------------------------------

#game on
game_on = True
# note here that the player_one_cards = cards of player1 on the floor
# and player1.all_cards = card that player 1 has a deck
round_num = 0
while game_on:
    round_num += 1
    print(f"Round {round_num}")

    if len(player_one.all_cards) == 0:
        print("player one, out of cards! player two wins")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("player two, out of cards! player one wins")
        game_on = False
        break
    #start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    # while at war loop
    at_war = True
    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("war")

            if(len(player_one.all_cards) < 3) :
                print("player one unable to declare war")
                print("player two wins")
                game_on = False
                break

            elif(len(player_one.all_cards) < 3) :
                print("player two unable to declare war")
                print("player one wins")
                game_on = False
                break
            else:
                for num in range(3):
                    player_one_cards.append(player_one.remove_one())
            