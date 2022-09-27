from string import whitespace
from time import time
import pygame
from pygame import mixer
import os

pygame.mixer.init()
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
clock = pygame.time.Clock()

black = (0,0,0)
score = 0

screen = pygame.display.set_mode((500, 800))
pygame.display.set_caption("PLAYING")

red = (139, 0, 0, 255)
yellow = (255,200,0)
font = "./fonts/Retro.ttf"

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

def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont,               textSize)
    newText=newFont.render(message, 0, textColor)

    return newText

def load(map):
    rects = []
    mixer.music.load("./Music/Skeleton.mp3")
    mixer.music.play()
    file = open(map + ".txt", 'r')
    data = file.readlines()

    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == '0':
                rects.append(pygame.Rect(keys[x].rect.centerx - 25,y * -100,68,70))
    return rects

map_rect = load("./Main/map")

while True:
    print(score)
    up_img = pygame.image.load("./image/box_up.png")
    right_img = pygame.image.load("./image/box_right.png")
    left_img = pygame.image.load("./image/box_left.png")
    bar_ = pygame.image.load("./image/box_.png")
    EZ = pygame.image.load("./image/EZ.png")
    up_img = pygame.transform.scale(up_img, (120,120))
    right_img = pygame.transform.scale(right_img, (120,120))
    left_img = pygame.transform.scale(left_img, (120,120))
    text_score = text_format("Score: {}".format(score), font, 40, yellow)
    screen.fill((255,255,255))
    red_rect = pygame.draw.rect(screen, red, pygame.Rect(0, 795,570, 40))
    Yello_rect = pygame.draw.rect(screen, yellow, pygame.Rect(0, 620,570, 170))
    for event in pygame.event.get():
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
        pygame.draw.rect(screen,(5, 5, 5, 255), rect, border_radius=20)
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
    screen.blit(up_img,(188,650))
    screen.blit(right_img,(357,650))
    screen.blit(left_img,(20,650))
    screen.blit(bar_,(0,0))
    screen.blit(text_score,(15,10))
    screen.blit(EZ,(150,-15))

    pygame.display.update()
    clock.tick(60)