import pygame
from pygame import *
class Pong_ai():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.move_left = False
        self.move_right = False
    def ai_command(self, ball, player):
        self.move_left = False
        self.move_right = False
        if ball.speed_factory  < 0:
            if player.rect.centerx < ball.rect.centerx:
                self.move_left = True
                player.moving_right   = self.move_left
                player.moving_left = False
            
            if player.rect.centerx > ball.rect.centerx:
                self.move_right = True
                player.moving_left = self.move_right
                player.moving_right = False
            if player.rect.centerx == ball.rect.centerx:
                self.ai_deffault(player)
    def ai_deffault(self, player):
        player.moving_left = False
        player.moving_right = False
        
            
        
            
        
        
        
        
        
