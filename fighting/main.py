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

#define colours
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

#load background image
background = pygame.image.load("image/background.jpeg").convert_alpha()


def draw_background():
    scaled_background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_background, (0, 0))
    
#craete health bars
def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, YELLOW, pygame.Rect(x - 2, y - 2, 404, 34))
    pygame.draw.rect(screen, RED, pygame.Rect(x, y, 400, 30))
    pygame.draw.rect(screen, YELLOW, pygame.Rect(x, y, 400 * ratio, 30))
    
#create two instances of fighters:
fighter_1 = Fighter(150, 310)
fighter_2 = Fighter(800, 310)


#game loop

run = True

while run:
    
    clock.tick(FPS)
    
    #draw background
    draw_background()
    
    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 680, 20)
    
    #move fighters
    fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2)
    
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
            
            




