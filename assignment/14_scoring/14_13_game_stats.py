# 14_13_game_stats.py
import pygame, sys

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)   # player
bullets, targets = [], []
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

# Game stats class
class GameStats:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lives = 3

stats = GameStats()

# Create a small fleet
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
                stats.score += 1
                bullets.remove(b); targets.remove(t); break
        if b.x>600 and b in bullets: bullets.remove(b)

    # If fleet cleared → new level
    if not targets:
        stats.level += 1
        for i in range(5):
            targets.append(pygame.Rect(400+i*40, 100, 30, 30))

    # Draw everything
    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    for t in targets: pygame.draw.rect(s,(0,200,0),t)
    for b in bullets: pygame.draw.rect(s,(0,0,0),b)

    # Show stats
    s.blit(f.render(f"Score:{stats.score}",1,(0,0,0)),(10,10))
    s.blit(f.render(f"Level:{stats.level}",1,(0,0,0)),(10,40))
    s.blit(f.render(f"Lives:{stats.lives}",1,(0,0,0)),(10,70))

    pygame.display.flip(); c.tick(60)
