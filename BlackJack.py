import random
from cardvalues import *



class Card():

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]  #value is the value of the rank corresponds to in the rank value dict

    def __str__(self):
        return f"{self.rank} of {self.suit} : {self.value}"


class Deck():

    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
            #creating the whole deck
                self.all_cards.append(Card(suit,rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

class com():
    def __init__(self):
        self.com_hand = []
        self.card_values = []

class player():

    def __init__(self, money, name):
        self.money = money
        self.player_hand = []
        self.card_values = []

def deal_cards(user,deck, card_values , card_rank):
    new_card = deck.pop()
    user.append(new_card)
    card_values.append(new_card.value)
    card_rank.append(new_card.rank)



def display_cards(user):
    print('{[' , end = ' ')
    for item in user: 
        print(item , end = ' ')   
    print(']}')

    







class game():

    print("WELCOME TO BLACK JACK!")
    deck = Deck()
    deck.shuffle()
    Computer = com()
    player_name = input("Enter your name:")
    money = int(input("How much money do you have?"))
    Player = player(money, player_name)
    game_on = (input(f"Hello {player_name} shall we begin? (Y/N):"))
    while game_on == 'Y' and money > 0:
        print("*****************************************")
        Computer.com_hand = []
        Computer.card_values = []
        Computer.card_rank = []
        Player.player_hand = []
        Player.card_values = []
        Player.card_rank = []
        for _ in range(2):
            deal_cards(Computer.com_hand,deck.all_cards,Computer.card_values, Computer.card_rank)
        display_cards(Computer.com_hand)
        for _ in range(2):
            deal_cards(Player.player_hand, deck.all_cards, Player.card_values , Player.card_rank)
        display_cards(Player.player_hand)


        #asking to place a bet
        bet_amt = int(input("how much money do you want to bet?"))
        money = money - bet_amt
        print(f"you have {money} left")
        HS = True
        while HS == True:
            hit_stay = input("Press H for hit and S for stay:")
            if hit_stay == 'H':
                deal_cards(Player.player_hand, deck.all_cards , Player.card_values , Player.card_rank)
                display_cards(Player.player_hand)
            elif hit_stay =='S':
                HS = False
        if sum(Computer.card_values) > 21:
            print("Computer is busted , you win!")
        elif sum(Player.card_values) > 21:
            print("Computer wins! You're busted")
        else:
            print("Computer's Turn!")
            while sum(Computer.card_values) < 11:
                print("Computer drew a card. Hit!")
                deal_cards(Computer.com_hand, deck.all_cards , Computer.card_values , Computer.card_rank)
                display_cards(Computer.com_hand)
            if sum(Computer.card_values) == 21:
                print("Computer chose to stay")
                display_cards(Computer.com_hand)
            
        play_sum = sum(Player.card_values)
        if 'ace' in Player.card_rank and play_sum < 21:
            play_sum = play_sum + 10
        com_sum = sum(Computer.card_values)
        if 'ace' in Player.card_rank and com_sum < 21:
            play_sum = play_sum + 10
        if com_sum > 21:
            print("You win! Computer busted")
        elif play_sum > 21:
            print("Computer wins! You're busted")
        elif 21 - com_sum > 21 - play_sum:
            print("You win!")
        elif 21 - com_sum < 21 - play_sum:
            print("Computer wins!")
        elif com_sum == play_sum:
            print("it's a draw!")
        
        game_on = input("Play again? (Y/N)")
    else:
        print("GAME OVER")



            


        

game()


        


