import sys
import pygame

def run_game():

    pygame.init()


    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Rocket Game")


    bg_color = (135, 206, 250) 

  
    rocket = pygame.image.load('images/spaceship.png')  
    rocket_rect = rocket.get_rect()
    screen_rect = screen.get_rect()


    rocket_rect.center = screen_rect.center


    moving_right = moving_left = moving_up = moving_down = False
    speed = 5


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    moving_right = True
                elif event.key == pygame.K_LEFT:
                    moving_left = True
                elif event.key == pygame.K_UP:
                    moving_up = True
                elif event.key == pygame.K_DOWN:
                    moving_down = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    moving_right = False
                elif event.key == pygame.K_LEFT:
                    moving_left = False
                elif event.key == pygame.K_UP:
                    moving_up = False
                elif event.key == pygame.K_DOWN:
                    moving_down = False

     
        if moving_right and rocket_rect.right < screen_rect.right:
            rocket_rect.x += speed
        if moving_left and rocket_rect.left > 0:
            rocket_rect.x -= speed
        if moving_up and rocket_rect.top > 0:
            rocket_rect.y -= speed
        if moving_down and rocket_rect.bottom < screen_rect.bottom:
            rocket_rect.y += speed

     
        screen.fill(bg_color)
        screen.blit(rocket, rocket_rect)
        pygame.display.flip()

run_game()
