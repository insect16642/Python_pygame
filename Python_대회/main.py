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



# Text_Font 정의
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText



# 프레임 속도
clock = pygame.time.Clock()
FPS=30


def copyright_page():
    print("copyright_page")
    background = pygame.image.load("./image/box_.png")
    background = pygame.transform.scale(background,(500,800))
    CP = text_format("저작권", font_title, 60, white)
    CP_skeleton = text_format("Skeleton Dance Disney - Boomwhackers 1", font_title, 40, white)
    CP_Midnight = text_format("5-X: The Midnight Train", font_title, 40, white)

    while True:
        screen.blit(background,(0,0))
        screen.blit(CP,(10,0))
        screen.blit(CP_skeleton, (10,50))
        screen.blit(CP_Midnight, (10, 100))

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

        screen.blit(text_skeleton,(115,200))
        screen.blit(text_midnight_train,(115,320))
        screen.blit(text_rush_e, (115, 440))
        pygame.display.update()

def play_skeleton():
    pygame.display.set_caption("Skeleton Dance")
    score = 0
    mixer.music.load("./Music/Skeleton.mp3")
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
        screen.fill((255,255,255))
        print(score_rank)
        text_title = text_format("Skeleton Dance", font, 60, tomato)
        red_rect = pygame.draw.rect(screen, tomato, pygame.Rect(0, 795,570, 40))
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
            rect.y += 5
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

#매인 메뉴
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
                # 위 화살표 키를 눌럿을떄
                if event.key==pygame.K_UP:
                    selected="start"
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    
                    # 아랫쪽 화살표 키를 눌럿을떄
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    mixer.music.load("./Music/BiLing.mp3")
                    mixer.music.play()
                    # 엔터 키를 눌럿을떄
                if event.key==pygame.K_RETURN:
                    # #만일 "start"가 selected로 정의 되었는가?
                    if selected=="start":
                        print("selecter")
                        selecter()
                     #만일 "quit"가 selected로 정의 되었는가?
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # 텍스트 색깔들
        #바탕화면

        screen.blit(Beat_X_bac,(0,0))
        copyright_text = text_format("BeatX에 대한 저작권 표기", font_title, 38, white)
        #만일 "start"가 selected로 정의 되었는가?
        if selected=="start":
            # "PLAY" 텍스트를 하얀색으로
            text_start=text_format("PLAY", font, 150, tomato)
        else:
            # "PLAY" 텍스트를 색깔을 검정색으로
            text_start = text_format("PLAY", font, 150, white)
            #만일 "quit"가 selected로 정의 되었는가?
        if selected=="quit":
            text_quit=text_format("QUIT", font, 150, tomato)
            # "quit" 텍스트 색깔을 하얀색으로
        else:
            # "quit" 텍스트 색깔을 검정색으로
            text_quit = text_format("QUIT", font, 150, white)

        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # 텍스트 위치
        screen.blit(copyright_text, (45,758))
        screen.blit(text_start, (500/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (500/2 - (quit_rect[2]/2), 400))
        screen.blit(copyright,(0,758))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Beat_X_Main")

#불러오기
main_menu()
