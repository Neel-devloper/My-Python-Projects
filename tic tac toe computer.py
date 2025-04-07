turn = 0

def play_game():
    import pygame
    import random
    pygame.init()
    screen_height = 500
    screen_width = 500
    screen = pygame.display.set_mode((screen_height, screen_width))
    pygame.display.set_caption('Tic Tac Toe Computer')
    
    # Define colors
    white = (255, 255, 255)         # New background color
    black = (0, 0, 0)               # Text color
    red = (255, 0, 0)              # Win/draw message color
    light_gray = (211, 211, 211)    # Default box color
    light_blue = (173, 216, 230)    # Hover color
    yellow = (255, 255, 0)          # Winning boxes highlight color
    
    class Boxes:
        def __init__(self, x, y, width, height, color, text):
            self.x = x
            self.y = y
            self.width = width
            self.height = height
            self.color = color
            self.text = text
            self.rect = pygame.Rect(x, y, width, height)
    
    # Initialize boxes with larger size (150x150) and adjacent positions
    boxes = [
        Boxes(25, 25, 150, 150, light_gray, ''),    # box1
        Boxes(175, 25, 150, 150, light_gray, ''),   # box2
        Boxes(325, 25, 150, 150, light_gray, ''),   # box3
        Boxes(25, 175, 150, 150, light_gray, ''),   # box4
        Boxes(175, 175, 150, 150, light_gray, ''),  # box5
        Boxes(325, 175, 150, 150, light_gray, ''),  # box6
        Boxes(25, 325, 150, 150, light_gray, ''),   # box7
        Boxes(175, 325, 150, 150, light_gray, ''),  # box8
        Boxes(325, 325, 150, 150, light_gray, '')   # box9
    ]
    
    box1, box2, box3, box4, box5, box6, box7, box8, box9 = boxes
    
    global turn
    game_over = False
    winner = None
    winning_boxes = None  # To store the winning combination
    
    def computer_turn():
        global turn
        nonlocal game_over
        empty_boxes = [box for box in boxes if box.text == '']
        
        if not empty_boxes:
            game_over = True
            return
        
        winning_combinations = [
            [box1, box2, box3], [box4, box5, box6], [box7, box8, box9],
            [box1, box4, box7], [box2, box5, box8], [box3, box6, box9],
            [box1, box5, box9], [box3, box5, box7]
        ]
        # Win priority
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
            
        # box8 and box6 priority
        if box8.text == 'X' and box6.text == 'X' and box3.text == '':
            box3.text = 'O'
            turn += 1
            return
        
        # Block priority
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
        

        # Center priority
        if box5.text == '':
            box5.text = 'O'
            turn += 1
            return
        

        # Box2 priority
        if box1.text == 'X' and box9.text == 'X' or box3.text == 'X' and box7.text == 'X':
            box2.text = 'O'
            turn += 1
            return
        # Defense priority
        edges = [
            [box1, box4, box7], [box7, box8, box9], [box3, box6, box9],
            [box1, box2, box3], [box1, box5, box9], [box3, box5, box7]
        ]
        combo1 = [edges[0], edges[1], box7]
        combo2 = [edges[1], edges[2], box9]
        combo3 = [edges[2], edges[3], box3]
        combo4 = [edges[3], edges[0], box1]
        combo5 = [edges[4], edges[1], box7]
        combo6 = [edges[5], edges[1], box9]
        combo7 = [edges[4], edges[2], box9]
        combo8 = [edges[5], edges[2], box3]
        combo9 = [edges[4], edges[3], box3]
        combo10 = [edges[5], edges[3], box1]
        combo11 = [edges[4], edges[0], box9]
        combo12 = [edges[5], edges[0], box3]
        
        if 'X' in combo1[0][0].text and 'X' in combo1[1][1].text:
            if combo1[2].text == '':
                combo1[2].text = 'O'
                turn += 1
                return
        elif 'X' in combo1[0][1].text and 'X' in combo1[1][2].text:
            if combo1[2].text == '':
                combo1[2].text = 'O'
                turn += 1
                return
        elif box3.text == 'X' and box8.text == 'X':
            if box9.text == '':
                box9.text = 'O'
                turn += 1
                return
        elif box6.text == 'X' and box7.text == 'X':
            if box9.text == '':
                box9.text = 'O'
                turn += 1
                return
        # Attack priority
        combinations = [
            [box1, box2, box3], [box7, box8, box9], [box1, box4, box7],
            [box3, box6, box9], [box1, box5, box9], [box3, box5, box7]
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
                    ctr += 1
            else:
                return False
        for i in combinations:
            if can_attack(i):
                turn += 1
                return
        # Opposite corner priority
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
        # Random corner priority
        empty_corners = []
        corners = [box1, box3, box7, box9]
        for box in corners:
            if box.text == '':
                empty_corners.append(box)
        if empty_corners:
            random_corner = random.choice(empty_corners)
            random_corner.text = 'O'
            turn += 1
            return
        # Random move priority
        for box in boxes:
            if box.text == '':
                box.text = 'O'
                turn += 1
                return
    
    def check_win():
        nonlocal winner, winning_boxes
        winning_combinations = [
            [box1, box2, box3], [box4, box5, box6], [box7, box8, box9],
            [box1, box4, box7], [box2, box5, box8], [box3, box6, box9],
            [box1, box5, box9], [box3, box5, box7]
        ]
        for combo in winning_combinations:
            if combo[0].text == combo[1].text == combo[2].text != '':
                winner = combo[0].text
                winning_boxes = combo
                return True
        return False
    
    def draw_board():
        screen.fill(white) 
        

        for box in boxes:
            if game_over and winning_boxes and box in winning_boxes:
                color = yellow
            else:
                color = box.color
            pygame.draw.rect(screen, color, box.rect)
            if box.text:
                font = pygame.font.Font(None, 100)  
                text = font.render(box.text, True, black)
                screen.blit(text, (box.x + box.width/2 - text.get_width()/2,
                                  box.y + box.height/2 - text.get_height()/2))
        

        pygame.draw.line(screen, black, (25, 175), (475, 175), 5)  # Horizontal line 1
        pygame.draw.line(screen, black, (25, 325), (475, 325), 5)  # Horizontal line 2
        pygame.draw.line(screen, black, (175, 25), (175, 475), 5)  # Vertical line 1
        pygame.draw.line(screen, black, (325, 25), (325, 475), 5)  # Vertical line 2
        
        if game_over:
            font = pygame.font.Font(None, 74)
            if winner:
                text = font.render(f'{winner} Wins!', True, red)
            else:
                text = font.render('Draw!', True, red)
            text_rect = text.get_rect(center=(250, 250))
            screen.blit(text, text_rect)
            

            play_again_button = pygame.Rect(175, 425, 150, 50)
            pygame.draw.rect(screen, light_gray, play_again_button)
            font = pygame.font.Font(None, 36)
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
                    play_again_button = pygame.Rect(175, 425, 150, 50)
                    if play_again_button.collidepoint(mouse_pos):
                        game_over = False
                        turn = 0
                        winner = None
                        winning_boxes = None
                        for box in boxes:
                            box.text = ''
                            box.color = light_gray
                        continue
                        
                if not game_over and turn % 2 == 0:
                    for box in boxes:
                        if box.rect.collidepoint(mouse_pos) and box.text == '':
                            box.text = 'X'
                            box.color = light_gray
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
                        box.color = light_gray
                        
        if check_win() or turn >= 9:
            game_over = True
        
        
        pygame.display.update()

play_game()
