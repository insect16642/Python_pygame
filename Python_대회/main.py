from ast import main
import imp
from turtle import back, pos
from pygame.locals import *
import os
from string import whitespace
from time import time
import pygame
from pygame import mixer

pygame.mixer.init()
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("PLAYING")

white = (255, 255, 255)
black = (0, 0, 0)
tomato = (255, 99, 71, 255)
yellow = (255,200,0)
red = (139, 0, 0, 255)
font = "./fonts/Retro.ttf"
font_title = "./fonts/godoMaum.ttf"

class Key():
    def __init__(self,x,y,color1,color2,key):
        self.x = x
        self.y = y
        self.color1 = color1
        self.color2 = color2
        self.key = key
        self.rect = pygame.Rect(self.x,self.y,120,120)
        self.handled = False

keys = [
    Key(20,650,(3, 3, 3, 255),(3, 3, 3, 255),pygame.K_LEFT,),
    Key(188,650,(3, 3, 3, 255),(3, 3, 3, 255),pygame.K_UP),
    Key(357,650,(3, 3, 3, 255),(3, 3, 3, 255),pygame.K_RIGHT),
]

def load(map):
    rects = []
    file = open(map + ".txt", 'r')
    data = file.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,50,70))
    return rects

map_rect = load("map")

def load(rush_e):
    rects_rush_e = []
    file_rush_e = open(rush_e + ".txt", 'r')
    data_rush_e = file_rush_e.readlines()

    for y in range(len(data_rush_e)):
        for x in range(len(data_rush_e[y])):
            if data_rush_e[y][x] == '0':
                rects_rush_e.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,50,70))
    return rects_rush_e

rush_e_map = load("rush_e")

def load(midnight_train):
    rects_midnight_train= []
    file_midnight_train = open(midnight_train + ".txt", 'r')
    midnight_train = file_midnight_train.readlines()

    for y in range(len(midnight_train)):
        for x in range(len(midnight_train[y])):
            if midnight_train[y][x] == '0':
                rects_midnight_train.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,50,70))
    return rects_midnight_train

midnight_train_map = load("midnight_train")



# Text_Font ??????
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText



# ????????? ??????
clock = pygame.time.Clock()
FPS=30


def copyright_page():
    print("copyright_page")
    background = pygame.image.load("./image/box_.png")
    background = pygame.transform.scale(background,(500,800))
    CP = text_format("?????????", font_title, 60, white)
    CP_skeleton = text_format("Skeleton Dance Disney - Boomwhackers 1", font_title, 40, white)
    CP_Midnight_Train = text_format("5-X: The Midnight Train", font_title, 40, white)
    CP_Rush_E = text_format("RUSH E(Sheet Music Boss)", font_title, 40, white)
    Exit_to = text_format("EXIT To K_ESCAPE", font, 40, white)
    while True:
        screen.blit(background,(0,0))
        screen.blit(CP,(10,0))
        screen.blit(CP_skeleton, (10,50))
        screen.blit(CP_Midnight_Train, (10, 100))
        screen.blit(CP_Rush_E,(10,150))
        screen.blit(Exit_to,(10,200))

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    main_menu()

def selecter():
    selecter = 0
    while True:
        background_selecter_ = pygame.image.load("./image/box_.png")
        map_select_img = pygame.image.load("./image/map_select.png")
        select_img = pygame.image.load("./image/select.png")
        skeleton_img = pygame.image.load("./image/skeleton_pixel.png")
        Train_icon = pygame.image.load("./image/Ball_img.png")
        Fire = pygame.image.load("./image/Fire.png")
        Fire = pygame.transform.scale(Fire,(50,50))
        Train_icon = pygame.transform.scale(Train_icon,(50,50))
        map_select_img = pygame.transform.scale(map_select_img,(100,100))
        skeleton_img = pygame.transform.scale(skeleton_img,(40,40))
        background_selecter_ = pygame.transform.scale(background_selecter_,(500,
        800))
        select_img = pygame.transform.scale(select_img,(180,65))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    print("main_menu")
                    main_menu()
                if event.key == pygame.K_1:
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    selecter="Skeleton_Dance"
                if event.key == pygame.K_2:
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    selecter="Midnight Train"
                if event.key == pygame.K_3:
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    selecter = "Rush E"
                if event.key == pygame.K_RETURN:
                    if selecter == "Skeleton_Dance":
                        play_skeleton()
                    if selecter == "Midnight Train":
                        play_midnight_train()
                    if selecter == "Rush E":
                        play_rush_e()
                if event.type == pygame.QUIT:
                    pygame.quit()


        screen.blit(background_selecter_,(0,0))
        screen.blit(map_select_img,(10,10))
        screen.blit(select_img, (30,30))
        white_rect = pygame.draw.rect(screen, white, pygame.Rect(30, 160,440, 410), border_radius=5)
        black_rect = pygame.draw.rect(screen, black, pygame.Rect(50, 200,400, 43), border_radius=5)
        screen.blit(skeleton_img,(350,200))
        black_rect = pygame.draw.rect(screen, black, pygame.Rect(50, 320,400, 43), border_radius=5)
        screen.blit(Train_icon,(336, 317))
        black_rect = pygame.draw.rect(screen, black, pygame.Rect(50, 440,400, 43), border_radius=5)
        screen.blit(Fire,(336,437))

        easy_text = text_format("EASY", font, 45, black)
        middle_text = text_format("MIDDLE", font, 45, black)
        hard_text = text_format("HARD", font, 45, black)

        if selecter=="Skeleton_Dance":
            text_skeleton = text_format("Skeleton Dance", font, 45, tomato)
        else:
            text_skeleton = text_format("Skeleton Dance", font, 45, white)
        if selecter == "Midnight Train":
            text_midnight_train = text_format("Midnight Train", font, 45, tomato)
        else:
            text_midnight_train = text_format("Midnight Train", font, 45, white)
        if selecter == "Rush E":
            text_rush_e = text_format("Rush E", font, 45, tomato)
        else:
            text_rush_e = text_format("Rush E", font, 45, white)
        
        screen.blit(easy_text,(50,240))
        screen.blit(middle_text,(50,360))
        screen.blit(hard_text,(50,480))
        screen.blit(text_skeleton,(115,200))
        screen.blit(text_midnight_train,(115,320))
        screen.blit(text_rush_e, (115, 440))
        pygame.display.update()

def play_midnight_train():
    pygame.display.set_caption("Midnight Train")
    score = 0
    mixer.music.load("./Music/Midnight_Train.mp3")
    mixer.music.play()
    while True:
        if not pygame.mixer.music.get_busy():
            selecter()
        if score == 300:
            score_rank = "Excellent!"
        elif 300 > score > 250:
            score_rank = "Great!"
        elif 100 < score < 200:
            score_rank = "Good!"
        elif score < 100:
            score_rank = "Well Done"
        up_img = pygame.image.load("./image/box_up.png")
        right_img = pygame.image.load("./image/box_right.png")
        left_img = pygame.image.load("./image/box_left.png")
        box_ = pygame.image.load("./image/box_.png")
        box_ = pygame.transform.scale(box_, (500,100))
        up_img = pygame.transform.scale(up_img, (120,120))
        right_img = pygame.transform.scale(right_img, (120,120))
        left_img = pygame.transform.scale(left_img, (120,120))
        text_score = text_format("Score: {}".format(score), font, 40, white)
        screen.fill((242, 242, 242, 255))
        text_title = text_format("Midnight Train", font, 60, tomato)
        red_rect = pygame.draw.rect(screen, red, pygame.Rect(0, 799,570, 30))
        yellow_rect = pygame.draw.rect(screen, yellow, pygame.Rect(0,650,570,122))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    selecter()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        for key in keys:
            if pressed[key.key] :
                pygame.draw.rect(screen,key.color1,key.rect, border_radius=25)
                key.handled = False
            if not pressed[key.key]: 
                pygame.draw.rect(screen,key.color2,key.rect, 10, border_radius=25)
                key.handled = True
        for rects_midnight_train in midnight_train_map:
            pygame.draw.rect(screen,(5, 5, 5, 255), rects_midnight_train, border_radius=10)
            rects_midnight_train.y += 5
            for key in keys: 
                if key.rect.colliderect(rects_midnight_train) and not key.handled:
                    midnight_train_map.remove(rects_midnight_train)
                    key.handled = True
                    score += 3
                    break
                if rects_midnight_train.colliderect(red_rect):
                    midnight_train_map.remove(rects_midnight_train)
                    score -= 1
                    break
        screen.blit(box_,(0,0))
        screen.blit(up_img,(188,650))
        screen.blit(right_img,(357,650))
        screen.blit(left_img,(20,650))
        screen.blit(text_score,(15,10))
        screen.blit(text_title,(17,45))
        pygame.display.update()
        clock.tick(60)

