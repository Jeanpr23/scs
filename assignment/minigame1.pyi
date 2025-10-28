# Code_Jam

import pygame, sys

pygame.init()
WIDTH, HEIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pumpkin 🎃")
clock = pygame.time.Clock()

BLACK = (20, 20, 20)
ORANGE = (255, 140, 0)
GREEN = (0, 200, 0)
PURPLE = (120, 0, 120)

pumpkin = pygame.Rect(100, HEIGHT - 70, 40, 40)
pumpkin_speed_x = 0
pumpkin_speed_y = 0
gravity = 0.5
jump_strength = -10
on_ground = False

platforms = [
    pygame.Rect(0, HEIGHT - 20, WIDTH, 20),
    pygame.Rect(150, 400, 120, 15),
    pygame.Rect(350, 320, 120, 15),
    pygame.Rect(550, 240, 120, 15),
    pygame.Rect(250, 160, 120, 15),
]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                pumpkin_speed_x = -5
            if event.key == pygame.K_RIGHT:
                pumpkin_speed_x = 5
            if event.key == pygame.K_SPACE and on_ground:
                pumpkin_speed_y = jump_strength
                on_ground = False
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                pumpkin_speed_x = 0

    pumpkin.x += pumpkin_speed_x
    pumpkin.y += pumpkin_speed_y
    pumpkin_speed_y += gravity

    on_ground = False
    for plat in platforms:
        if pumpkin.colliderect(plat) and pumpkin_speed_y >= 0:
            pumpkin.bottom = plat.top
            pumpkin_speed_y = 0
            on_ground = True

    if pumpkin.left < 0: pumpkin.left = 0
    if pumpkin.right > WIDTH: pumpkin.right = WIDTH
    if pumpkin.top > HEIGHT:
        pumpkin.x, pumpkin.y = 100, HEIGHT - 70
        pumpkin_speed_y = 0

    screen.fill(BLACK)
    for plat in platforms:
        pygame.draw.rect(screen, PURPLE, plat)
    pygame.draw.ellipse(screen, ORANGE, pumpkin)
    stem_rect = pygame.Rect(pumpkin.centerx - 5, pumpkin.top - 10, 10, 10)
    pygame.draw.rect(screen, GREEN, stem_rect)
    pygame.display.flip()
    clock.tick(60)
