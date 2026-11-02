import pygame
from fighter import Fighter

pygame.init()

# game window
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fighting!")

#set framerate
clock = pygame.time.Clock()
FPS = 60


#load background image
background = pygame.image.load("background.jpeg").convert_alpha()


def draw_background():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))
    
#create two instances of fighters:
    
#instances for fighters
fighter_1 = Fighter(150, 310)
fighter_2 = Fighter(800, 310)


#game loop

run = True

while run:
    
    clock.tick(FPS)
    
    #draw background
    draw_background()
    
    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #update display
    pygame.display.update()
            
            
#exit pygame
pygame.quit()
            
            




