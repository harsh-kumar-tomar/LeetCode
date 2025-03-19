import pygame

from constants import *

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Express")

rocket_image = pygame.image.load("rocket.png")
rocket_image = pygame.transform.scale(rocket_image, (rocket_image_width, rocket_image_height))
pygame.display.set_icon(rocket_image)

running = True


def updatePos(image, x, y):
    screen.blit(image, (x, y))


while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                rocket_speed_x = -1*speed

            if event.key == pygame.K_RIGHT:
                rocket_speed_x = speed

            if event.key == pygame.K_UP:
                rocket_speed_y = -1*speed

            if event.key == pygame.K_DOWN:
                rocket_speed_y = speed

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                rocket_speed_x = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                rocket_speed_y = 0

    rocket_x += rocket_speed_x
    rocket_y += rocket_speed_y

    if rocket_x < 0:
        rocket_x = 0
    elif rocket_x > WIDTH - rocket_image_width:
        rocket_x = WIDTH - rocket_image_width

    if rocket_y < 0:
        rocket_y = 0
    elif rocket_y > HEIGHT - rocket_image_height:
        rocket_y = HEIGHT - rocket_image_height

    updatePos(rocket_image, rocket_x, rocket_y)
    pygame.display.update()

pygame.quit()
