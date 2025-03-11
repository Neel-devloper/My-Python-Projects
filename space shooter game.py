import pygame
import random
pygame.init()

screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Space Shooter Game')

white = (255,255,255)
black = (0,0,0)
red  = (255,0,0)
green = (0,255,0)


score = 0

player_width = 40
player_height = 40
player_x = 700 / 2 - player_width / 2
player_y = 630
player_speed = 10

enemy_width = 25
enemy_height = 25
enemy_speed = 10

class Enemy:
    def __init__(self, width, height, x, y, speed):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.y += self.speed
        if self.y >= 700: 
            self.y = 0
            self.x = random.randint(0, 700 - self.width)

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
    
    
class Partical:
    def __init__(self,x,y,width,height,color,speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.speed = speed
    
    def update(self):
        self.y += 15
        if self.y >= 700:
            self.y = 0
            self.x = random.randint(0,700-self.width)
    
    def get_rect(self):
        return pygame.Rect(self.x,self.y,self.width,self.height)


enemy1 = Enemy(enemy_width, enemy_height, random.randint(0, 700 - enemy_width), 0, enemy_speed)
enemy2 = Enemy(enemy_width, enemy_height, random.randint(0, 700 - enemy_width), 0, enemy_speed)
enemy3 = Enemy(enemy_width, enemy_height, random.randint(0, 700 - enemy_width), 0, enemy_speed)
enemy4 = Enemy(enemy_width, enemy_height, random.randint(0, 700 - enemy_width), 0, enemy_speed)

partical1 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical2 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical3 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical4 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical5 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical6 = Partical(random.randint(0,700-5),0,5,5,black,15)
partical7 = Partical(random.randint(0,700-5),0,5,5,black,15)

bullet_width = 5
bullet_height = 20
bullet_speed = 30
bullet_x = player_x + player_width / 2 - bullet_width / 2
bullet_y = player_y
bullet_show = False

running = True
clock = pygame.time.Clock()
fps = 60

while running:
    screen.fill(white)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Player movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and player_x > 0:
        player_x -= player_speed
    if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player_x < 700 - player_width:
        player_x += player_speed
    if (keys[pygame.K_UP] or keys[pygame.K_w]) and player_y > 0:
        player_y -= player_speed
    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and player_y < 700 - player_width:
        player_y += player_speed

    enemy1.update()
    enemy2.update()
    enemy3.update()
    enemy4.update()

    partical1.update()
    partical2.update()
    partical3.update()
    partical4.update()
    partical5.update()
    partical6.update()
    partical7.update()

    if keys[pygame.K_SPACE] and not bullet_show:
        bullet_show = True
        bullet_x = player_x + player_width / 2 - bullet_width / 2
        bullet_y = player_y

    if bullet_show:
        bullet_y -= bullet_speed
        if bullet_y <= 0:
            bullet_show = False

    if bullet_show and enemy1.get_rect().colliderect(pygame.Rect(bullet_x, bullet_y, bullet_width, bullet_height)):
        enemy1.y = 0
        enemy1.x = random.randint(0, 700 - enemy_width)
        bullet_show = False
        score += 1
    
    if bullet_show and enemy2.get_rect().colliderect(pygame.Rect(bullet_x,bullet_y,bullet_width,bullet_height)):
        enemy2.y = 0
        enemy2.x = random.randint(0,700 - enemy_width)
        bullet_show = False
        score += 1

    if bullet_show and enemy3.get_rect().colliderect(pygame.Rect(bullet_x,bullet_y,bullet_width,bullet_height)):
        enemy3.y = 0
        enemy3.x = random.randint(0, 700 - enemy_width)
        bullet_show = False
        score += 1

    if bullet_show and enemy4.get_rect().colliderect(pygame.Rect(bullet_x,bullet_y,bullet_width,bullet_height)):
        enemy4.y = 0
        enemy4.x = random.randint(0,700 - enemy_width)
        bullet_show = False
        score += 1
        
    if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(enemy1.get_rect()):
        running = False 
    
    if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(enemy2.get_rect()):
        running = False
    
    if pygame.Rect(player_x,player_y, player_width, player_height).colliderect(enemy3.get_rect()):
        running = False
    
    if pygame.Rect(player_x, player_y, player_width, player_height).colliderect(enemy4.get_rect()):
        running = False

    player = pygame.Rect(player_x,player_y,player_width,player_height)
    pygame.draw.rect(screen, red, player)

    pygame.draw.rect(screen, green, enemy1.get_rect())
    pygame.draw.rect(screen, green, enemy2.get_rect())
    pygame.draw.rect(screen, green, enemy3.get_rect())
    pygame.draw.rect(screen, green, enemy4.get_rect())

    pygame.draw.rect(screen, black, partical1.get_rect())
    pygame.draw.rect(screen, black, partical2.get_rect())
    pygame.draw.rect(screen, black, partical3.get_rect())
    pygame.draw.rect(screen, black, partical4.get_rect())
    pygame.draw.rect(screen, black, partical5.get_rect())
    pygame.draw.rect(screen, black, partical6.get_rect())
    pygame.draw.rect(screen, black, partical7.get_rect())

    bullet = pygame.Rect(bullet_x,bullet_y,bullet_width,bullet_height)
    
    if bullet_show:
        pygame.draw.rect(screen, black, bullet)
    
    enemy1_rect = enemy1.get_rect()
    enemy2_rect = enemy2.get_rect()
    enemy3_rect = enemy3.get_rect()
    enemy4_rect = enemy4.get_rect()
    
    if enemy1_rect.colliderect(bullet) or enemy2_rect.colliderect(bullet) or enemy3_rect.colliderect(bullet) or enemy4_rect.colliderect(bullet):
        score += 1
    
    print(score)


    pygame.display.flip()
    clock.tick(fps)

pygame.quit()