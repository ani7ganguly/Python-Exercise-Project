#!/usr/bin/env python
# coding: utf-8

# In[96]:


#Setting up suits and ranks of cards as tuple and values as dictionary using ranks as keys.

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11,
        'Queen':12,'King':13, 'Ace':14}


# In[97]:


#Creating CARD class to define every single card as an object of this class.

class CARD():
    def __init__(self, suits, ranks):
        
        self.suits = suits
        self.ranks = ranks
        self.values = values[ranks]
        
    def __str__(self):
        return f"{self.ranks} of {self.suits}"


# In[98]:


#Using the defined CARD class, DECK is created, method created to shuffle the deck, and another
#method created to grab the card from deck and distribute it.

class DECK:
    
    def __init__(self):
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                create_cards = CARD(suit,rank)
                self.all_cards.append (create_cards)
        
    def shuffle_deck(self):
        
        from random import shuffle
        
        shuffle(self.all_cards)
        
    def grab_card(self):
        
        return self.all_cards.pop()


# In[99]:


#Creating PLYAER Class with empty list to keep player's deck. Player will use remove method to take out
#card(s) from deck to put on the table while game is on. add-cards method will add the card to round winner's deck.

class PLAYER:
    
    def __init__(self,name):
        
        self.name = name
        self.all_cards = []
        
    def remove_one(self):
        return (self.all_cards).pop(0)
        
    def add_cards(self,new_cards):
        
        self.new_cards = new_cards
        
        if len(new_cards) > 1:
            #for list of multiple objects
            (self.all_cards).extend(new_cards) 
        else:
            #for list of single card object
            (self.all_cards).append(new_cards[0])
    
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


# In[100]:


#To check if anybody has won after a round.

def winner_check():
    
    if len(Player_1.all_cards) == 0:
        print(f'{Player_2.name} is winner')
    elif len(Player_2.all_cards) == 0:
        print(f'{Player_1.name} is winner')
    #why do I need to return it? otherwise it does not work. why?
    return len(Player_1.all_cards) == 0 or len(Player_2.all_cards) == 0


# In[101]:


#Creating players using PLAYER class

Player_1 = PLAYER('Ani')
Player_2 = PLAYER('Langto')

#Creating a new deck, shuffle, divide into two

New_Deck = DECK()

New_Deck.shuffle_deck()

x =0

for x in range(len(New_Deck.all_cards)):

    if x%2 == 0:
        card_1 = [New_Deck.grab_card()]
        Player_1.add_cards(card_1)
    else:
        card_2 = [New_Deck.grab_card()]
        Player_2.add_cards(card_2)


# In[102]:


game_on = True

#setting up loop for round

round_num = 0

while game_on:
    
    round_num += 1
    print(f"It is round {round_num}")
    
    if winner_check():
        print ("Game is over")
        game_on = False
        break

        
#Starting a new round 

    player_one_cards = []
    player_one_cards.append(Player_1.remove_one())

    player_two_cards = []
    player_two_cards.append(Player_2.remove_one())

    at_war = True
#Starting a new while loop to handle the game when it is war.
    while at_war:
        
        if player_one_cards[-1].values > player_two_cards[-1].values:
            
            Player_1.add_cards(player_one_cards)
            Player_1.add_cards(player_two_cards)
            at_war = False
                
        elif player_one_cards[-1].values < player_two_cards[-1].values:
            
            Player_2.add_cards(player_one_cards)
            Player_2.add_cards(player_two_cards)
            at_war = False

        else:
            print("it's war")
            
             #it makes sure we are not dealing with empty list while all cards are used but none has win it.           
            if len(Player_1.all_cards) < 5:
                print(f'{Player_2.name} is winner')
                game_on = False
                break
            elif len(Player_2.all_cards) < 5:
                print(f'{Player_1.name} is winner')
                game_on = False
                break

            else:
                #when it is war, it will add more cards to table
                for num in range(5):
                    player_one_cards.append(Player_1.remove_one())
                    player_two_cards.append(Player_2.remove_one())


# In[ ]:




