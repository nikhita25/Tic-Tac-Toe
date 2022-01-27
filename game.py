
import pygame, sys
import numpy as np #Help create the console board
import AI_Module as AI
pygame.init()

#Constants
WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
BOARD_ROWS = 3
BOARD_COLS = 3
C_RADIUS = 60
C_WIDTH = 15
X_WIDTH = 25

#Colors
MENU_BG_COLOR = (0,0,0)
BG_COLOR = (28,170,156)
LINE_COLOR = (23,145, 135)
C_COLOR = (255,0,0)
X_COLOR = (0,0,255)
color = (0,0,0)

smallfont = pygame.font.SysFont('Corbel',35)
win = smallfont.render('You Win' , True , color)
loss = smallfont.render('You have not won' , True , color)
tie = smallfont.render('You have tied' , True , color)
player1_win = smallfont.render('Player 1 Wins' , True , color)
player2_win = smallfont.render('Player 2 Wins' , True , color)
quit1 = smallfont.render('Quit' , True , color)
single = smallfont.render('Menu' , True , color)
retry = smallfont.render('Retry' , True , color)

button = pygame.Rect(250, 250, 100, 50)
button1 = pygame.Rect(250, 350, 100, 50)
screen = None
#screen = pygame.display.set_mode((WIDTH,HEIGHT))
#pygame.display.set_caption("TIC TAC TOE")

board = np.zeros((BOARD_ROWS,BOARD_ROWS))
#setting up the board
def drawLines():
    pygame.draw.line(screen, LINE_COLOR, (0,200), (600,200), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0,400), (600,400), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (200,0), (200,600), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (400,0), (400,600), LINE_WIDTH)
#draws either X or O
def drawShapes():
    for row in range (BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, C_COLOR, (int(col * 200 + 100), int(row * 200 + 100)), C_RADIUS,C_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, X_COLOR, (col * 200 + 50, row * 200 + 200 - 50), (col * 200 + 200 - 50, row * 200 + 50), X_WIDTH)
                pygame.draw.line(screen, X_COLOR, (col * 200 + 50, row * 200 + 50), (col * 200 + 200 - 50, row * 200 + 200- 50), X_WIDTH)

#adds the player's move to the board
def markSquare(row, col, player):
    board[row][col] = player
    print(board)

#Check if there is an empty square
def availableSquare(row, col):
    return board[row][col] == 0

#Check if the board is full or not
def isFullBoard():
    for x in range(BOARD_ROWS):
        for y in range(BOARD_COLS):
            if board[x][y] == 0:
                return False
    return True

def checkWin(player):
    for col in range(BOARD_COLS):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            drawVerticalLine(col,player)
            return True
    
    for row in range(BOARD_ROWS):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            drawHorizontalLine(row,player)
            return True
    
    if board[2][0] == player and board [1][1] == player and board[0][2] == player:
        drawAscDiagonalLine(player)
        return True

    if board[0][0] == player and board [1][1] == player and board[2][2] == player:
        drawDescDiagonalLine(player)
        return True  
    
    return False

#vertical win line
def drawVerticalLine(col, player):
    posX = col * 200 + 100
    
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    
    pygame.draw.line(screen,color,(posX, 15),(posX, HEIGHT - 15), 15)

#horizontal win line
def drawHorizontalLine(row,player):
    posY = row * 200 + 100
    
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    
    pygame.draw.line(screen,color,(15, posY),(WIDTH - 15, posY), 15)

#diagonal win line
def drawAscDiagonalLine(player):
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    
    pygame.draw.line(screen,color,(15, HEIGHT - 15),(WIDTH - 15, 15), 15)

#diagonal win line
def drawDescDiagonalLine(player):
    if player == 1:
        color = C_COLOR
    elif player == 2:
        color = X_COLOR
    
    pygame.draw.line(screen,color,(15, 15),(WIDTH - 15, HEIGHT - 15), 15)

