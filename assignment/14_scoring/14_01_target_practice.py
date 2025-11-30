# 14_01_target_practice.py
import pygame, sys

pygame.init()
screen = pygame.display.set_mode((600, 400))
player = pygame.Rect(50, 180, 40, 40)
target = pygame.Rect(500, 150, 60, 100)
bullets = []
clock = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            bullets.append(pygame.Rect(player.right, player.centery-5, 10, 10))

    for b in bullets[:]:
        b.x += 5
        if b.colliderect(target): print("Hit!"); bullets.remove(b)
        elif b.x > 600: bullets.remove(b)

    screen.fill((255,255,255))
    pygame.draw.rect(screen, (255,0,0), player)
    pygame.draw.rect(screen, (0,200,0), target)
    for b in bullets: pygame.draw.rect(screen, (0,0,0), b)
    pygame.display.flip()
    clock.tick(60)
