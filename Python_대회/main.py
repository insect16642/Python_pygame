import pygame
from pygame.locals import *
import os

pygame.init()

# 화면을 중앙에 배치
os.environ['SDL_VIDEO_CENTERED'] = '1'

# 기본 게임 설정
screen_width=500
screen_height=800
screen=pygame.display.set_mode((screen_width, screen_height))

# Text_Font 정의
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# 색깔들(수정)
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# 폰트 설정
font = "Retro.ttf"


# 프레임 속도
clock = pygame.time.Clock()
FPS=30

#매인 메뉴
def main_menu():

    menu=True
    selected="start"

    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                # 위 화살표 키를 눌럿을떄
                if event.key==pygame.K_UP:
                    selected="start"
                    # 아랫쪽 화살표 키를 눌럿을떄
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    # 엔터 키를 눌럿을떄
                if event.key==pygame.K_RETURN:
                    # #만일 "start"가 selected로 정의 되었는가?
                    if selected=="start":
                        print("Start")
                     #만일 "quit"가 selected로 정의 되었는가?
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # 텍스트 색깔들
        #바탕화면 색깔
        screen.fill(blue)
        # "게임의 이름" 글짜 색깔
        title=text_format("Game Name", font, 100, yellow)
        #만일 "start"가 selected로 정의 되었는가?
        if selected=="start":
            # "PLAY" 텍스트를 하얀색으로
            text_start=text_format("PLAY", font, 90, white)
        else:
            # "PLAY" 텍스트를 색깔을 검정색으로
            text_start = text_format("PLAY", font, 90, black)
            #만일 "quit"가 selected로 정의 되었는가?
        if selected=="quit":
            text_quit=text_format("QUIT", font, 90, white)
            # "quit" 텍스트 색깔을 하얀색으로
        else:
            # "quit" 텍스트 색깔을 검정색으로
            text_quit = text_format("QUIT", font, 90, black)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # 텍스트 위치
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Python Game")

#불러오기
main_menu()
pygame.quit()
quit()
