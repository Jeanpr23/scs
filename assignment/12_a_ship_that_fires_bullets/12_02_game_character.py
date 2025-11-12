import sys
import pygame

def run_game():

    pygame.init()


    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Game Character")


    bg_color = (135, 206, 250)  # sky blue


    character = pygame.image.load('images/spaceship.bmp')

    
    character_rect = character.get_rect()
    screen_rect = screen.get_rect()


    character_rect.midbottom = screen_rect.midbottom


    while True:
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    
        screen.fill(bg_color)

     
        screen.blit(character, character_rect)

       
        pygame.display.flip()

run_game()
