import pygame
import settings

class Screen:

    def __init__(self):
        self._screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        settings.load_images()   
        pygame.display.set_icon(settings.ICON_IMAGE)
        pygame.display.set_caption("TSnake")        

    def get_screen(self):
        return self._screen

    def fill(self, rgb):
        r , g, b = rgb
        self._screen.fill((r, g, b))
  
    def blit(self, image, position):
        x, y = position
        self._screen.blit(image, (x, y))

    def draw_rect(self, x , y):
        pygame.draw.rect(self._screen, (settings.BACKGROUND_RGB), (x, y, settings.CELL_SIZE, settings.CELL_SIZE))