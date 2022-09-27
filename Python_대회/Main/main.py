from turtle import back
import pygame
from pygame.locals import *
import os

pygame.init()

# 화면을 중앙에 배치
os.environ['SDL_VIDEO_CENTERED'] = '1'

# 기본 게임 설정
W, H = 10, 20
Title = 45
screen_width=500
screen_height=800
screen=pygame.display.set_mode((screen_width, screen_height))



# Text_Font 정의
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont,               textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# 색깔들(수정)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (53, 53, 53)
gray = (127,127,127)

# 폰트 설정
font = "./fonts/Retro.ttf"


# 프레임 속도
clock = pygame.time.Clock()
FPS=30


# def play():
#     index.main()

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
                        Play.main()
                        print("play")
                     #만일 "quit"가 selected로 정의 되었는가?
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # 텍스트 색깔들
        #바탕화면

        screen.fill(black)
        # "게임의 이름" 글짜 색깔
        title=text_format("Rythm MAX", font, 100, yellow)
        #만일 "start"가 selected로 정의 되었는가?
        if selected=="start":
            # "PLAY" 텍스트를 하얀색으로
            text_start=text_format("PLAY", font, 150, white)
        else:
            # "PLAY" 텍스트를 색깔을 검정색으로
            text_start = text_format("PLAY", font, 150, gray)
            #만일 "quit"가 selected로 정의 되었는가?
        if selected=="quit":
            text_quit=text_format("QUIT", font, 150, white)
            # "quit" 텍스트 색깔을 하얀색으로
        else:
            # "quit" 텍스트 색깔을 검정색으로
            text_quit = text_format("QUIT", font, 150, gray)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # 텍스트 위치
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 400))
        pygame.display.update()
        clock.tick(FPS)
        pygame.display.set_caption("Rythm MAX")


class Button():
	def __init__(self, x, y, image, scale):
		width = image.get_width()
		height = image.get_height()
		self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self, surface):
		action = False
		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				self.clicked = True
				action = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button on screen
		surface.blit(self.image, (self.rect.x, self.rect.y))

		return action

#불러오기
main_menu()
pygame.quit()
quit()