#resets the board to a fresh state
def restart():
    screen.fill(BG_COLOR)
    drawLines()
    player = 1
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            board[row][col] = 0
#playing with another person
def Multi_Player():
    screen.fill(BG_COLOR)
    drawLines()
    score = [0,0]
    player = 1
    gameOver = False
    restart_flag = 0
    while True:
        for event in pygame.event.get():
            #keeps track of the Score
            score_str = 'Player 1: ' + str(score[0]) + ' Player 2: ' + str(score[1])
            score_text = smallfont.render(score_str, True , color)
            if event.type == pygame.QUIT:
                sys.exit()
            #displays the score when the game ends
            if gameOver:
                screen.blit(score_text , (157,11))
            #shows a 2 button 'pause' menu to restart the game when clicked after the game has ended
            if event.type == pygame.MOUSEBUTTONDOWN and gameOver:
                pygame.draw.rect(screen, [255, 0, 0], button)
                pygame.draw.rect(screen, [255, 0, 0], button1)
                mouse_pos = event.pos
                screen.blit(retry , (250,250))
                screen.blit(single , (250,350))
                #button listeners, call restart on both since the board's state is constant
                if button.collidepoint(mouse_pos):
                    restart()
                    restart_flag = True
                    player = 1
                if button1.collidepoint(mouse_pos):
                    restart()
                    gameOver = False
                    player = 1
                    #reset score
                    score = [0,0]
                    return 2
            #making moves if the game has not ended
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clickedRow = int(mouseY // 200)
                clickedColumn = int(mouseX // 200)
                #makes a move based on who is the current player
                if availableSquare(clickedRow,clickedColumn):
                    if player == 1:
                        markSquare(clickedRow,clickedColumn,1)
                        if checkWin(player):
                            score[0] += 1
                            gameOver = True
                            screen.blit(player1_win , (200,200))
                        player = 2
                    elif player == 2:
                        markSquare(clickedRow,clickedColumn,2)
                        if checkWin(player):
                            gameOver = True
                            score[1] += 1
                            screen.blit(player2_win , (200,200))
                        player = 1
                drawShapes()
            #if the board is full and no one has won it is a tie
            if(isFullBoard() and not gameOver):
                gameOver = True
                screen.blit(tie , (200,200))
            if restart_flag:
                restart_flag = False
                gameOver = False
        pygame.display.update()
#replaces player 2 with an AI, same code as above except no score
def Single_Player():
    screen.fill(BG_COLOR)
    drawLines()
    player = 1
    gameOver = False
    restart_flag = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and gameOver:
                pygame.draw.rect(screen, [255, 0, 0], button)
                pygame.draw.rect(screen, [255, 0, 0], button1)
                mouse_pos = event.pos
                screen.blit(retry , (250,250))
                screen.blit(single , (250,350))
                if button.collidepoint(mouse_pos):
                    restart()
                    restart_flag = True
                    player = 1
                if button1.collidepoint(mouse_pos):
                    restart()
                    gameOver = False
                    player = 1
                    return 2
            if event.type == pygame.MOUSEBUTTONDOWN and not gameOver:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clickedRow = int(mouseY // 200)
                clickedColumn = int(mouseX // 200)

                if availableSquare(clickedRow,clickedColumn):
                    if player == 1:
                        markSquare(clickedRow,clickedColumn,1)
                        if checkWin(player):
                            gameOver = True
                            screen.blit(win , (200,200))
                        player = 2
            #AI moves here, will not make a move if [-1,-1] is returned
            if player == 2 and not gameOver:
                move = AI.AIMove(board,2)
                if(move[0] != -1):
                    markSquare(move[0],move[1],2)
                if checkWin(player):
                    gameOver = True
                    screen.blit(loss , (200,200))
                player = 1
            drawShapes()
            if(isFullBoard() and not gameOver):
                gameOver = True
                screen.blit(tie , (200,200))
            if restart_flag:
                restart_flag = False
                gameOver = False
        pygame.display.update()
#small internal menu to go back to main menu if needed and to switch game modes
def Pause_Menu(screen1,mode):
    global screen
    screen = screen1
    scene = mode
    while True:
        if scene == 0:
            scene = Single_Player()
        elif scene == 1:
            scene = Multi_Player()
        elif scene == 2:
            return -1
    
    
