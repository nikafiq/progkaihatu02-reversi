import sys, pygame as pyg
from pygame.locals import *
from images import *
from PIL import Image
import time

#initalizing the game setting
WB = 'x'
winner = None
draw = False
width = 600
height = 600
black = (105, 105, 105)
line_color = (255,140,0)

#8x8 board setting
board = [[None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8, [None]*8]
#print(board)

#pygame windows setting
pyg.init()
fps = 30
CLOCK = pyg.time.Clock()
screen = pyg.display.set_mode((width, height+100),0,32)
pyg.display.set_caption("レバーシ")

#image load, size setting
opening = pyg.image.load('images/reversi.png')
w_img = pyg.image.load('images/white.png')
b_img = pyg.image.load('images/black.png')
w_img = pyg.transform.scale(w_img, (38,38))
b_img = pyg.transform.scale(b_img, (38,38))
opening = pyg.transform.scale(opening, (width, (height+100)))

def game_opening():
    screen.blit(opening,(0,0))
    pyg.display.update()
    time.sleep(1)
    screen.fill(black)
    pyg.draw.line(screen,line_color,(width/3,0),(width/3, height),7)
    pyg.draw.line(screen,line_color,(width/3*2,0),(width/3*2, height),7)
    pyg.draw.line(screen,line_color,(0,height/3),(width, height/3),7)
    pyg.draw.line(screen,line_color,(0,height/3*2),(width, height/3*2),7)
    draw_status()

