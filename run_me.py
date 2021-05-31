import os
import time

# REMOVED ERROR LOG SYSTEM - not needed in small programme
# FUNCTIONS

def clear():
    # clear the terminal display
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

def display_game(board):
    clear()
    #Using padding methods 1 for visual display
    a = ''
    print(f"{board[7]:^3}|{board[8]:^3}|{board[9]:^3}")
    print(f'{a:-^3}|{a:-^3}|{a:-^3}')
    #Using padding methods 2 for visual display
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print('---|---|---')
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def change_board(board,op):
    #Check which player has made the selection and change that number to that players marker
    if p%2==0:
        board[op] = 'O'        
    else:
        board[op] = 'X'
    return board

def win_check(board):
    #Register the correct marker with each player
    p1set = {'X'}
    p2set = {'O'}

    if p%2==0:
        player = 1
    else:
        player = 2

    #I use a set of the board row since a set will only hold unique values
    #This means if there are 3 'X's then i will have a set of {'X'} 
    #If there are numbers OR a different marker the set would be different
    if set(board[1:4]) == p1set or set(board[1:4]) == p2set or set(board[4:7]) == p1set or set(board[4:7]) == p2set or set(board[7:10]) == p1set or set(board[7:10]) == p2set:
        #since we check the win after each turn the only win condition can come from the last player
        print(f'Well done Player {player} is the winner')
        #Pause here for drama
        time.sleep(3)
        #set game_ison loop to False so we exit to main menu
        return False
    #I split this condition check to have my sets with steps in, seperate for easier managment later
    elif set(board[1:8:3]) == p1set or set(board[1:8:3]) == p2set or set(board[2:9:3]) == p1set or set(board[2:9:3]) == p2set or set(board[3:10:3]) == p1set or set(board[3:10:3]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[1:10:4]) == p1set or set(board[1:10:4]) == p2set or set(board[3:8:2]) == p1set or set(board[3:8:2]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    for i in range(1,10):
        #By checking that there is still at least 1 number in the board list we can see if a play is still available
        if board[i] in range(0,10):
            return True
    
    #if function has not returned by this point it means there is no winner and no moves availbale hence a draw
    print('Game is a draw - no winner possible')
    time.sleep(3)
    return False
    
# VARIABLES
projectName = 'tictactoe'
p = 1

# MAIN LOOP
def game_on():
    #Enable menu loop
    playing = True
    while playing:
        #Stop game loop until ready
        game_ison = False
        clear()
        print('\nTIC TAC TOE GAME\n')
        print('[1] - Start game')
        print('[999] - to exit at any time')
        try:
            #Only int can be entered or the menu will fail and repeat
            op = int(input('--> : '))
        except:
            print('invalid input')
            time.sleep(2)

        # I prefer the exit option to be covered first in the logic
        if op == 999:
            print('Good Bye')
            #Force end to menu loop (main exit)
            playing = False
        elif op == 1:
            # Enable Game loop
            game_ison = True
            #Establish all board squars in a list
            board = [0,1,2,3,4,5,6,7,8,9]
            display_game(board)
        
        #Game_ison is set to true in option 1 above
        while game_ison:
            # p is for player (even or odd)(1 or 2) I set this to global so I dont need to pass it each time
            global p
            if p%2==0:
                print('\nPlayer 2 please select your move')
            else:
                print('\nPlayer 1 please select your move')
            try:
                op = int(input('--> : '))
                if op == 999:
                    game_ison = False
                    print('Game Over')
                # here we check the number is valid selection and has not already been marked
                elif op in range(1,10) and board[op] not in ['X','O']:
                    board = change_board(board,op)
                    p += 1
                    # after changes display the new board
                    display_game(board)
                    # check for win conditions after the last play was made
                    game_ison = win_check(board)
                else:
                    print('Invalid selection')
                    # I added a pause here so the error message can be read before being cleared from screen
                    time.sleep(2)
                    # Clear screen as not to flood with errors
                    display_game(board)
            except:
                print('{} is not a valid number'.format(op))
                #Removed error loggin to file
                # I added a pause here so the error message can be read before being cleared from screen
                time.sleep(2)
                # Clear screen as not to flood with errors
                display_game(board)

# Start main loop
game_on()
