import pygame
import settings
from PIL import Image

class Screen:

    _screen = None

    def __init__(self):        
        pygame.display.set_icon(settings.ICON_IMAGE)
        self._screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption("TSnake")        

    def get_screen(self):
        return self._screen

    def update(self):
        return None

    def fill(self, rgb):
        r , g, b = rgb
        self._screen.fill((r, g, b))

    def add_image(self, image):
        image_block = pygame.transform.scale(image, (settings.CELL_SIZE, settings.CELL_SIZE))
        return image_block
    
    def blit(self, image, position):
        x, y = position
        self._screen.blit(self.add_image(image), (x, y))

    def draw_rect(self, x , y):
        pygame.draw.rect(self._screen, (settings.BACKGROUND_RGB), (x, y, settings.CELL_SIZE, settings.CELL_SIZE))

