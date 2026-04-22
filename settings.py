import pygame

#BASIC GAME SETTINGS
TIMER = 300
LOOP_PER_SECOND = 60
CELL_SIZE = 40
BACKGROUND_RGB = (30, 30, 30)
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#CORE SETTINGS, DO NOT CHANGE
MOVE_EVENT = pygame.USEREVENT + 1
DIRECTION_RIGHT = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_UP = 3    

APPLE_IMAGE = None
SNAKE_HEAD_IMAGE = None
SNAKE_BODY_IMAGE = None
ICON_IMAGE = None

def load_images():
    global APPLE_IMAGE, SNAKE_HEAD_IMAGE, SNAKE_BODY_IMAGE, ICON_IMAGE

    APPLE_IMAGE = pygame.transform.scale(
        pygame.image.load('img/apple.png').convert_alpha(),
        (CELL_SIZE, CELL_SIZE)
    )

    SNAKE_HEAD_IMAGE = pygame.transform.scale(
        pygame.image.load('img/snake_head.png').convert_alpha(),
        (CELL_SIZE, CELL_SIZE)
    )

    SNAKE_BODY_IMAGE = pygame.transform.scale(
        pygame.image.load('img/snake_body.png').convert_alpha(),
        (CELL_SIZE, CELL_SIZE)
    )

    ICON_IMAGE = pygame.transform.scale(
        pygame.image.load('img/icon.png').convert_alpha(),
        (CELL_SIZE, CELL_SIZE)
    )