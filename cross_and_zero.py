import os,sys
import pygame,time
from pygame.locals import *
import random

#variables.......................................................
FPS = 30 # frames per second, the general speed of the program
WINDOWWIDTH = 600 # size of window's width in pixels
WINDOWHEIGHT = 400 # size of windows' height in pixels
BOARD_ARRAY=[['','',''],['','',''],['','','']]
PLAYER_SYMBOL=''
COMP_SYMBOL=''
PLAYER_SCORE=0
COMP_SCORE=0
TURN_COUNT=0
#...................................................................

#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 166,   81)
BLUE     = (  57,   74, 134)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)
LG_GREEN=(0,255,0)
BLACK=(0,0,0)
#colors done..........................................................

def select_symbol():
    global PLAYER_SYMBOL
    DISPLAYSURF.fill(BLACK)
    img2=pygame.image.load("main2.png")
    DISPLAYSURF.blit(img2,(0,0))
    pygame.display.update()
    rect1=pygame.Rect(95,30,100,100)
    rect2=pygame.Rect(95,165,100,100)
    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONUP:
                mousex,mousey=event.pos
                if rect1.collidepoint(mousex,mousey):
                    PLAYER_SYMBOL='X'
                    start_game()
                elif rect2.collidepoint(mousex,mousey):
                    PLAYER_SYMBOL='0'
                    start_game()


def start_game():
    global BOARD_ARRAY
    PLAYER_SCORE=0
    COMP_SCORE=0
    DISPLAYSURF.fill(BLACK)
    img4=pygame.image.load("main3.png")
    DISPLAYSURF.blit(img4,(0,0))
    pygame.display.update()
    font=pygame.font.Font('freesansbold.ttf',40)
    text=font.render(""+str(PLAYER_SCORE),True,WHITE,BLUE)
    text2=font.render(""+str(COMP_SCORE),True,WHITE,BLUE)
    rect=text.get_rect()
    rect2=text2.get_rect()
    rect.center=(480,110)
    rect2.center=(480,300)
    DISPLAYSURF.blit(text,rect)
    DISPLAYSURF.blit(text2,rect2)
    pygame.display.update()
    TURN_COUNT=0
    while 1:
        init_board()
        print("hee",BOARD_ARRAY)
        if TURN_COUNT%2==0:
            TURN_COUNT+=1#player moves first
            while is_draw()==False:
                while 1:
                    VALID=False
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type==MOUSEMOTION:
                            mousex,mousey=event.pos
                            highlight(mousex,mousey)
                        elif event.type==MOUSEBUTTONUP:
                            mousex,mousey=event.pos
                            VALID=player_move(mousex,mousey)
                            if VALID:
                                break
                    if VALID:
                        break
                if is_winner(1,BOARD_ARRAY):
                    PLAYER_SCORE+=1
                    text.fill(BLUE)
                    text=font.render(""+str(PLAYER_SCORE),True,WHITE,BLUE)
                    rect=text.get_rect()
                    rect.center=(480,110)
                    DISPLAYSURF.blit(text,rect)
                    break
                if is_draw():
                    break
                comp_move()
                if is_winner(0,BOARD_ARRAY):
                    COMP_SCORE+=1
                    text2.fill(BLUE)
                    text2=font.render(""+str(COMP_SCORE),True,WHITE,BLUE)
                    rect2=text2.get_rect()
                    rect2.center=(480,300)
                    DISPLAYSURF.blit(text2,rect2)
                    break
                if is_draw():
                    break
        else:
            TURN_COUNT+=1
            while is_draw()==False:
                comp_move()
                if is_winner(0,BOARD_ARRAY):
                    COMP_SCORE+=1
                    text2.fill(BLUE)
                    text2=font.render(""+str(COMP_SCORE),True,WHITE,BLUE)
                    rect2=text2.get_rect()
                    rect2.center=(480,300)
                    DISPLAYSURF.blit(text2,rect2)
                    break
                if is_draw():
                    break
                while 1:
                    VALID=False
                    for event in pygame.event.get():
                        if event.type==QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type==MOUSEMOTION:
                            mousex,mousey=event.pos
                            highlight(mousex,mousey)
                        elif event.type==MOUSEBUTTONUP:
                            mousex,mousey=event.pos
                            VALID=player_move(mousex,mousey)
                            if VALID:
                                break
                    if VALID:
                        break
                if is_winner(1,BOARD_ARRAY):
                    PLAYER_SCORE+=1
                    text.fill(BLUE)
                    text=font.render(""+str(PLAYER_SCORE),True,WHITE,BLUE)
                    rect=text.get_rect()
                    rect.center=(480,110)
                    DISPLAYSURF.blit(text,rect)
                    break
                if is_draw():
                    break



def highlight(mousex,mousey):
    for i in range(0,3):
        for j in range(0,3):
            if BOARD_ARRAY[i][j]=='':
                rect=pygame.Rect(17+119*i,20+119*j,120,120)
                if rect.collidepoint(mousex,mousey):
                    pygame.draw.rect(DISPLAYSURF,LG_GREEN,(17+120*i,20+120*j,119,119))
                    pygame.display.update()
                else:
                    pygame.draw.rect(DISPLAYSURF,GREEN,(17+120*i,20+120*j,119,119))
                    pygame.display.update()


