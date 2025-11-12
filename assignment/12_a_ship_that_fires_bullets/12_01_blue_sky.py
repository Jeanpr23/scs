import sys
import pygame

def run_game():
    # Initialize pygame modules
    pygame.init()

  
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Blue Sky")


    bg_color = (135, 206, 250)  # sky blue

   
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

     
        screen.fill(bg_color)

   
        pygame.display.flip()

run_game()
