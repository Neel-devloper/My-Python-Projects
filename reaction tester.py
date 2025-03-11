try:
    def test_reaction():
        import pygame
        import random
        import time
        pygame.init()
        pygame.font.init()
        font1 = pygame.font.Font(None, 50)
        score = 0
        text1 = font1.render('Your last score: ', True, (255, 255, 255))  
        text_rect1 = text1.get_rect(center=(700 // 2, (700 // 2) + 20))
        font2 = pygame.font.Font(None, 50)
        text2 = font2.render(str(score), True, (255, 255, 255))
        text_rect2 = text2.get_rect(center=((700 // 2) + 150, (700 // 2) + 20))
        screen = pygame.display.set_mode((700, 700))
        pygame.display.set_caption('Reaction Tester')
        red = (255, 0, 0)
        black = (0, 0, 0)
        white = (255, 255, 255)
        green = (0, 255, 0)
        
        square_width = 50
        square_height = 50
        square_x = random.randint(0, 700 - square_width)  # Random X position
        square_y = random.randint(0, 700 - square_height)  # Random Y position
        square = pygame.Rect(square_x, square_y, square_width, square_height)
        clock = pygame.time.Clock()

        # making the exit button
        exit_button = pygame.Rect(700 / 2 + 110, 650, 120, 30)  
        exit_button_font = pygame.font.Font(None, 30)  
        exit_button_text = exit_button_font.render('Exit', True, (0, 0, 0))
        exit_button_text_rect = exit_button_text.get_rect(center=exit_button.center)  

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if square.collidepoint(mouse_pos):
                        time.sleep(1.5)
                        test_reaction()
                    
                    if exit_button.collidepoint(mouse_pos):  
                        pygame.quit()

            screen.fill(black)
            pygame.draw.rect(screen, red, square)
            pygame.draw.rect(screen, green, exit_button)  
            screen.blit(text1, text_rect1)
            screen.blit(exit_button_text, exit_button_text_rect)  # 
            
            text2 = font2.render(str(score), True, (255, 255, 255))  
            screen.blit(text2, text_rect2)

            pygame.display.flip()
            clock.tick(60)
            score += 1  

        pygame.quit()

    test_reaction()

except:  
    pass