# 14_11_new_level.py
import pygame, sys

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)   # player
bullets, targets, score, level = [], [], 0, 1
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

def create_fleet(rows, cols):
    fleet = []
    for r in range(rows):
        for i in range(cols):
            fleet.append(pygame.Rect(300+i*40, 50+r*40, 30, 30))
    return fleet

# Start with first fleet
targets = create_fleet(3,6)
fleet_dir = 1

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
                score+=1; bullets.remove(b); targets.remove(t); break
        if b.x>600 and b in bullets: bullets.remove(b)

    # Move fleet
    edge_hit = False
    for t in targets:
        t.x += fleet_dir * level  # fleet gets faster each level
        if t.right >= 600 or t.left <= 0:
            edge_hit = True
    if edge_hit:
        fleet_dir *= -1
        for t in targets: t.y += 20

    # If fleet cleared → new level
    if not targets:
        level += 1
        targets = create_fleet(3,6)

    # Draw everything
    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    for t in targets: pygame.draw.rect(s,(0,200,0),t)
    for b in bullets: pygame.draw.rect(s,(0,0,0),b)

    # Show score + level
    s.blit(f.render(f"Score:{score}",1,(0,0,0)),(10,10))
    s.blit(f.render(f"Level:{level}",1,(0,0,0)),(10,40))

    pygame.display.flip(); c.tick(60)
