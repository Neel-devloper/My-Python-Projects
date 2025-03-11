import pygame
import random
import time
pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Space Shooter by Neel Vorani')

red = (255, 0, 0)
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)

clock = pygame.time.Clock()
fps = 60
running = True

player1_score = 0
player2_score = 0

class Player:
    def __init__(self,x,y,width,height,color,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)


class Enemy:
    def __init__(self,x,y,width,height,color,speed,show):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
        self.show = show

    def update(self):
        self.y += self.speed
        if self.y >= 700:
            self.y = 0
            self.x = random.randint(0,700-self.width)
            self.show = True

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)


class Particle:
    def __init__(self,x,y,width,height,color,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y >= 700:
            self.y = 0
            self.x = random.randint(0,700-self.width)

    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)

# instances
player1 = Player(700/2,600,50,50,green,12)
player2 = Player(700/2+30,600,50,50,green,12)

enemy1 = Enemy(random.randint(0,700-50),0,50,50,red,10,True)
enemy2 = Enemy(random.randint(0,700-50),0,50,50,red,10,True)
enemy3 = Enemy(random.randint(0,700-50),0,50,50,red,10,True)
enemy4 = Enemy(random.randint(0,700-50),0,50,50,red,10,True)

particle1 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle2 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle3 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle4 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle5 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle6 = Particle(random.randint(0,700-5),0,5,5,black,20)
particle7 = Particle(random.randint(0,700-5),0,5,5,black,20)

bullet1_x = player1.x
bullet1_y = player1.y
bullet1_width = 5
bullet1_height = 20
bullet1_show = False
bullet1_speed = 30


bullet2_x = player2.x
bullet2_y = player2.y
bullet2_width = 5
bullet2_height = 20
bullet2_show = False
bullet2_speed = 30




while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # code
    screen.fill(black)

    if enemy1.show:
        pygame.draw.rect(screen,red,enemy1.get_rect())
    if enemy2.show:
        pygame.draw.rect(screen,red,enemy2.get_rect())
    if enemy3.show:
        pygame.draw.rect(screen,red,enemy3.get_rect())
    if enemy4.show:
        pygame.draw.rect(screen,red, enemy4.get_rect())

    bullet2 = pygame.Rect(bullet2_x, bullet2_y, bullet2_width, bullet2_height)
    bullet1 = pygame.Rect(bullet1_x, bullet1_y, bullet1_width, bullet1_height)

    pygame.draw.rect(screen,white, particle1.get_rect())
    pygame.draw.rect(screen,white, particle2.get_rect())
    pygame.draw.rect(screen,white, particle3.get_rect())
    pygame.draw.rect(screen,white, particle4.get_rect())
    pygame.draw.rect(screen,white, particle5.get_rect())
    pygame.draw.rect(screen,white, particle6.get_rect())
    pygame.draw.rect(screen,white, particle7.get_rect())

    pygame.draw.rect(screen,green,player1.get_rect())
    pygame.draw.rect(screen,green,player2.get_rect())

    enemy1.update()
    enemy2.update()
    enemy3.update()
    enemy4.update()

    particle1.update()
    particle2.update()
    particle3.update()
    particle4.update()
    particle5.update()
    particle6.update()
    particle7.update()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.x -= player1.speed
    if keys[pygame.K_RIGHT]:
        player1.x += player1.speed
    if keys[pygame.K_UP]:
        player1.y -= player1.speed
    if keys[pygame.K_DOWN]:
        player1.y += player1.speed

    if keys[pygame.K_a]:
        player2.x -= player2.speed
    if keys[pygame.K_d]:
        player2.x += player2.speed
    if keys[pygame.K_w]:
        player2.y -= player2.speed
    if keys[pygame.K_s]:
        player2.y += player2.speed

    if player1.get_rect().colliderect(enemy1.get_rect()) or player1.get_rect().colliderect(enemy2.get_rect()) or player1.get_rect().colliderect(enemy3.get_rect()) or player1.get_rect().colliderect(enemy4.get_rect()):
        time.sleep(0.5)
        running = False

    if player2.get_rect().colliderect(enemy1.get_rect()) or player2.get_rect().colliderect(enemy2.get_rect()) or player2.get_rect().colliderect(enemy3.get_rect()) or player2.get_rect().colliderect(enemy4.get_rect()):
        time.sleep(0.5)
        running = False

    if keys[pygame.K_RSHIFT] and not bullet1_show:
        bullet1_show = True

    if keys[pygame.K_LSHIFT] and not bullet2_show:
        bullet2_show = True

    if not bullet1_show:
        bullet1_x = player1.x
        bullet1_y = player1.y

    if not bullet2_show:
        bullet2_x = player2.x
        bullet2_y = player2.y

    if bullet1_show:
        bullet1_y -= bullet1_speed
        if bullet1_y <= 0:
            bullet1_show = False
        if bullet1.colliderect(enemy1.get_rect()):
            player1_score += 1
            enemy1.show = False
        if bullet1.colliderect(enemy2.get_rect()):
            player1_score += 1
            enemy2.show = False
        if bullet1.colliderect(enemy3.get_rect()):
            player1_score += 1
            enemy3.show = False
        if bullet1.colliderect(enemy4.get_rect()):
            player1_score += 1
            enemy4.show = False

        pygame.draw.rect(screen,white,bullet1)

    if bullet2_show:
        bullet2_y -= bullet2_speed
        if bullet2_y <= 0:
            bullet2_show = False
        if bullet2.colliderect(enemy1.get_rect()):
            player2_score += 1
            enemy1.show = False
        if bullet2.colliderect(enemy2.get_rect()):
            player2_score += 1
            enemy2.show = False
        if bullet2.colliderect(enemy3.get_rect()):
            player2_score += 1
            enemy3.show = False
        if bullet2.colliderect(enemy4.get_rect()):
            player2_score += 1
            enemy4.show = False

        pygame.draw.rect(screen,white,bullet2)

    if player1.x > 700:
        player1.x = 700
    elif player1.x < 0:
        player1.x = 0
    elif player1.y < 0:
        player1.y = 0
    elif player1.y > 700:
        player1.y = 700

    if player2.x > 700:
        player2.x = 700
    elif player2.x < 0:
        player2.x = 0
    elif player2.y < 0:
        player2.y = 0
    elif player2.y > 700:
        player2.y = 700

    # end
    pygame.display.flip()
    clock.tick(fps)


pygame.quit()
