# 14_02_target_practice_scoring.py
import pygame, sys

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)
t = pygame.Rect(500,150,60,100)
b, score = [], 0
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            b.append(pygame.Rect(p.right,p.centery-5,10,10))

    for x in b[:]:
        x.x += 5
        if x.colliderect(t): score+=1; b.remove(x)
        elif x.x>600: b.remove(x)

    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    pygame.draw.rect(s,(0,200,0),t)
    for x in b: pygame.draw.rect(s,(0,0,0),x)
    s.blit(f.render(f"Score:{score}",1,(0,0,0)),(10,10))
    pygame.display.flip(); c.tick(60)