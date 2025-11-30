# 14_12_powerups.py
import pygame, sys, random

pygame.init()
s = pygame.display.set_mode((600,400))
p = pygame.Rect(50,180,40,40)   # player
bullets, targets, score = [], [], 0
f = pygame.font.SysFont(None,30)
c = pygame.time.Clock()

# Fleet setup
for r in range(2):
    for i in range(5):
        targets.append(pygame.Rect(300+i*40, 50+r*40, 30, 30))

fleet_dir = 1
bullet_speed = 5
powerup = None
powerup_timer = 0

while True:
    for e in pygame.event.get():
        if e.type==pygame.QUIT: pygame.quit(); sys.exit()
        if e.type==pygame.KEYDOWN and e.key==pygame.K_SPACE:
            bullets.append(pygame.Rect(p.right,p.centery-5,10,10))

    # Spawn powerup randomly
    if not powerup and random.randint(0,500)==1:
        powerup = pygame.Rect(random.randint(100,500), random.randint(50,350), 20, 20)

    # Move bullets
    for b in bullets[:]:
        b.x += bullet_speed
        for t in targets[:]:
            if b.colliderect(t):
                score+=1; bullets.remove(b); targets.remove(t); break
        if powerup and b.colliderect(powerup):
            bullet_speed = 10   # activate faster bullets
            powerup = None
            powerup_timer = 300 # lasts ~5 seconds at 60fps
            bullets.remove(b)
        elif b.x>600 and b in bullets: bullets.remove(b)

    # Powerup timer countdown
    if powerup_timer>0:
        powerup_timer -= 1
        if powerup_timer==0:
            bullet_speed = 5    # reset to normal

    # Move fleet
    edge_hit = False
    for t in targets:
        t.x += fleet_dir
        if t.right >= 600 or t.left <= 0:
            edge_hit = True
    if edge_hit:
        fleet_dir *= -1
        for t in targets: t.y += 20

    # Draw everything
    s.fill((255,255,255))
    pygame.draw.rect(s,(255,0,0),p)
    for t in targets: pygame.draw.rect(s,(0,200,0),t)
    for b in bullets: pygame.draw.rect(s,(0,0,0),b)
    if powerup: pygame.draw.rect(s,(0,0,255),powerup)  # blue = powerup
    s.blit(f.render(f"Score:{score}",1,(0,0,0)),(10,10))
    s.blit(f.render(f"Bullet speed:{bullet_speed}",1,(0,0,0)),(10,40))
    pygame.display.flip(); c.tick(60)
