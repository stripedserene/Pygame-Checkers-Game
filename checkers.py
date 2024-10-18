import random, pygame, sys, time
from pygame.locals import *


SCREENWIDTH = 700
SCREENHEIGHT = 700
FPS = 30


BOARDWIDTH = 8
BOARDHEIGHT = 8


BOXWIDTH = 70
BOXHEIGHT = 70
BOXSIZE = 70
BOXMARGIN = 15.5


grid = []
for row in range(BOARDWIDTH):
    grid.append([])
    for column in range(BOARDHEIGHT):
        grid[row].append('white')




turn = "blue"


pygame.init()
screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Checkers!")
clock = pygame.time.Clock()


running = True


X = 100
Y = 100
font = pygame.font.Font(None, 75)
redWinText = font.render('GAME OVER! RED WINS', True, "red", "black")
blueWinText = font.render('GAME OVER! BLUE WINS', True, "blue", "black")
blueWinTextRect = blueWinText.get_rect()
redWinTextRect = redWinText.get_rect()
blueWinTextRect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)
redWinTextRect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 2)




#RED SATRTING PEICES
grid[0][0] = "red"
grid[0][2] = "red"
grid[0][4] = "red"
grid[0][6] = "red"


grid[1][1] = "red"
grid[1][3] = "red"
grid[1][5] = "red"
grid[1][7] = "red"


grid[2][0] = "red"
grid[2][2] = "red"
grid[2][4] = "red"
grid[2][6] = "red"




#BLUE STARTING PEICES
grid[7][1] = "blue"
grid[7][3] = "blue"
grid[7][5] = "blue"
grid[7][7] = "blue"


grid[6][0] = "blue"
grid[6][2] = "blue"
grid[6][4] = "blue"
grid[6][6] = "blue"


grid[5][1] = "blue"
grid[5][3] = "blue"
grid[5][5] = "blue"
grid[5][7] = "blue"


Left = -1000
Top = -1000


greenActive = False
canJump = False


redsLeft = True
bluesLeft = True
winner = "no one"


def clearGreens(row, column):
    for row in range(BOARDWIDTH):
        for column in range(BOARDHEIGHT):
            if grid[row][column] == "green":
                grid[row][column] = "white"
            if grid[row][column] == "yellow":
                grid[row][column] = "white"


def checkWin():
    global redsLeft
    global bluesLeft
    redsLeft = False
    bluesLeft = False
    for row in range(BOARDWIDTH):
        for column in range(BOARDHEIGHT):
            if grid[row][column] == "red" or grid[row][column] == "king red":
                redsLeft = True
            if grid[row][column] == "blue" or grid[row][column] == "king blue":
                bluesLeft = True
    if redsLeft == False or bluesLeft == False:
        displayWin()


def displayWin():
    if redsLeft == False:
        winner = "blue"
        screen.blit(blueWinText, blueWinTextRect)
        pygame.display.flip()
    if bluesLeft == False:
        winner = "red"
        screen.blit(redWinText, redWinTextRect)
        pygame.display.flip()


