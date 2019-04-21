import pygame, sys, socket
from pygame import *
from settings import Settings
from racket import Racket
from ball import Ball
from interface import Scoreboard
from interface import Button
from pong_ai import Pong_ai
import game_functions 

def main():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.win_width, ai_settings.win_height))
    pygame.display.set_caption("PyPong_v01")
    pygame.display.set_icon(pygame.image.load("images/ball.png"))
    player1 = Racket(screen,1)
    player2 = Racket(screen,2)
    g_ball = Ball(screen)
    sb = Scoreboard(screen)
    bplay1 = Button(screen, '1 Player', 'active', 0)
    bplay2 = Button(screen, '2 Players', 'noactive', 1)
    bplayOnlineServer = Button(screen, 'Create Online Game', 'noactive', 2)
    bplayOnlineClient = Button(screen, 'Connect Online Game', 'noactive', 3)    
    bquit = Button(screen, 'Exit', 'noactive', 4)

    button_box = [bplay1,bplay2 , bquit, bplayOnlineServer, bplayOnlineClient]
    music = pygame.mixer.music.load('music/Sound.mp3')
    pygame.mixer.music.play(-1, 0.0)
    ai = Pong_ai(screen, ai_settings)
    sock = False
    conn = False
    
    while True:
        

        if ai_settings.game_active == 'fase_menu':
            game_functions.menu_controll(ai_settings, screen, button_box)
        if ai_settings.game_active == 'game_fase' or ai_settings.game_active == 'fase_end':
            if ai_settings.server_on == True and ai_settings.yes_online != 1:
                sock, conn = game_functions.create_server(ai_settings)
            if ai_settings.client_on == True and ai_settings.yes_online != 2:
                sock = game_functions.create_client(ai_settings)                
            game_functions.check_events(ai_settings,screen, player1, player2, g_ball, sb, ai, sock, conn)
            game_functions.check_collide(screen, player1, player2, g_ball)
            game_functions.up_score(screen, player1, player2, g_ball, sb)       
            game_functions.update_screen(ai_settings, screen, player1, player2, g_ball, sb)
        
        


if __name__ == "__main__":
    main()
    
    
