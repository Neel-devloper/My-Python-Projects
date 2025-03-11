turn = 0

def play_game():
    import pygame
    import random
    pygame.init()
    screen = pygame.display.set_mode((500,500))
    pygame.display.set_caption('Tic Tac Toe computer')
    blue = (0,0,255)
    black = (0,0,0)
    red = (255,0,0)
    light_blue = (173,216,230)
    light_green = (144,238,144)
    
    class Boxes:
        def __init__(self,x,y,width,height,color,text):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.text = text
            self.rect = pygame.Rect(x, y, width, height)
            
        def draw(self, screen):
            pygame.draw.rect(screen, self.color, self.rect)
            if self.text:
                font = pygame.font.Font(None, 70)
                text = font.render(self.text, True, black)
                screen.blit(text, (self.x + self.width/2 - text.get_width()/2, self.y + self.height/2 - text.get_height()/2))
                

    boxes = [
        Boxes(100,100,50,50,light_green,''), # box1
        Boxes(225,100,50,50,light_green,''), # box2 
        Boxes(350,100,50,50,light_green,''), # box3
        Boxes(100,225,50,50,light_green,''), # box4
        Boxes(225,225,50,50,light_green,''), # box5
        Boxes(350,225,50,50,light_green,''), # box6
        Boxes(100,350,50,50,light_green,''), # box7
        Boxes(225,350,50,50,light_green,''), # box8
        Boxes(350,350,50,50,light_green,'')  # box9
    ]
    
    box1,box2,box3,box4,box5,box6,box7,box8,box9 = boxes
    
    global turn
    game_over = False
    winner = None

    def computer_turn():
        global turn
        nonlocal game_over
        empty_boxes = []
        for box in boxes:
            if box.text == '':
                empty_boxes.append(box)
        
        if not empty_boxes:
            game_over = True
            return
        
        winning_combinations = [
            [box1,box2,box3], [box4,box5,box6], [box7,box8,box9], 
            [box1,box4,box7], [box2,box5,box8], [box3,box6,box9], 
            [box1,box5,box9], [box3,box5,box7] 
        ]
        # win priority
        for combo in winning_combinations:
            if combo[0].text == combo[1].text == 'O' and combo[2].text == '':
                combo[2].text = 'O'
                turn += 1
                return
            elif combo[0].text == combo[2].text == 'O' and combo[1].text == '':
                combo[1].text = 'O'
                turn += 1
                return
            elif combo[1].text == combo[2].text == 'O' and combo[0].text == '':
                combo[0].text = 'O'
                turn += 1
                return

        # block priority 
        for combo in winning_combinations:
            if combo[0].text == combo[1].text == 'X' and combo[2].text == '':
                combo[2].text = 'O'
                turn += 1
                return
            elif combo[0].text == combo[2].text == 'X' and combo[1].text == '':
                combo[1].text = 'O'
                turn += 1
                return
            elif combo[1].text == combo[2].text == 'X' and combo[0].text == '':
                combo[0].text = 'O'
                turn += 1
                return
        # center priority 
        if box5.text == '':
            box5.text = 'O'
            turn += 1
            return
        # box2 priority

        if box1.text == 'X' and box9.text == 'X' or box3.text == 'X' and box7.text == 'X':
            box2.text = 'O'
            turn += 1
            return

        # defense priority
        edges = [
        [box1,box4,box7], # edge 1
        [box7,box8,box9], # edge 2
        [box3,box6,box9], # edge 3
        [box1,box2,box3], # edge 4
        [box1,box5,box9], # edge 5
        [box3,box5,box7]  # edge 6
        ]
        combo1 = [edges[0],edges[1],box7]
        combo2 = [edges[1],edges[2],box9]
        combo3 = [edges[2],edges[3],box3]       
        combo4 = [edges[3],edges[0],box1]
        combo5 = [edges[4],edges[1],box7]
        combo6 = [edges[5],edges[1],box9]
        combo7 = [edges[4],edges[2],box9]
        combo8 = [edges[5],edges[2],box3]
        combo9 = [edges[4],edges[3],box3]
        combo10 = [edges[5],edges[3],box1]
        combo11 = [edges[4],edges[0],box9]
        combo12 = [edges[5],edges[0],box3]

        if 'X' in combo1[0][0].text and 'X' in combo1[1][1].text: # box1 and box8
            if combo1[2].text == '':
                combo1[2].text = 'O'
                turn += 1
                return
        elif 'X' in combo1[0][1].text and 'X' in combo1[1][2].text: # box4 and box8
            if combo1[2].text == '':
                combo1[2].text = 'O'
                turn += 1
                return
        elif box3.text == 'X' and box8.text == 'X': # box3 and box8
            if box9.text == '':
                box9.text = 'O'
                turn += 1
                return
        elif box6.text == 'X' and box7.text == 'X': # box6 and box7
            if box9.text == '':
                box9.text = 'O'
                turn += 1
                return
        
        # attack priority 
        combinations = [
        [box1,box2,box3], # row1
        [box7,box8,box9], # row3
        [box1,box4,box7], # column1
        [box3,box6,box9], # column3
        [box1,box5,box9], # diagonal1
        [box3,box5,box7] # diagonal2
        ]
        def can_attack(list_of_boxes):
            o_count = 0
            empty_count = 0
            for box in list_of_boxes:
                if box.text == 'O':
                    o_count += 1
                elif box.text == '':
                    empty_count += 1
            if o_count == 1 and empty_count == 2:
                ctr = 1
                for box in list_of_boxes:
                    if ctr != 2:
                        if box.text == '':
                            box.text = 'O'
                            return True
                    ctr+= 1
            else:
                return False
        for i in combinations:
            if can_attack(i):
                turn += 1
                return
        # oppsite corner priority 
        if box1.text == 'X' and box9.text == '':
            box9.text = 'O'
            turn += 1
            return
        elif box9.text == 'X' and box1.text == '':
            box1.text = 'O'
            turn += 1
            return
        elif box3.text == 'X' and box7.text == '':
            box7.text = 'O'
            turn += 1
            return
        elif box7.text == 'X' and box3.text == '':
            box3.text = 'O'
            turn += 1
            return
            
        else:
        # random corner priority 
            empty_corners = []
            corners = [box1,box3,box7,box9]
            for box in corners:
                if box.text == '':
                    empty_corners.append(box)
            if empty_corners:
                random_corner = random.choice(empty_corners)
                random_corner.text = 'O'
                turn += 1
                return
            else:
        # random move priority 
                for box in boxes:
                    if box.text == '':
                        box.text = 'O'
                        turn += 1
                        return
                

    def check_win():
        nonlocal winner
        winning_combinations = [
            [box1,box2,box3], [box4,box5,box6], [box7,box8,box9], 
            [box1,box4,box7], [box2,box5,box8], [box3,box6,box9], 
            [box1,box5,box9], [box3,box5,box7] 
        ]
        for combo in winning_combinations:
            if combo[0].text == combo[1].text == combo[2].text != '':
                winner = combo[0].text
                return True

        return False
    
    def draw_board():
        screen.fill(blue)
        for box in boxes:
            box.draw(screen)
        
        if game_over:
            font = pygame.font.Font(None, 74)
            if winner:
                text = font.render(f'{winner} Wins!', True, red)
            else:
                text = font.render('Draw!', True, red)

            text_rect = text.get_rect(center=(250, 250))
            screen.blit(text, text_rect)
            
            # Draw play again button in bottom right
            play_again_button = pygame.Rect(350, 420, 120, 40)
            pygame.draw.rect(screen, light_green, play_again_button)
            font = pygame.font.Font(None, 32)
            text = font.render('Play Again', True, black)
            text_rect = text.get_rect(center=play_again_button.center)
            screen.blit(text, text_rect)
    
    running = True
    while running:
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if game_over:
                    play_again_button = pygame.Rect(350, 420, 120, 40)
                    if play_again_button.collidepoint(mouse_pos):
                        game_over = False
                        turn = 0
                        winner = None
                        for box in boxes:
                            box.text = ''
                            box.color = light_green
                        continue
                        
                if not game_over and turn % 2 == 0:
                    for box in boxes:
                        if box.rect.collidepoint(mouse_pos) and box.text == '':
                            box.text = 'X'
                            box.color = light_green
                            turn += 1
                            if not check_win() and not game_over:
                                computer_turn()
                                check_win()
                            break
                            
            if not game_over and turn % 2 == 0:
                mouse_pos = pygame.mouse.get_pos()
                for box in boxes:
                    if box.rect.collidepoint(mouse_pos) and box.text == '':
                        box.color = light_blue
                    else:
                        box.color = light_green
                        
        if check_win() or turn >= 9:
            game_over = True
            
        pygame.display.update()

play_game()
