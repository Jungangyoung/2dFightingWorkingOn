import pygame
from pygame import mixer
from fighter import Fighter

mixer.init()
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

#define game variables
intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]#[fighter1_score, fighter2_score]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define fighter variables
ICARA_SIZE = 256
ICARA_SCALE = 1.25
ICARA_OFFSET = [60, 0]
ICARA_DATA = [ICARA_SIZE, ICARA_SCALE, ICARA_OFFSET]

#### LOAD #####
#load music and sounds
pygame.mixer.music.load("audio/music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)
hit_fx = pygame.mixer.Sound("audio/boung.wav")
hit_fx.set_volume(0.5)

#load background image
background = pygame.image.load("image/background.png").convert_alpha()

#load spritesheets
icara_sheet = pygame.image.load("image/test.png").convert_alpha()

#load victory image
victory_img = pygame.image.load("image/victory.png").convert_alpha()

#define animation steps
ICARA_ANIMATION_STEPS = [10, 8, 1, 7, 7, 3, 7]

#define font
count_font = pygame.font.SysFont("Arial", 80)
score_font = pygame.font.SysFont("Arial", 30)

#function for drawing text
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#create background
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
fighter_1 = Fighter(1, 150, 310, False, ICARA_DATA, icara_sheet, ICARA_ANIMATION_STEPS, hit_fx)
fighter_2 = Fighter(2, 800, 310, True, ICARA_DATA, icara_sheet, ICARA_ANIMATION_STEPS, hit_fx)


#game loop

run = True

while run:
    
    clock.tick(FPS)
    
    #draw background
    draw_background()
    
    #show player stats
    draw_health_bar(fighter_1.health, 20, 20)
    draw_health_bar(fighter_2.health, 680, 20)
    draw_text("P1: " + str(score[0]), score_font, WHITE, 20, 60)
    draw_text("P2: " + str(score[1]), score_font, WHITE, 680, 60)
    
    #update countdown
    if intro_count <= 0:    
        #move fighters
        fighter_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_2, round_over)
        fighter_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, fighter_1, round_over)
    else: 
        #display count timer
        draw_text(str(intro_count), count_font, WHITE, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3)
        #update count timer
        if (pygame.time.get_ticks() - last_count_update) >= 1000:
            intro_count -= 1
            last_count_update = pygame.time.get_ticks()
            #print(intro_count)
                          
    #update fighters
    fighter_1.update()
    fighter_2.update()
    
    #draw fighters
    fighter_1.draw(screen)
    fighter_2.draw(screen)
    
    #check for player defeat
    if round_over == False:
        if fighter_1.alive == False:
            score[1] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
        elif fighter_2.alive == False:
            score[0] += 1
            round_over = True
            round_over_time = pygame.time.get_ticks()
    else:
        #display victory image
        screen.blit(victory_img, (280, 150))
        if pygame.time.get_ticks() - round_over_time > ROUND_OVER_COOLDOWN:
            round_over = False
            intro_count = 3
            fighter_1 = Fighter(1, 150, 310, False, ICARA_DATA, icara_sheet, ICARA_ANIMATION_STEPS, hit_fx)
            fighter_2 = Fighter(2, 800, 310, True, ICARA_DATA, icara_sheet, ICARA_ANIMATION_STEPS, hit_fx)
    
    #event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    #update display
    pygame.display.update()
            
            
#exit pygame
pygame.quit()
            
            




