import pygame
import random
from pygame import mixer

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Set up the game display
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Save The Car")
background=pygame.image.load("C:/Users/nilas/3452442.jpg")

over_font=pygame.font.Font('freesansbold.ttf',64)

def game_over_text():
    over_text=over_font.render("GAME OVER",True,(0,0,0))
    screen.blit(over_text,(200,250))


#background music
mixer.music.load("C:/Users/nilas/Arcade-background-music-retro-style.mp3")
mixer.music.play(-1)
# Define game objects
car_width = 73
car_height = 82
car_image = pygame.image.load("C:/Users/nilas/OneDrive/Desktop/icons8-racing-car-64.png")
obstacle_width = 100
obstacle_height = 100
obstacle_speed = 7
pause = False
# Define functions
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def draw_car(x, y):
    screen.blit(car_image, (x, y))

def draw_obstacle(x, y):
    pygame.draw.rect(screen, RED, [x, y, obstacle_width, obstacle_height])

def is_collision(car_x, car_y, obstacle_x, obstacle_y):
    if (car_x + car_width > obstacle_x) and (car_x < obstacle_x + obstacle_width):
        if (car_y + car_height > obstacle_y) and (car_y < obstacle_y + obstacle_height):
            return True
    return False

# Set up the game loop
clock = pygame.time.Clock()
FPS = 60
score = 0

# Main game loop
def game_loop():
    global score
    game_exit = False
    car_x = SCREEN_WIDTH * 0.45
    car_y = SCREEN_HEIGHT * 0.8
    car_speed = 0
    obstacle_x = random.randrange(0, SCREEN_WIDTH - obstacle_width)
    obstacle_y = -obstacle_height
    while not game_exit:
       
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    car_speed = -5
                elif event.key == pygame.K_RIGHT:
                    car_speed = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    car_speed = 0
          
        car_x += car_speed
        screen.blit(background,(0,0))
        draw_car(car_x, car_y)
        draw_obstacle(obstacle_x, obstacle_y)
        obstacle_y += obstacle_speed
        if obstacle_y > SCREEN_HEIGHT:
            obstacle_x = random.randrange(0, SCREEN_WIDTH - obstacle_width)
            obstacle_y = -obstacle_height
            score += 1
        if is_collision(car_x, car_y, obstacle_x, obstacle_y):
            game_over_text()
            pygame.QUIT()
            pygame.display.flip()
        draw_text("Score: " + str(score), pygame.font.SysFont("freesansbold.ttf", 30), BLACK, SCREEN_WIDTH / 2, 10)
        pygame.display.update()
        clock.tick(FPS)
    pygame.quit()
    quit()

game_loop()
