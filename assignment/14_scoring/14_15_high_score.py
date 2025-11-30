# 14_15_high_score.py
import pygame, sys

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)   # player
bullets, targets = [], []
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

score, high_score = 0, 0

# Create fleet
for i in range(5):
    targets.append(pygame.Rect(400+i*40, 100, 30, 30))

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            bullets.append(pygame.Rect(p.right,p.centery-5,10,10))

    # Move bullets
    for b in bullets[:]:
        b.x += 5
        for t in targets[:]:
            if b.colliderect(t):
                score += 1
                if score > high_score: high_score = score
                bullets.remove(b); targets.remove(t); break
        if b.x>600 and b in bullets: bullets.remove(b)

    # If fleet cleared → reset fleet
    if not targets:
        for i in range(5):
            targets.append(pygame.Rect(400+i*40, 100, 30, 30))

    # Draw everything
    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    for t in targets: pygame.draw.rect(s,(0,200,0),t)
    for b in bullets: pygame.draw.rect(s,(0,0,0),b)

    # Show score + high score
    s.blit(f.render(f"Score:{score}",1,(0,0,0)),(10,10))
    s.blit(f.render(f"High Score:{high_score}",1,(0,0,0)),(10,40))

    pygame.display.flip(); c.tick(60)
