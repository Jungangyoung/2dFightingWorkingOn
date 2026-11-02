import pygame
from fighter import Fighter

pygame.init()

# game window
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting!")

background = pygame.image.load("background.jpg").convert_alpha()


def draw_background():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))
    
#create two instances of fighters:
    


#game loop

run = True

while run:
    
    #draw background
    draw_background()
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #update display
    pygame.display.update()
            
            
#exit pygame
pygame.quit()
            
            