while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()




        elif event.type == pygame.MOUSEBUTTONDOWN:
            checkWin()
            if redsLeft == False or bluesLeft == False:
                displayWin()
                pygame.display.flip()
                continue
            pos = pygame.mouse.get_pos()
            column = int(pos[0] // (BOXSIZE + BOXMARGIN))
            row = int(pos[1] // (BOXSIZE + BOXMARGIN))
           
            # print("row: " + str(row) + " column: " + str(column))
            if row > 7 or column > 7:
                continue
            if turn == "blue":
                if grid[row][column] == "red" or grid[row][column] == "king red":
                    continue


                if grid[row][column] == "blue":


                    if greenActive == True:
                        clearGreens(row, column)
                        greenActive = False


                    boxy = row
                    boxx = column


                    Left = boxx * (BOXSIZE + BOXMARGIN) + BOXMARGIN
                    Top = boxy * (BOXSIZE + BOXMARGIN) +  BOXMARGIN
                    # pygame.draw.rect(screen, (100, 0, 100), (left - BOXMARGIN, top - BOXMARGIN, BOXSIZE + BOXMARGIN, BOXSIZE + BOXMARGIN), 4)


                    if column > 0:
                        if row > 0:
                            if grid[row - 1][column - 1] == 'white':
                                grid[row - 1][column - 1] = "green"
                            if grid[row - 1][column - 1] == 'red' or grid[row - 1][column - 1] == 'king red':
                                if column - 2 >= 0 and row - 2 >= 0:
                                    if grid[row - 2][column - 2] == 'white':
                                        grid[row - 2][column - 2] = "yellow"
                    if column < 7:
                        if row > 0:
                            if grid[row - 1][column + 1] == 'white':
                                grid[row - 1][column + 1] = "green"
                            if grid[row - 1][column + 1] == 'red' or grid[row - 1][column + 1] == 'king red':
                                if column + 2 <= 7 and row - 2 >= 0:
                                    if grid[row - 2][column + 2] == 'white':
                                        grid[row - 2][column + 2] = "yellow"
               
                if grid[row][column] == "king blue":


                    if greenActive == True:
                        clearGreens(row, column)
                        greenActive = False
                   
                    boxy = row
                    boxx = column


                    Left = boxx * (BOXSIZE + BOXMARGIN) + BOXMARGIN
                    Top = boxy * (BOXSIZE + BOXMARGIN) +  BOXMARGIN
                   
                    if column > 0:
                        if row > 0:
                            if grid[row - 1][column - 1] == 'white':
                                grid[row - 1][column - 1] = "green"
                            if grid[row - 1][column - 1] == 'red' or grid[row - 1][column - 1] == 'king red':
                                if column - 2 >= 0 and row - 2 >= 0:
                                    if grid[row - 2][column - 2] == 'white':
                                        grid[row - 2][column - 2] = "yellow"
                    if column < 7:
                        if row > 0:
                            if grid[row - 1][column + 1] == 'white':
                                grid[row - 1][column + 1] = "green"
                            if grid[row - 1][column + 1] == 'red' or grid[row - 1][column + 1] == 'king red':
                                if column + 2 <= 7 and row - 2 >= 0:
                                    if grid[row - 2][column + 2] == 'white':
                                        grid[row - 2][column + 2] = "yellow"
                    if column > 0:
                        if row < 7:
                            if grid[row + 1][column - 1] == 'white':
                                grid[row + 1][column - 1] = "green"
                            if grid[row + 1][column - 1] == 'red' or grid[row + 1][column - 1] == 'king red':
                                if column - 2 >= 0 and row + 2 <= 7:
                                    if grid[row + 2][column - 2] == 'white':
                                        grid[row + 2][column - 2] = "yellow"
                    if column < 7:
                        if row < 7:
                            if grid[row + 1][column + 1] == 'white':
                                grid[row + 1][column + 1] = "green"
                            if grid[row + 1][column + 1] == 'red' or grid[row + 1][column + 1] == 'king red':
                                if column + 2 <= 7 and row + 2 <= 7:
                                    if grid[row + 2][column + 2] == 'white':
                                        grid[row + 2][column + 2] = "yellow"


                   


                if grid[row][column] == "green" and  grid[prevrow][prevcolumn] == "blue":
                    if row == 0:
                        grid[row][column] = "king blue"
                    else:
                        grid[row][column] = "blue"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    turn = "red"


               
                if grid[row][column] == "green" and  grid[prevrow][prevcolumn] == "king blue":
                    grid[row][column] = "king blue"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    turn = "red"
               
                if grid[row][column] == "yellow" and  grid[prevrow][prevcolumn] == "king blue":
                    grid[row][column] = "king blue"
                    grid[int((prevrow + row) / 2)][int((prevcolumn + column) / 2)] = "white"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    canJump = False
                    if column > 0 and column - 1 >= 0 and row - 1 >= 0:
                        if grid[row - 1][column - 1] == 'red' or grid[row - 1][column - 1] == 'king red':
                            if column - 2 >= 0 and row - 2 >= 0:
                                if grid[row - 2][column - 2] == 'white':
                                    grid[row - 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7 and column + 1 <= 7 and row - 1 >= 0:
                        if grid[row - 1][column + 1] == 'red' or grid[row - 1][column + 1] == 'king red':
                            if column + 2 <= 7 and row - 2 >= 0:
                                if grid[row - 2][column + 2] == 'white':
                                    grid[row - 2][column + 2] = "yellow"
                                    canJump = True
                    if column > 0 and column - 1 >= 0 and row + 1 <= 7:
                        if grid[row + 1][column - 1] == 'red' or grid[row + 1][column - 1] == 'king red':
                            if column - 2 >= 0 and row + 2 <= 7:
                                if grid[row + 2][column - 2] == 'white':
                                    grid[row + 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7 and column + 1 <= 7 and row + 1 <= 7:
                        if grid[row + 1][column + 1] == 'red' or grid[row + 1][column + 1] == 'king red':
                            if column + 2 <= 7 and row + 2 <= 7:
                                if grid[row + 2][column + 2] == 'white':
                                    grid[row + 2][column + 2] = "yellow"
                                    canJump = True
                    if canJump == False:
                        turn = "red"
                    checkWin()


                if grid[row][column] == "yellow" and  grid[prevrow][prevcolumn] == "blue":
                    if row == 0:
                        grid[row][column] = "king blue"
                    else:
                        grid[row][column] = "blue"
                    grid[int((prevrow + row) / 2)][int((prevcolumn + column) / 2)] = "white"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    canJump = False
                    if column > 0:
                        if grid[row - 1][column - 1] == 'red' or grid[row - 1][column - 1] == 'king red':
                            if column - 2 >= 0 and row - 2 >= 0:
                                if grid[row - 2][column - 2] == 'white':
                                    grid[row - 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7:
                        if grid[row - 1][column + 1] == 'red' or grid[row - 1][column + 1] == 'king red':
                            if column + 2 <= 7 and row - 2 >= 0:
                                if grid[row - 2][column + 2] == 'white':
                                    grid[row - 2][column + 2] = "yellow"
                                    canJump = True
                    if canJump == False:
                        turn = "red"
                    checkWin()




            if turn == "red":
                if grid[row][column] == "blue" or grid[row][column] == "king blue":
                    continue


                if grid[row][column] == "red":


                    if greenActive == True:
                        clearGreens(row, column)
                        greenActive = False
                   
                    boxy = row
                    boxx = column


                    Left = boxx * (BOXSIZE + BOXMARGIN) + BOXMARGIN
                    Top = boxy * (BOXSIZE + BOXMARGIN) +  BOXMARGIN


                    if column > 0:
                        if row < 7:
                            if grid[row + 1][column - 1] == 'white':
                                grid[row + 1][column - 1] = "green"
                            if grid[row + 1][column - 1] == 'blue' or grid[row + 1][column - 1] == 'king blue':
                                if column - 2 >= 0 and row + 2 <= 7:
                                    if grid[row + 2][column - 2] == 'white':
                                        grid[row + 2][column - 2] = "yellow"
                    if column < 7:
                        if row < 7:
                            if grid[row + 1][column + 1] == 'white':
                                grid[row + 1][column + 1] = "green"
                            if grid[row + 1][column + 1] == 'blue' or grid[row + 1][column + 1] == 'king blue':
                                if column + 2 <= 7 and row + 2 <= 7:
                                    if grid[row + 2][column + 2] == 'white':
                                        grid[row + 2][column + 2] = "yellow"
               
                if grid[row][column] == "king red":
                    if greenActive == True:
                        clearGreens(row, column)
                        greenActive = False
                   
                    boxy = row
                    boxx = column


                    Left = boxx * (BOXSIZE + BOXMARGIN) + BOXMARGIN
                    Top = boxy * (BOXSIZE + BOXMARGIN) +  BOXMARGIN


                    if column > 0:
                        if row > 0:
                            if grid[row - 1][column - 1] == 'white':
                                grid[row - 1][column - 1] = "green"
                            if grid[row - 1][column - 1] == 'blue' or grid[row - 1][column - 1] == 'king blue':
                                if column - 2 >= 0 and row - 2 >= 0:
                                    if grid[row - 2][column - 2] == 'white':
                                        grid[row - 2][column - 2] = "yellow"
                    if column < 7:
                        if row > 0:
                            if grid[row - 1][column + 1] == 'white':
                                grid[row - 1][column + 1] = "green"
                            if grid[row - 1][column + 1] == 'blue' or grid[row - 1][column + 1] == 'king blue':
                                if column + 2 <= 7 and row - 2 >= 0:
                                    if grid[row - 2][column + 2] == 'white':
                                        grid[row - 2][column + 2] = "yellow"
                    if column > 0:
                        if row < 7:
                            if grid[row + 1][column - 1] == 'white':
                                grid[row + 1][column - 1] = "green"
                            if grid[row + 1][column - 1] == 'blue' or grid[row + 1][column - 1] == 'king blue':
                                if column - 2 >= 0 and row + 2 <= 7:
                                    if grid[row + 2][column - 2] == 'white':
                                        grid[row + 2][column - 2] = "yellow"
                    if column < 7:
                        if row < 7:
                            if grid[row + 1][column + 1] == 'white':
                                grid[row + 1][column + 1] = "green"
                            if grid[row + 1][column + 1] == 'blue' or grid[row + 1][column + 1] == 'king blue':
                                if column + 2 <= 7 and row + 2 <= 7:
                                    if grid[row + 2][column + 2] == 'white':
                                        grid[row + 2][column + 2] = "yellow"
               
                if grid[row][column] == "green" and  grid[prevrow][prevcolumn] == "red":
                    if row == 7:
                        grid[row][column] = "king red"
                    else:
                        grid[row][column] = "red"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    turn = "blue"


                if grid[row][column] == "green" and  grid[prevrow][prevcolumn] == "king red":
                    grid[row][column] = "king red"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    turn = "blue"


                if grid[row][column] == "yellow"  and  grid[prevrow][prevcolumn] == "red":
                    if row == 7:
                        grid[row][column] = "king red"
                    else:
                        grid[row][column] = "red"
                    grid[int((prevrow + row) / 2)][int((prevcolumn + column) / 2)] = "white"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    canJump = False
                    if column > 0:
                        if grid[row + 1][column - 1] == 'blue' or grid[row + 1][column - 1] == 'king blue':
                            if column - 2 >= 0 and row + 2 <= 7:
                                if grid[row + 2][column - 2] == 'white':
                                    grid[row + 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7:
                        if grid[row + 1][column + 1] == 'blue' or grid[row + 1][column + 1] == 'king blue':
                            if column + 2 <= 7 and row + 2 <= 7:
                                if grid[row + 2][column + 2] == 'white':
                                    grid[row + 2][column + 2] = "yellow"
                                    canJump = True
                    if canJump == False:
                        turn = "blue"
                    checkWin()
               
                if grid[row][column] == "yellow"  and  grid[prevrow][prevcolumn] == "king red":
                    grid[row][column] = "king red"
                    grid[int((prevrow + row) / 2)][int((prevcolumn + column) / 2)] = "white"
                    grid[prevrow][prevcolumn] = "white"
                    clearGreens(row, column)
                    canJump = False
                    if column > 0 and column - 1 >= 0 and row - 1 >= 0:
                        if grid[row - 1][column - 1] == 'blue' or grid[row - 1][column - 1] == 'king blue':
                            if column - 2 >= 0 and row - 2 >= 0:
                                if grid[row - 2][column - 2] == 'white':
                                    grid[row - 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7 and column + 1 <= 7 and row - 1 >= 0:
                        if grid[row - 1][column + 1] == 'blue' or grid[row - 1][column + 1] == 'king blue':
                            if column + 2 <= 7 and row - 2 >= 0:
                                if grid[row - 2][column + 2] == 'white':
                                    grid[row - 2][column + 2] = "yellow"
                                    canJump = True
                    if column > 0 and column - 1 >= 0 and row + 1 <= 7:
                        if grid[row + 1][column - 1] == 'blue' or grid[row + 1][column - 1] == 'king blue':
                            if column - 2 >= 0 and row + 2 <= 7:
                                if grid[row + 2][column - 2] == 'white':
                                    grid[row + 2][column - 2] = "yellow"
                                    canJump = True
                    if column < 7 and column + 1 <= 7 and row + 1 <= 7:
                        if grid[row + 1][column + 1] == 'blue' or grid[row + 1][column + 1] == 'king blue':
                            if column + 2 <= 7 and row + 2 <= 7:
                                if grid[row + 2][column + 2] == 'white':
                                    grid[row + 2][column + 2] = "yellow"
                                    canJump = True
                    if canJump == False:
                        turn = "blue"
                    checkWin()


            prevcolumn = column
            prevrow = row
            greenActive = True


#drawing the board
    for row in range(BOARDWIDTH):
        for column in range(BOARDHEIGHT):
            if grid[row][column] == 'white':
                color = (255, 255, 255)
            elif grid[row][column] == 'red':
                color = (255, 0, 0)
            elif grid[row][column] == "green":
                color = (0, 255, 0)
            elif grid[row][column] == "blue":
                color = (0, 0, 255)
            elif grid[row][column] == "yellow":
                color = "yellow"
            elif grid[row][column] == "king red":
                color = (255, 170, 0)
            elif grid[row][column] == "king blue":
                color = (0, 200, 200)
            pygame.draw.rect(screen,
                            color,
                            [(BOXMARGIN + BOXWIDTH) * column + BOXMARGIN,
                            (BOXMARGIN + BOXHEIGHT) * row + BOXMARGIN,
                            BOXWIDTH,
                            BOXHEIGHT])
    if redsLeft == False:
        screen.blit(blueWinText, blueWinTextRect)
    if bluesLeft == False:
        screen.blit(redWinText, redWinTextRect)


    if redsLeft == True and bluesLeft == True:
        pygame.draw.rect(screen, (100, 0, 100), (Left, Top, BOXSIZE, BOXSIZE), 8)
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit
