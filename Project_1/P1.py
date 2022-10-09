#!/usr/bin/env python
# coding: utf-8

# In[1]:


#STEP 1 = TIC TAC TOE BOARD CONSTRUCTION
from IPython.display import clear_output
test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
def display_board(test_board):
    clear_output()
    print(test_board[0]+'|'+test_board[1]+'|'+test_board[2])
    print('-|-|-')
    print(test_board[3]+'|'+test_board[4]+'|'+test_board[5])
    print('-|-|-')
    print(test_board[6]+'|'+test_board[7]+'|'+test_board[8])


# In[2]:


display_board(test_board)


# In[3]:


#STEP 2 = PLAYER INPUT TO ASSIGN MARKER 'X' OR 'O'

def player_input_marker():
    
    #marker for player 1
    marker = ' '
    
    while marker != 'X' and marker != 'O':
        marker = input("Please pick a marker 'X' or 'O': ").upper()
    
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')


# In[4]:


player_input_marker()


# In[5]:


def place_marker(board, marker, position):
    
    board[position] = marker


# In[6]:


position = place_marker(test_board,'$', 8)


# In[7]:


place_marker(test_board,'$', 8)


# In[8]:


def win_check(board,mark):
    
    return ((board[6] == mark and board[7] == mark and board[8] == mark) or # across the top
    (board[3] == mark and board[4] == mark and board[5] == mark) or # across the middle
    (board[0] == mark and board[1] == mark and board[2] == mark) or # across the bottom
    (board[6] == mark and board[3] == mark and board[0] == mark) or # down the middle
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the right side
    (board[6] == mark and board[4] == mark and board[2] == mark) or # diagonal
    (board[8] == mark and board[4] == mark and board[0] == mark)) # diagonal


# In[9]:


import random
from random import randint

def choose_first():
    
    first_player = (randint(1,2))
    
    if first_player == 1:
        return 'player_1'
    else:
        return 'player_2'


# In[10]:


def space_check(board,position):
    
    return board[position] == ' '


# In[11]:


def full_board_check(board):
    
    for i in range (0,9):
        if space_check(board,i) == True:
            return False
            
    return True


# In[12]:


def player_choice(board):
    
    position = 100
    
    choice_list = [0,1,2,3,4,5,6,7,8]
    
    while position not in choice_list or not space_check(board,position):
        position = int(input('pick a position between 0 to 8: '))
        
        if position not in choice_list:
            print ('Sorry, invalid choice')
        if board[position] != ' ':
            print(f'The position {position} is occupied. Please choose an empty position')
    
    return position


# In[13]:


def replay():
    
    choice = 'wrong'
    
    while choice not in ['Y','N']:
        choice = input("please choose 'Y' if you want to play again or 'N' if you don't: ")
        
    if choice not in ['Y','N']:
        print("Invalid choice, please choose 'Y' or 'N'")
        
    if choice == 'Y':
        return True
    elif choice == 'N':
        return False


# In[14]:


print('Welcome to TIC TAC TOE')
#WHILE loop to run the game

while True:
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']    
    player_1_marker, player_2_marker = player_input_marker()
    
    
    
    #who will go first?
    turn = choose_first()
    print(f"{turn} will go first")
    
    play_game = input('Ready to play? Y or N: ')
    
    if play_game.upper() == 'Y':
        game_on = True
    else:
        game_on = False
        
    while game_on:

        if turn == 'player_1':
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player_1_marker, position)

            if win_check(test_board,player_1_marker):
                display_board(test_board)
                print("The game is over. player_1 has won.")
                break
            else: 
                if full_board_check(test_board):
                    display_board(test_board)
                    print("It's a tie.")
                    break
                else:
                    turn = 'player_2'

        else:
            display_board(test_board)
            position = player_choice(test_board)
            place_marker(test_board, player_2_marker, position)

            if win_check(test_board,player_2_marker):
                display_board(test_board)
                print("The game is over. player_2 has won.")
                break
            else: 
                if full_board_check(test_board):
                    display_board(test_board)
                    print("It's a tie.")
                    break
                else:
                    turn = 'player_1'


    if not replay():
        break
        #Break out of the while loop on replay


# In[ ]:




