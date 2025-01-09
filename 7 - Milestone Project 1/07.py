import random

# test board
test_board = None
def intialize_board():
    return [' '] * 10
test_board = intialize_board()

#---------------------------------------------------------------------

# step1: displaying the board

def display_board(board):

    print('\n'*100)
    
    print(board[7] + '|' + board[8] + '|' + board[9])
    #print('-|-|-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    #print('-|-|-')
    print(board[1] + '|' + board[2] + '|' + board[3])

# step2:  display_board(test_board) displaying the board

#----------------------------------------------------

# taking player input as either X or O
def player_input(player):
    marker = ''
    while marker not in ['X', 'O']:
        marker = input(f"{player} , select X or O: ")
        
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 =  'X'
    return (player1, player2)

#testing
# (player1_marker, player2_marker) = player_input()
# print(player1_marker, player2_marker) 

#-----------------------------------------------------------------

# step3: Write a function that takes in the board list object, a marker ('X' or 'O'),
# and a desired position (number 1-9) and assigns it to the board. 

def place_marker(board, marker, position):
    board[position] = marker

#test
# place_marker(test_board,'X',9)
# display_board(test_board)

#---------------------------------------------------------------------

# step 4: Write a function that takes in a board and a mark (X or O) and then checks to see if that mark has won.
def win_check(board, mark):
    # row check
    ans = None
    if board[7] == mark and board[8] == mark and board[9] == mark:
       ans = True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
       ans = True
    elif board[1] == mark and board[2] == mark and board[3] == mark:
       ans = True
    # column check
    elif board[1] == mark and board[4] == mark and board[7] == mark:
       ans = True
    elif board[2] == mark and board[8] == mark and board[5] == mark:
       ans = True
    elif board[9] == mark and board[6] == mark and board[3] == mark:
       ans = True
    # diagonal check
    elif board[7] == mark and board[5] == mark and board[3] == mark:
       ans = True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
       ans = True
    else:
        ans = False
    return ans

# check
# win_check(test_board,'X')

#--------------------------------------------------------------

# Step 5: Write a function that uses the random module to randomly decide which player goes first. 
# You may want to lookup random.randint() Return a string of which player went first.


def choose_first():
    a = random.randint(1, 2)
    if(a % 2 == 0):
        return "player1"
    else:
        return "player2"

#test
# print(choose_first())

#--------------------------------------------------------------

#Step 6: Write a function that returns a boolean indicating whether a space on the board is freely available.

def space_check(board, position):
    if board[position] == " ":
        return True
    else: 
        return False
    
#test
# print(space_check(test_board, 3))

#-------------------------------------------------------------------------------------------------------------

#Step 7: Write a function that checks if the board is full and returns a boolean value. True if full, False otherwise.

def full_board_check(board):
    for i in range (1, 11):
        if board[i] == " ":
            return False
    else:
        return True
    
#test
# print(full_board_check(test_board))

#-------------------------------------------------------------------------------------------------------------

#Step 8: Write a function that asks for a player's next position (as a number 1-9) and then uses the function from step 6 to check if it's a free position. If it is, then return the position for later use.

def player_choice(player):
    pos_input = None  # Initialize pos_input to a default value
    while True:
        try:
            pos_input = int(input(f"{player} Enter a position between 1 and 9: "))
            if pos_input not in range(1, 10):
                print(f"{player}Enter a position between 1 and 9: ")
            else:
                break 
        except ValueError:
            print("Invalid input! Please enter a valid number between 1 and 9.")
    return pos_input
    #print(f"Selected position: {pos_input}")

#test
# player_choice(test_board)

#-------------------------------------------------------------------------------------------------------------

# Step 9: Write a function that asks the player if they want to play again and returns a boolean True if they do want to play again.

def replay():
    while True:
        choice = input("Do you want to play again? (Y/N): ").upper() 
        if choice == 'Y':
            return True
        elif choice == 'N':
            return False
        else:
            print("Invalid input! Please enter 'Y' for Yes or 'N' for No.")

#test
# replay()



#------------------------------------------------------------------------------------------------------------------------

#final combination

print('Welcome to Tic Tac Toe!')
again = True
while again:
    # Set the game up here
    game_on = True
    firstPlayer = choose_first()

    player1Mark = None
    player2Mark = None
    player1Turn = None
    player2Turn = None

    currPlayer = None
    currMark = None
    #determining the first player
    if(firstPlayer == "player1"):
        currPlayer = "player1"
        player1Turn = True
        (player1Mark, player2Mark) = player_input(firstPlayer)
        currMark = player1Mark
    
    else:
        currPlayer = "player2"
        player2Turn = True
        (player2Mark, player1Mark) = player_input(firstPlayer)
        currMark = player2Mark

    while game_on:
        choice = player_choice(currPlayer)
        space_available = space_check(test_board, choice)
        is_full = full_board_check(test_board)
        if(full_board_check == True):
            again = replay()
            if again:
                test_board = intialize_board()
                break
            else:
                game_on = False
                
        while(not space_available):
            print(f"space {choice} already occupied")
            choice = player_choice(currPlayer)
            space_available = space_check(test_board, choice)
        
        place_marker(test_board, currMark, choice)
        display_board(test_board)
        # print("\n"*10)
        result = win_check(test_board, currMark)
        if(result == True):
            print(f"{currPlayer} won the game")
            again = replay()
            if(again):
                test_board = intialize_board()
                break
            else:
                game_on = False

        
        player1Turn = not player1Turn
        player2Turn = not player2Turn

        if(currMark == 'X'):
            currMark = 'O'
        else:
            currMark = 'X'

        if(currPlayer == "player2"):
            currPlayer = "player1"
        else:
            currPlayer = "player2"

        
        
    # if again: 
            
        





    # if not replay():
    #     break