import pygame

CELL_SIZE = 20
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BACKGROUND_RGB = (30, 30, 30)
MOVE_EVENT = pygame.USEREVENT + 1
DIRECTION_RIGHT = 0
DIRECTION_DOWN = 1
DIRECTION_LEFT = 2
DIRECTION_UP = 3

def load_images():
    global APPLE_IMAGE
    global SNAKE_HEAD_IMAGE
    global SNAKE_BODY_IMAGE
    global ICON_IMAGE

    APPLE_IMAGE = pygame.image.load('img/apple.png')
    SNAKE_HEAD_IMAGE = pygame.image.load('img/snake_head.png')
    SNAKE_BODY_IMAGE = pygame.image.load('img/snake_body.png')
    ICON_IMAGE = pygame.image.load('img/icon.png')