def play_skeleton():
    pygame.display.set_caption("Skeleton Dance")
    score = 0
    mixer.music.load("./Music/Skeleton.mp3")
    mixer.music.play()
    while True:
        if not pygame.mixer.music.get_busy():
            print(score_rank)
            selecter()
        if score == 300:
            score_rank = "Excellent!"
        elif 300 > score > 250:
            score_rank = "Great!"
        elif 100 < score < 200:
            score_rank = "Good!"
        elif score < 100:
            score_rank = "Well Done"
        up_img = pygame.image.load("./image/box_up.png")
        right_img = pygame.image.load("./image/box_right.png")
        left_img = pygame.image.load("./image/box_left.png")
        box_ = pygame.image.load("./image/box_.png")
        box_ = pygame.transform.scale(box_, (500,100))
        up_img = pygame.transform.scale(up_img, (120,120))
        right_img = pygame.transform.scale(right_img, (120,120))
        left_img = pygame.transform.scale(left_img, (120,120))
        text_score = text_format("Score: {}".format(score), font, 40, white)
        screen.fill((242, 242, 242, 255))
        text_title = text_format("Skeleton Dance", font, 60, tomato)
        red_rect = pygame.draw.rect(screen, red, pygame.Rect(0, 799,570, 30))
        yellow_rect = pygame.draw.rect(screen, yellow, pygame.Rect(0,650,570,122))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    selecter()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        for key in keys:
            if pressed[key.key] :
                pygame.draw.rect(screen,key.color1,key.rect, border_radius=25)
                key.handled = False
            if not pressed[key.key]: 
                pygame.draw.rect(screen,key.color2,key.rect, 10, border_radius=25)
                key.handled = True
        for rect in map_rect:
            pygame.draw.rect(screen,(5, 5, 5, 255), rect, border_radius=10)
            rect.y += 10
            for key in keys: 
                if key.rect.colliderect(rect) and not key.handled:
                    map_rect.remove(rect)
                    key.handled = True
                    score += 3
                    break
                if rect.colliderect(red_rect):
                    map_rect.remove(rect)
                    score -= 1
                    break
        screen.blit(box_,(0,0))
        screen.blit(up_img,(188,650))
        screen.blit(right_img,(357,650))
        screen.blit(left_img,(20,650))
        screen.blit(text_score,(15,10))
        screen.blit(text_title,(17,45))
        pygame.display.update()
        clock.tick(60)

