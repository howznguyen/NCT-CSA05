# Pygame
# Image - Trình bày nhân vật + nền + hoạt cảnh
# Logic - Điều khiển nhân vật

import random
import pygame
import math

class Pong:

    def __init__(self):
        self.loop = True
        self.title_screen = "Pong"
        self.width_screen = 800
        self.height_screen = 600
        self.background_screen = (70,95,70)
        self.clock = pygame.time.Clock()
        self.pygame = pygame


    def event(self):
        self.events = self.pygame.event.get()

        for e in self.events:
            if e.type == pygame.QUIT:
                self.loop = False

        self.player_one.event()
        self.player_two.event()
        self.ball.event()

    def render(self):
        self.canvas.fill(self.background_screen)
        ###
        self.player_one.render()
        self.player_two.render()
        self.ball.render()

        ###
        self.clock.tick(60)
        self.pygame.display.flip()

    def start(self):
        self.pygame.init()
        self.pygame.display.set_caption(self.title_screen)
        self.canvas = self.pygame.display.set_mode((self.width_screen,self.height_screen))
        # Init
        self.player_one = Player(self,1)
        self.player_two = Player(self,2)
        self.ball = Ball(self)

        while self.loop:
            # Handle Event
            self.event()
            # Handle Render
            self.render()
            
class Player:
    def __init__(self,game,player):
        self.game = game

        self.player = player
        self.speed_y = 10

        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("assets/paddle.png")
        self.rect = self.image.get_rect()
        self.point = 0

        # 
        self.rect.x = 0
        if self.player != 1:
            self.rect.x = self.game.width_screen - self.rect.width
        self.rect.y = self.game.height_screen / 2 - self.rect.height / 2
        #
    
    def event(self):
        pressed = self.game.pygame.key.get_pressed()

        keyUp = None
        keyDown = None

        if self.player == 1:
            keyUp = pygame.K_w
            keyDown = pygame.K_s
        else:
            keyUp = pygame.K_UP
            keyDown = pygame.K_DOWN


        if pressed[keyUp]:
            if self.rect.y <= 0:
                self.rect.y = 0
            else:
                self.rect.y -= self.speed_y
        elif pressed[keyDown]:
            if self.rect.y >= self.game.height_screen - self.rect.height:
                self.rect.y = self.game.height_screen - self.rect.height
            else:
                self.rect.y += self.speed_y


    def render(self):
        self.canvas.blit(self.image, (self.rect.x,self.rect.y))

class Ball:
    def __init__(self,game):
        # game = Pong
        self.game = game

        self.speed_y = random.randint(3, 9)
        self.speed_x = random.randint(3, 9)
        
        #
        self.pygame = self.game.pygame
        self.canvas = self.game.canvas
        self.image = self.pygame.image.load("assets/ball.png")
        self.rect = self.image.get_rect()

        self.rect.x = (self.game.width_screen / 2) - (self.rect.width / 2)
        self.rect.y = random.randint((self.rect.height / 2)    ,   self.game.height_screen  - (self.rect.height / 2))

    def event(self):

        #Va chạm vào tường phải - trái
        if self.rect.x >= self.game.width_screen - self.rect.width or self.rect.x <= 0:
            self.speed_y = random.randint(3, 9)
            self.speed_x = random.randint(3, 9)

            self.rect.x = (self.game.width_screen / 2) - (self.rect.width / 2)
            self.rect.y = random.randint((self.rect.height / 2) , self.game.height_screen  - (self.rect.height / 2))
            

        if self.rect.colliderect(self.game.player_one.rect):
            self.rect.x = self.game.player_one.rect.width
            self.speed_x *= -1
        
        if self.rect.colliderect(self.game.player_two.rect):
            self.rect.x = self.game.width_screen - self.game.player_two.rect.width - self.rect.width
            self.speed_x *= -1

        # Va chạm vào tường trên - dưới
        if self.rect.y >= self.game.height_screen - self.rect.height:
            self.rect.y = self.game.height_screen - self.rect.height
            self.speed_y *= -1

        if self.rect.y <= 0:
            self.rect.y = 0
            self.speed_y *= -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        


    def render(self):
        self.canvas.blit(self.image, (self.rect.x,self.rect.y))

pong = Pong()
pong.start()