import pygame
import random

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 400
WHITE = (255, 255, 255)
GROUND_HEIGHT = 300
GRAVITY = 1
JUMP_STRENGTH = -15
OBSTACLE_SPEED = 7

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Game")
clock = pygame.time.Clock()

# Load images
dino_img = pygame.image.load("dino.png")  # Add a small dino image
cactus_img = pygame.image.load("dino.png")  # Add a small cactus image
dino_img = pygame.transform.scale(dino_img, (50, 50))
cactus_img = pygame.transform.scale(cactus_img, (30, 50))

# Dino class
class Dino:
    def __init__(self):
        self.image = dino_img
        self.x = 50
        self.y = GROUND_HEIGHT - 50
        self.velocity = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.velocity = JUMP_STRENGTH
            self.is_jumping = True

    def update(self):
        self.y += self.velocity
        self.velocity += GRAVITY
        if self.y >= GROUND_HEIGHT - 50:
            self.y = GROUND_HEIGHT - 50
            self.is_jumping = False

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Obstacle class
class Obstacle:
    def __init__(self):
        self.image = cactus_img
        self.x = WIDTH
        self.y = GROUND_HEIGHT - 50

    def update(self):
        self.x -= OBSTACLE_SPEED
        if self.x < -30:
            self.x = WIDTH + random.randint(100, 300)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Game objects
dino = Dino()
obstacle = Obstacle()
running = True

# Game loop
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino.jump()

    dino.update()
    obstacle.update()

    # Collision detection
    if dino.x + 50 > obstacle.x and dino.x < obstacle.x + 30 and dino.y + 50 > obstacle.y:
        print("Game Over!")
        running = False

    dino.draw()
    obstacle.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()