def play_rush_e():
    pygame.display.set_caption("RushE")
    score = 0
    mixer.music.load("./Music/RUSH E.mp3")
    mixer.music.play()
    while True:
        if not pygame.mixer.music.get_busy():
            print(score_rank)
            selecter()
        if score == 300:
            score_rank = "Excellent!"
        elif 300 > score > 250:
            score_rank = "Great!"
        elif 100 < score < 200:
            score_rank = "Good!"
        elif score < 100:
            score_rank = "Well Done"
        up_img = pygame.image.load("./image/box_up.png")
        right_img = pygame.image.load("./image/box_right.png")
        left_img = pygame.image.load("./image/box_left.png")
        box_ = pygame.image.load("./image/box_.png")
        box_ = pygame.transform.scale(box_, (500,100))
        up_img = pygame.transform.scale(up_img, (120,120))
        right_img = pygame.transform.scale(right_img, (120,120))
        left_img = pygame.transform.scale(left_img, (120,120))
        text_score = text_format("Score: {}".format(score), font, 40, white)
        screen.fill((242, 242, 242, 255))
        text_title = text_format("Rush E", font, 60, tomato)
        red_rect = pygame.draw.rect(screen, red, pygame.Rect(0, 799,570, 30))
        yellow_rect = pygame.draw.rect(screen, yellow, pygame.Rect(0,650,570,122))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mixer.music.stop()
                    selecter()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        pressed = pygame.key.get_pressed()
        for key in keys:
            if pressed[key.key] :
                pygame.draw.rect(screen,key.color1,key.rect, border_radius=25)
                key.handled = False
            if not pressed[key.key]: 
                pygame.draw.rect(screen,key.color2,key.rect, 10, border_radius=25)
                key.handled = True
        for rects_rush_e in rush_e_map:
            pygame.draw.rect(screen,(5, 5, 5, 255), rects_rush_e, border_radius=10)
            rects_rush_e.y += 20
            for key in keys: 
                if key.rect.colliderect(rects_rush_e) and not key.handled:
                    rush_e_map.remove(rects_rush_e)
                    key.handled = True
                    score += 3
                    break
                if rects_rush_e.colliderect(red_rect):
                    rush_e_map.remove(rects_rush_e)
                    score -= 1
                    break
        screen.blit(box_,(0,0))
        screen.blit(up_img,(188,650))
        screen.blit(right_img,(357,650))
        screen.blit(left_img,(20,650))
        screen.blit(text_score,(15,10))
        screen.blit(text_title,(17,45))
        pygame.display.update()
        clock.tick(60)
#?????? ??????
def main_menu():

    menu=True
    selected="start"

    while menu:
        Beat_X_bac = pygame.image.load("./image/BeatX.png")
        Beat_X_bac = pygame.transform.scale(Beat_X_bac, (500,800))
        copyright = pygame.image.load("./image/copyright.png").convert_alpha()
        copyright = pygame.transform.scale(copyright, (40,40)).convert_alpha()
        pos = pygame.mouse.get_pos()
        x = pos[0]
        y = pos[1]
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.MOUSEBUTTONUP:
                if (5<x<35):
                    if (762<y<793):
                        copyright_page()
            if event.type==pygame.KEYDOWN:
                # ??? ????????? ?????? ????????????
                if event.key==pygame.K_UP:
                    selected="start"
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    
                    # ????????? ????????? ?????? ????????????
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    # ?????? ?????? ????????????
                if event.key==pygame.K_RETURN:
                    # #?????? "start"??? selected??? ?????? ?????????????
                    if selected=="start":
                        print("selecter")
                        selecter()
                     #?????? "quit"??? selected??? ?????? ?????????????
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # ????????? ?????????
        #????????????

        screen.blit(Beat_X_bac,(0,0))
        copyright_text = text_format("COPYRIGHT", font_title, 38, white)
        #?????? "start"??? selected??? ?????? ?????????????
        if selected=="start":
            # "PLAY" ???????????? ???????????????
            text_start=text_format("PLAY", font, 150, tomato)
        else:
            # "PLAY" ???????????? ????????? ???????????????
            text_start = text_format("PLAY", font, 150, white)
            #?????? "quit"??? selected??? ?????? ?????????????
        if selected=="quit":
            text_quit=text_format("QUIT", font, 150, tomato)
            # "quit" ????????? ????????? ???????????????
        else:
            # "quit" ????????? ????????? ???????????????
            text_quit = text_format("QUIT", font, 150, white)

        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # ????????? ??????
        screen.blit(copyright_text, (45,758))
        screen.blit(text_start, (500/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (500/2 - (quit_rect[2]/2), 400))
        screen.blit(copyright,(0,758))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Beat_X_Main")

#????????????
main_menu()
