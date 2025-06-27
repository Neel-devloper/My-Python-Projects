import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 400, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 155, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Bird settings
BIRD_WIDTH = 30
BIRD_HEIGHT = 30
bird_x = 50
bird_y = HEIGHT // 2
bird_vel = 0
gravity = 0.5
flap_strength = -10

# Load bird image once
bird_img = pygame.image.load('/Users/neelvorani/Desktop/python pycharm projects/flappy img.png') # change this with the path on your computer
bird_img = pygame.transform.scale(bird_img, (BIRD_WIDTH, BIRD_HEIGHT))

# Pipe settings
pipe_width = 60
pipe_gap = 150
pipe_speed = 4
pipe_list = []

# Font
font = pygame.font.SysFont(None, 48)

# Score
score = 0

def create_pipe():
    """Return a dict with top/bottom Rects and a scored flag."""
    height = random.randint(100, HEIGHT - 200)
    top_rect = pygame.Rect(WIDTH, 0, pipe_width, height)
    bottom_rect = pygame.Rect(WIDTH, height + pipe_gap, pipe_width, HEIGHT)
    return {"top": top_rect, "bottom": bottom_rect, "scored": False}

def draw_pipes(pipes):
    """Draw all pipes stored in pipe_list."""
    for pipe in pipes:
        pygame.draw.rect(SCREEN, GREEN, pipe["top"])
        pygame.draw.rect(SCREEN, GREEN, pipe["bottom"])

def check_collision(pipes, bird_rect):
    """Return True if bird collides with any pipe or leaves screen."""
    # Pipe collisions
    for pipe in pipes:
        if bird_rect.colliderect(pipe["top"]) or bird_rect.colliderect(pipe["bottom"]):
            return True
    if bird_rect.top < 0 or bird_rect.bottom > HEIGHT:
        return True
    return False

def draw_text(text, size, color, x, y):
    font_obj = pygame.font.SysFont(None, size)
    surf = font_obj.render(text, True, color)
    rect = surf.get_rect(center=(x, y))
    SCREEN.blit(surf, rect)

def game_loop():
    global bird_y, bird_vel, pipe_list, score

    # Reset state
    bird_y = HEIGHT // 2
    bird_vel = 0
    pipe_list = []
    score = 0
    spawn_timer = 0

    while True:
        clock.tick(FPS)
        SCREEN.fill(BLUE)

        # ——— Input Handling ———
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird_vel = flap_strength

        # ——— Bird Physics ———
        bird_vel += gravity
        bird_y += bird_vel
        bird_rect = pygame.Rect(bird_x, int(bird_y), BIRD_WIDTH, BIRD_HEIGHT)
        SCREEN.blit(bird_img, bird_rect.topleft)

        # ——— Pipe Spawning & Movement ———
        spawn_timer += 1
        if spawn_timer > 90:
            pipe_list.append(create_pipe())
            spawn_timer = 0

        for pipe in pipe_list:
            pipe["top"].x -= pipe_speed
            pipe["bottom"].x -= pipe_speed

            # Scoring: count once per pipe
            if pipe["top"].right < bird_x and not pipe["scored"]:
                score += 1
                pipe["scored"] = True

        # Remove off-screen pipes
        pipe_list[:] = [p for p in pipe_list if p["top"].right > 0]

        # Draw pipes
        draw_pipes(pipe_list)

        # Draw score
        draw_text(f"Score: {score}", 36, WHITE, WIDTH // 2, 40)

        # ——— Collision Check ———
        if check_collision(pipe_list, bird_rect):
            draw_text("Game Over", 64, WHITE, WIDTH // 2, HEIGHT // 2)
            pygame.display.update()
            pygame.time.wait(2000)
            return  # back to main loop to restart

        # ——— Update Display ———
        pygame.display.update()

# ——— Entry Point ———
if __name__ == "__main__":
    while True:
        game_loop()