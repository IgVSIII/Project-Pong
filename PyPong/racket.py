import pygame
from pygame import *
class Racket():
    def __init__(self, screen, player):

        self.screen = screen
        self.player = 'images/Player' + str(player) + '.png'
        self.moving_right = False
        self.moving_left = False
        self.racket_speed = 1
        self.image = pygame.image.load(self.player)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx


        if player == 1 :
            self.rect.bottom = self.screen_rect.bottom
            self.vector_player = 1
        elif player == 2:
            self.rect.top = self.screen_rect.top
            self.vector_player = 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def acceleration(self):
        if self.racket_speed < 6:
            self.racket_speed +=1
            
    def refresh(self):
        self.rect.centerx = self.screen_rect.centerx
            
    def stop(self):
        self.racket_speed = 1

    def update(self):
        

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.acceleration()
            self.rect.centerx +=self.racket_speed

            
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.acceleration()
            self.rect.centerx -=self.racket_speed

        if self.moving_right == False and self.moving_left == False:
            self.stop() 
        
