import pygame

class Scoreboard():
    def __init__(self, screen):
        self.player1 = 0
        self.player2 = 0
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_color = (230,230,230)
        self.font = pygame.font.SysFont(None, 48)
        self.font_win = pygame.font.SysFont(None, 38)
        self.prep_score()
    def prep_score(self):
        score_str = str(str(self.player1) + ' vs '+str(self.player2))
        self.image = self.font.render(score_str, True, self.text_color, (30, 30, 30))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def show_score(self):
        self.screen.blit(self.image, self.rect)
    def up_score_player1(self):
        self.player1 +=1
        self.prep_score()
    def up_score_player2(self):
        self.player2 +=1         
        self.prep_score()
    def win_board(self):
        score_str = str('The party is over ' + str(self.player1) + ' vs '+str(self.player2) + ' press Q for beginner')
        self.image = self.font_win.render(score_str, True, self.text_color, (30, 30, 30))        
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery
    def refresh_score(self):
        self.player1 = 0
        self.player2 = 0

class Button():
    def __init__(self, screen, text, status, level):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.text_button = text
        self.rect = pygame.Rect(0,0,100,30)
        self.button_color = (30, 30, 30)
        self.rect.center = self.screen_rect.center
        self.active_text = (255, 255, 255)
        self.notactive_text =(150, 150, 150)
        if status == 'active':
            self.color_text = self.active_text
        if status == 'noactive':
            self.color_text = self.notactive_text
        self.font = pygame.font.SysFont(None, 50)
        self.status = status
        self.level = level
        self.prep_button()

    def change_status(self):
        if self.status == 'active':
            self.status ='noactive'
            self.color_text = self.notactive_text
            
        elif self.status == 'noactive':
            self.status = 'active'
            self.color_text = self.active_text

            

        self.prep_button()

    def prep_button(self):
        self.image = self.font.render(self.text_button, True, self.color_text, self.button_color)
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = self.rect.centery - 220 + self.level * 50
        self.image_rect.centerx = self.rect.centerx
    def draw_button(self):
        self.screen.fill(self.button_color, self.image_rect)
        self.screen.blit(self.image, self.image_rect)
        


        
        
        

    
