import os
import json
import csv
import string
import traceback
import time

# LOGS

def errorLog(tb):
    global projectName
    path = os.getcwd()
    path += '/errors'
    if os.path.isdir(path):
        path += '/{}_error_log.txt'.format(projectName)
    else:
        try:
            os.mkdir(path)
            path += '/{}_error_log.txt'.format(projectName)
        except OSError:
            print ("\nDirectory cannot be created :  %s failed\n" % path)
    try:
        os.path.isfile(path) 
        with open(path, 'r') as errorFile:
            txt = errorFile.read()
    except:
        txt = ''
    now = time.localtime()
    now = time.asctime(now)
    newError = '\n\n{}\n{}'.format(now,tb)
    txt += newError
    with open(path, 'w') as errorFile:
        errorFile.write(txt)
    print('Error Logged at : {}'.format(now))

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
    print(f" {board[7]} | {board[8]} | {board[9]} ")
    print('---|---|---')
    print(f" {board[4]} | {board[5]} | {board[6]} ")
    print('---|---|---')
    print(f" {board[1]} | {board[2]} | {board[3]} ")

def change_board(board,op):
    if p%2==0:
        board[op] = 'O'        
    else:
        board[op] = 'X'
    return board

def win_check(board):
    p1set = {'X'}
    p2set = {'O'}

    if p%2==0:
        player = 1
    else:
        player = 2

    if set(board[1:4]) == p1set or set(board[1:4]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[4:7]) == p1set or set(board[4:7]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[7:10]) == p1set or set(board[7:10]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[1:8:3]) == p1set or set(board[1:8:3]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[2:9:3]) == p1set or set(board[2:9:3]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[3:10:3]) == p1set or set(board[3:10:3]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[1:10:4]) == p1set or set(board[1:10:4]) == p2set:
        print(f'Well done Player {player} is the winner')
        time.sleep(3)
        return False
    elif set(board[3:8:2]) == p1set or set(board[3:8:2]) == p2set:
        print(f'Well done Player {player} is the winner')  
        time.sleep(3)
        return False
    for i in range(1,10):
        if board[i] in range(0,10):
            return True
    
    print('Game is a draw - no winner possible')
    time.sleep(3)
    return False
    
# VARIABLES

projectName = 'tictactoe'
p = 1


# MAIN LOOP

def game_on():
    playing = True
    while playing:
        game_ison = False
        clear()
        print('\nTIC TAC TOE GAME\n')
        print('[1] - Start game')
        print('[999] - to exit at any time')
        try:
            op = int(input('--> : '))
        except:
            print('invalid input')
        if op == 1:
            game_ison = True
            board = [0,1,2,3,4,5,6,7,8,9]
            display_game(board)
        elif op == 999:
            print('Good Bye')
            playing = False

        while game_ison:
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
                elif op in range(1,10) and board[op] not in ['X','O']:
                    board = change_board(board,op)
                    p += 1
                else:
                    print('Invalid selection')
                    time.sleep(2)
            except Exception as e:
                print('Error in  : {}'.format(e))
                tb = traceback.format_exc()
                errorLog(tb) 
            
            display_game(board)
            game_ison = win_check(board)

game_on()