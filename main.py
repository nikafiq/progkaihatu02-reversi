import sys, pygame as pyg
from pygame.locals import *
from images import *
from PIL import Image
import time

#initalizing the game setting
WB = 'White'
winner = None
draw = False
width = 600
height = 600
black = (34, 139, 34) #actually green colored
line_color = (255,140,0)

#8x8 board setting
board = [[None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8]
#print(board)

#pygame windows setting
pyg.init()
fps = 30
CLOCK = pyg.time.Clock()
screen = pyg.display.set_mode((width, height+100), 0, 32)
pyg.display.set_caption("レバーシ")

#image load, size setting
opening = pyg.image.load('images/reversi.png')
w_img = pyg.image.load('images/white.png')
b_img = pyg.image.load('images/black.png')
w_img = pyg.transform.scale(w_img, (38, 38))
b_img = pyg.transform.scale(b_img, (38, 38))
opening = pyg.transform.scale(opening, (width, (height+100)))

def draw_status():
    global draw
    if winner is None:
        message = WB.upper() + "'s Turn"
    else:
        message = winner.upper() + " Win!"
    if draw:
        message = 'Draw!'
    font = pyg.font.Font(None, 30)
    text = font.render(message, 1, (255, 255, 255))
    screen.fill((0, 0, 0), (0, 610, 500, 80))
    text_rect = text.get_rect(center=(width/2, 700-50))
    screen.blit(text, text_rect)
    pyg.display.update()

def game_opening():
    screen.blit(opening, (0, 0))
    pyg.display.update()
    time.sleep(1)
    screen.fill(black)
    pyg.draw.line(screen, line_color, (width / 8, 0), (width / 8, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 2, 0), (width / 8 * 2, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 3, 0), (width / 8 * 3, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 4, 0), (width / 8 * 4, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 5, 0), (width / 8 * 5, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 6, 0), (width / 8 * 6, height), 7)
    pyg.draw.line(screen, line_color, (width / 8 * 7, 0), (width / 8 * 7, height), 7)

    pyg.draw.line(screen, line_color, (0, height / 8), (width, height / 8), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 2), (width, height / 8 * 2), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 3), (width, height / 8 * 3), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 4), (width, height / 8 * 4), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 5), (width, height / 8 * 5), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 6), (width, height / 8 * 6), 7)
    pyg.draw.line(screen, line_color, (0, height / 8 * 7), (width, height / 8 * 7), 7)
    draw_status()

#drawing the images on the board
def drawWB(row, col):
    global board,WB
    if row == 1:
        posx = 30
    if row == 2:
        posx = width/8 + 30
    if row == 3:
        posx = width/8*2 + 30
    if row == 4:
        posx = width/8*3 + 30
    if row == 5:
        posx = width/8*4 + 30
    if row == 6:
        posx = width/8*5 + 30
    if row == 7:
        posx = width/8*6 + 30
    if row == 8:
        posx = width/8*7 + 30

    if col == 1:
        posy = 30
    if col == 2:
        posy = (height)/3 + 30
    if col == 3:
        posy = (height)/3*2 + 30
    board[row-1][col-1] = XO
    if(WB == 'White'):
        screen.blit(w_img, (posy, posx))
        WB = 'Black'
    else:
        screen.blit(b_img, (posy, posx))
        WB = 'White'
    pyg.display.update()

def userClick():
    #get coordinates of mouse click
    x, y = pyg.mouse.get_pos()

    #get column of mouse click (1-8)
    if(x < width / 8):
        col = 1
    elif(x < width / 8 * 2):
        col = 2
    elif(x < width):
        col = 3
    else:
        col = None

    #get row of mouse click (1-8)
    if(y<height/3):
        row = 1
    elif (y<height/3*2):
        row = 2
    elif(y<height):
        row = 3
    else:
        row = None
    #print(row,col)

    if(row and col and board[row-1][col-1] is None):
        global XO

        #draw the x or o on screen
        drawWB(row, col)
        check_win()

def reset_game():
    global TTT, winner,XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_opening()
    winner=None
    board = [[None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8]

game_opening()

#game loop forever
while(True):
    for event in pyg.event.get():
        if event.type == QUIT:
            pyg.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN:
            # the user clicked; place an X or O
            userClick()
            if(winner or draw):
                reset_game()

    pyg.display.update()
    CLOCK.tick(fps)
