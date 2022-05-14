# Pygame
# Image - Trình bày nhân vật + nền + hoạt cảnh
# Logic - Điều khiển nhân vật

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


    def event(self):
        self.events = pygame.event.get()

        for e in self.events:
            if e.type == pygame.QUIT:
                self.loop = False

        self.player_one.event(self.events)

    def render(self):
        self.canvas.fill(self.background_screen)
        ###
        self.player_one.render()


        ###
        self.clock.tick(60)
        pygame.display.flip()

    def start(self):
        pygame.init()
        pygame.display.set_caption(self.title_screen)
        self.canvas = pygame.display.set_mode((self.width_screen,self.height_screen))
        # Init
        self.player_one = Player(1,pygame,self.canvas)
        # self.player_two = Player(2,pygame,self.canvas)

        while self.loop:
            # Handle Event
            self.event()
            # Handle Render
            self.render()
            
class Player:
    def __init__(self,player,pygame,canvas):
        self.player = player
        self.speed_y = 10
        # 
        self.x = 0
        self.y = 0
        #
        self.pygame = pygame
        self.canvas = canvas
        self.image = self.pygame.image.load("assets/paddle.png")
    
    def event(self,events):
        for e in events:

            if e.type == pygame.KEYDOWN:
                if self.player == 1:
                    if e.key == pygame.K_UP:
                        self.y -= self.speed_y

                    elif e.key == pygame.K_DOWN:
                        self.y += self.speed_y

            elif e.type == pygame.KEYUP:
                if self.player == 1:
                    if e.key == pygame.K_UP:
                        self.y = self.y

                    elif e.key == pygame.K_DOWN:
                        self.y = self.y


    def render(self):
        self.canvas.blit(self.image, (self.x,self.y))



pong = Pong()
pong.start()