def player_move(mousex,mousey):
    global PLAYER_SYMBOL
    for i in range(0,3):
        for j in range(0,3):
            rect=pygame.Rect(17+119*i,20+119*j,120,120)
            if rect.collidepoint(mousex,mousey):
                if BOARD_ARRAY[i][j]=='':
                    BOARD_ARRAY[i][j]=1
                    if PLAYER_SYMBOL=='X':
                        pygame.draw.rect(DISPLAYSURF,GREEN,(17+120*i,20+120*j,119,119))
                        #pygame.draw.circle(DISPLAYSURF,BLACK,rect.center,20)
                        font=pygame.font.Font('freesansbold.ttf',40)
                        text=font.render("X",True,WHITE,GREEN)
                        rect1=text.get_rect()
                        rect1.center=rect.center
                        DISPLAYSURF.blit(text,rect1)
                        pygame.display.update()
                    else:
                        pygame.draw.rect(DISPLAYSURF,GREEN,(17+120*i,20+120*j,119,119))
                        #pygame.draw.circle(DISPLAYSURF,WHITE,rect.center,20)
                        font=pygame.font.Font('freesansbold.ttf',40)
                        text=font.render("O",True,WHITE,GREEN)
                        rect1=text.get_rect()
                        rect1.center=rect.center
                        DISPLAYSURF.blit(text,rect1)
                        pygame.display.update()
                    return True
    return False


def comp_move():
    global PLAYER_SYMBOL
    i,j=get_comp_move(BOARD_ARRAY)
    BOARD_ARRAY[i][j]=0
    rect=pygame.Rect(17+119*i,20+119*j,120,120)
    if PLAYER_SYMBOL=='X':
        font=pygame.font.Font('freesansbold.ttf',40)
        text=font.render("O",True,WHITE,GREEN)
        rect1=text.get_rect()
        rect1.center=rect.center
        DISPLAYSURF.blit(text,rect1)
        pygame.display.update()
    else:
        font=pygame.font.Font('freesansbold.ttf',40)
        text=font.render("X",True,WHITE,GREEN)
        rect1=text.get_rect()
        rect1.center=rect.center
        DISPLAYSURF.blit(text,rect1)
        pygame.display.update()


def get_comp_move(copy):
    filled=True
    for i in range(0,3):
        for j in range(0,3):
            if copy[i][j]=='':
                filled=False
                copy[i][j]=0
            if is_winner(0,copy):
                return (i,j)
            else:
                if filled==False:
                    copy[i][j]=''
                    filled=True

    #Check if the player could win on his next move, and block them
    filled=True
    for i in range(0,3):
        for j in range(0,3):
            if copy[i][j]=='':
                copy[i][j]=1
                filled=False
            if is_winner(1,copy):
                return (i,j)
            else:
                if filled==False:
                    copy[i][j]=''
                    filled=True


    # Try to take one of the corners, if they are free.
    copy=BOARD_ARRAY
    listt=[(0,0),(2,2),(2,0),(2,2)]
    random.shuffle(listt)
    for pt in listt:
        if copy[pt[0]][pt[1]]=='':
            return pt

    # Try to take the center, if it is free.
    copy=BOARD_ARRAY
    if copy[1][1]=='':
        return (1,1)
    #choose random move
    for i in range(0,3):
        for j in range(0,3):
            if copy[i][j]=='':
                return (i,j)


def is_winner(pl,brd):
    #diagonal check
    if  brd[0][0]==brd[1][1]==brd[2][2]==pl:
        return True
    if brd[0][2]==brd[1][1]==brd[2][0]==pl:
        return True
    #check columns
    if brd[0][0]==brd[0][1]==brd[0][2]==pl:
        return True
    if brd[1][0]==brd[1][1]==brd[1][2]==pl:
        return True
    if brd[2][0]==brd[2][1]==brd[2][2]==pl:
        return True
    #check rows
    if brd[0][0]==brd[1][0]==brd[2][0]==pl:
        return True
    if brd[0][1]==brd[1][1]==brd[2][1]==pl:
        return True
    if brd[0][2]==brd[1][2]==brd[2][2]==pl:
        return True
    return False

def is_draw():
    dr=True
    for i in range(0,3):
        for j in range(0,3):
            if BOARD_ARRAY[i][j]=='':
                dr=False
    return dr

def main():
    global FPSCLOCK,DISPLAYSURF
    #-------starting---------------------------------------------------
    pygame.init()
    FPSCLOCK=pygame.time.Clock()
    DISPLAYSURF=pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
    DISPLAYSURF.fill(BLUE)
    img=pygame.image.load("main.png")
    DISPLAYSURF.blit(img,(0,0))
    pygame.mixer.music.load('1.mp3')
    pygame.mixer.music.play(-1,0.0)
    pygame.display.update()
    pygame.display.set_caption('TIC-TAC-TOE')
    #----------window-displayed----------------------------------------
    while 1:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEBUTTONUP:
                mousex,mousey=event.pos
                select_symbol()

def init_board():
    global BOARD_ARRAY
    #pygame.draw.rect(DISPLAYSURF,GREEN,(17,20,120,120))
    BOARD_ARRAY=[['','',''],['','',''],['','','']]
    for i in range(0,3):
        for j in range(0,3):
            pygame.draw.rect(DISPLAYSURF,GREEN,(17+(120*i),20+(120*j),119,119))
    pygame.display.update()



if __name__=="__main__":
    main()