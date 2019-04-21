import pygame, random
from pygame.sprite import Sprite
class Ball():
    def __init__(self, screen):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load("images/ball.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.centery = screen.get_rect().centery
        self.screen_rect = screen.get_rect()
        self.speed_vector = random.choice([-1,1])
        self.speed_factory = 5 * self.speed_vector
        self.speed_factorx = 0
        self.speed_factormax = 15
        

    def refresh(self):
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.centery = self.screen.get_rect().centery        
        self.speed_vector = random.choice([-1,1])
        self.speed_factory = 5 * self.speed_vector
        self.speed_factorx = 0        

    def update(self):
        self.rect.centery += self.speed_factory
        self.rect.centerx += self.speed_factorx
       
    def draw_ball(self):
       
        self.screen.blit(self.image, self.rect)

    def move_ball_side(self):
        if self.rect.left < self.screen_rect.left:
            self.speed_factorx = (-1)*self.speed_factorx
        if self.rect.right > self.screen_rect.right:
            self.speed_factorx = (-1)*self.speed_factorx

    def move_ball(self, player):
         
        self.x_vector = 1
        if player.moving_left:
            self.x_vector = -1*player.vector_player
            self.speed_factorx = 1
        if player.moving_right:
            self.x_vector = 1*player.vector_player
            self.speed_factorx = 1
            
        self.y_vector = -1
        self.speed_factorx = int((self.speed_factorx*player.racket_speed)*self.x_vector)
        self.speed_factory = int((self.speed_factory*player.racket_speed)*self.y_vector)
        if self.speed_factorx > self.speed_factormax:
            self.speed_factorx = self.speed_factormax
        if self.speed_factory > self.speed_factormax:
            self.speed_factory = self.speed_factormax
        if self.speed_factorx < -1*self.speed_factormax:
            self.speed_factorx = -1*self.speed_factormax
        if self.speed_factory < -1*self.speed_factormax:
            self.speed_factory = -1*self.speed_factormax             
        
        
        
        
        
        
        
