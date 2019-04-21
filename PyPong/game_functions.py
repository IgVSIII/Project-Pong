import sys, pygame, socket

def check_keydown_events(event, ai_settings, screen, player1, player2):

    if event.key == pygame.K_RIGHT:
        player1.moving_right = True
    if event.key == pygame.K_LEFT:
        player1.moving_left = True
    if event.key == pygame.K_d:
        player2.moving_right = True
    if event.key == pygame.K_a:
        player2.moving_left = True        


def check_keyup_events(event, player1, player2):

    if event.key == pygame.K_RIGHT:
        player1.moving_right = False
    if event.key == pygame.K_LEFT:
        player1.moving_left = False
    if event.key == pygame.K_d:
        player2.moving_right = False
    if event.key == pygame.K_a:
        player2.moving_left = False
        
def ai_move(ai_settings, screen, player2, g_ball, ai):
    if ai_settings.ai_active == 1:
        ai.ai_command(g_ball, player2)
        

def socket_get_event(ai_settings, screen, player2, player1, sock, conn):
    event = bytes(0)
    if ai_settings.yes_online != 0 and ai_settings.server_on == True and conn is not False:
        conn.setblocking(0)
        try: data = conn.recv(16384)
        except socket.error:
            event = bytes(0)
        else:
            event = data
    if ai_settings.yes_online != 0 and ai_settings.client_on == True and sock is not False:
        sock.setblocking(0)
        try: data = sock.recv(16384)
        except socket.error:
            event = bytes(0)
        else:
            event = data           
    if event !=bytes(0):
        if event == bytes(1):
            player1.moving_right = True
        if event == bytes(2):
            player1.moving_left = True
        if event == bytes(3):
            player2.moving_right = True
        if event == bytes(4):
            player2.moving_left = True 
        if event == bytes(5):
            player1.moving_right = False
        if event == bytes(6):
            player1.moving_left = False
        if event == bytes(7):
            player2.moving_right = False
        if event == bytes(8):
            player2.moving_left = False        

        
    
    
    


def socket_push_key_events(ai_settings, event, sock, conn):
    if ai_settings.yes_online != 0 and ai_settings.server_on == True and conn is not False:
        conn.send(bytes(convert_event(event)))
    if ai_settings.yes_online != 0 and ai_settings.client_on == True and sock is not False:
        sock.send(bytes(convert_event(event)))

def convert_event(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            return 1
        elif event.key == pygame.K_LEFT:
            return 2
        elif event.key == pygame.K_d:
            return 3
        elif event.key == pygame.K_a:
            return 4
        else:
            return 0
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            return 5
        elif event.key == pygame.K_LEFT:
            return 6
        elif event.key == pygame.K_d:
            return 7
        elif event.key == pygame.K_a:
            return 8
        else:
            return 0
  
  

            

def check_events(ai_settings, screen, player1, player2, g_ball, sb, ai, sock, conn):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if ai_settings.game_active == 'game_fase':
                check_keydown_events(event, ai_settings, screen, player1, player2)
                socket_push_key_events(ai_settings, event, sock, conn)
            if event.key == pygame.K_q and ai_settings.game_active == 'fase_end':
               ai_settings.game_active = 'fase_menu'
               sb.refresh_score()
               sb.prep_score()
               player1.refresh()
               player2.refresh()
               ai_settings.ai_active = 0
               ai.ai_deffault(player2)
               close_sock(sock, conn)
            
        elif event.type == pygame.KEYUP and ai_settings.game_active == 'game_fase':
            check_keyup_events(event, player1, player2)
            socket_push_key_events(ai_settings, event, sock, conn)


    if sb.player1 == ai_settings.max_score or sb.player2 == ai_settings.max_score:
        sb.win_board()
        ai_settings.game_active = 'fase_end'
    ai_move(ai_settings, screen, player2, g_ball, ai)
    socket_get_event(ai_settings, screen, player2, player1, sock, conn)
    
                    
def update_screen(ai_settings, screen, player1, player2, g_ball, sb):
    
    if ai_settings.game_active == 'game_fase':
        player1.update()
        player2.update()
        g_ball.move_ball_side()
        g_ball.update()
        screen.fill(ai_settings.bg_color)        
        screen.blit(pygame.image.load('images/space.png'),(0,0))       
        player1.blitme()
        player2.blitme()
        sb.show_score()        
        g_ball.draw_ball()
        pygame.display.flip()
    if ai_settings.game_active == 'fase_end':
        sb.show_score()
        pygame.display.flip()


        
        


def check_collide(screen, player1, player2, g_ball):
    if g_ball.rect.colliderect(player1):
        g_ball.move_ball(player1)

    if g_ball.rect.colliderect(player2):
        g_ball.move_ball(player2)
        
def up_score(screen, player1, player2, g_ball, sb):
    if g_ball.rect.bottom > screen.get_rect().bottom:
        sb.up_score_player2()
        g_ball.refresh()
        player1.refresh()
        player2.refresh()
    if g_ball.rect.top < screen.get_rect().top:
        sb.up_score_player1()
        g_ball.refresh()
        player1.refresh()
        player2.refresh()

        
def menu_controll(ai_settings, screen, button_box):
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:            
            check_keydown_events_menu(ai_settings, screen, button_box, event)
    screen.blit(pygame.image.load('images/space.png'),(0,0))
    for i in button_box:
        i.prep_button()
        i.draw_button()
    
    pygame.display.flip()
                

    

def check_keydown_events_menu(ai_settings, screen, button_box, event):

    if event.key == pygame.K_UP and ai_settings.menu_level > 0:
        for i in button_box:
            if i.level == ai_settings.menu_level:
                i.change_status()             
            if i.level == ai_settings.menu_level - 1:
                i.change_status()
        ai_settings.menu_level -=1 
        
    if event.key == pygame.K_DOWN and ai_settings.menu_level < len(button_box):
        for i in button_box:
            if i.level == ai_settings.menu_level:
                i.change_status()
            if i.level == ai_settings.menu_level + 1:
                i.change_status()
        ai_settings.menu_level +=1 


    if event.key == pygame.K_SPACE:
        for i in button_box:
            if i.status == 'active' and i.text_button == '2 Players':
                ai_settings.game_active = 'game_fase'
            if i.status == 'active' and i.text_button == 'Exit':
                sys.exit()
            if i.status == 'active' and i.text_button == 'Create Online Game':
                ai_settings.game_active = 'game_fase'
                ai_settings.server_on = True
            if i.status == 'active' and i.text_button == 'Connect Online Game':
                ai_settings.game_active = 'game_fase'
                ai_settings.client_on = True               
            if i.status == 'active' and i.text_button == '1 Player':
                ai_settings.game_active = 'game_fase'
                ai_settings.ai_active = 1

def create_server(ai_settings):
    if ai_settings.yes_online == 0:
        serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
        serv_sock.bind(('', 53210))
        serv_sock.listen(1)
        conn, addr = serv_sock.accept()
        ai_settings.yes_online = 1
    return serv_sock , conn

        

def create_client(ai_settings):
    if ai_settings.yes_online == 0:
        client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_sock.connect(('127.0.0.1', 53210))
        ai_settings.yes_online = 2
    return client_sock

def close_sock(sock, conn):
    if sock is not False:
        sock.close()
    if conn is not False:
        conn.close()

        
    
    
