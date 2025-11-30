# 14_06_world_boundaries.py
import pygame, sys

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)   # player
t = pygame.Rect(500,150,60,100) # target
bullets, score = [], 0
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            bullets.append(pygame.Rect(p.right,p.centery-5,10,10))

    # Player movement with boundaries
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and p.top>0: p.y -= 5
    if keys[pygame.K_DOWN] and p.bottom<400: p.y += 5

    # Move bullets, remove if outside world boundaries
    for b in bullets[:]:
        b.x += 5
        if b.colliderect(t): score+=1; bullets.remove(b)
        elif b.x>600: bullets.remove(b)

    # Draw everything
    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    pygame.draw.rect(s,(0,200,0),t)
    for b in bullets: pygame.draw.rect(s,(0,0,0),b)
    s.blit(f.render(f"Score:{score}",1,(0,0,0)),(10,10))
    pygame.display.flip(); c.tick(60)
