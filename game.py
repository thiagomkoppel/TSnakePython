import pygame
import settings
import random
import numpy as np
from screen import Screen
from snake import Snake

class Game:
    
    _matrix = None
    _screen = None
    _apple = None
    _snake = None
    _running = None
    _head_images = []
    
    def __init__(self):
        pygame.init()
        settings.load_images()
        self._screen = Screen()
        self.load_head_images()
        self._matrix = np.zeros((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        self._screen.fill(settings.BACKGROUND_RGB)
        self.load_apple()
        self.load_snake()
        self.GameLoop(self._screen.get_screen())
        pygame.quit()

    def GameLoop(self, screen):
        self._running = True
        clock = pygame.time.Clock()
        pygame.time.set_timer(settings.MOVE_EVENT, settings.TIMER)

        while self._running:
            
            if self._apple == False: self.load_apple()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == settings.MOVE_EVENT:
                    head_x, head_y = self._snake.get_nod(0)
                    move, head_image = self.calculate_move(head_x, head_y)
                    self._snake.set_head(head_image)  
                    self._snake.insert(0, move)                    
                    self._screen.draw_rect(head_x, head_y)
                   
                    self._screen.blit(settings.SNAKE_BODY_IMAGE, (head_x, head_y))
                    self._screen.fill(settings.BACKGROUND_RGB)
                    self._snake.pop()  # remove tail unless snake ate fruit
                    if self.detect_overlap("snake"): settings.GAMEOVER = 0 
                    if self.detect_overlap("apple"): self.grow()                
                     

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT and self._snake.get_dir() != settings.DIRECTION_LEFT:
                        self._snake.set_dir(0)
                    elif event.key == pygame.K_LEFT and self._snake.get_dir() != settings.DIRECTION_RIGHT:
                        self._snake.set_dir(2)
                    elif event.key == pygame.K_UP and self._snake.get_dir() != settings.DIRECTION_DOWN:
                        self._snake.set_dir(3)
                    elif event.key == pygame.K_DOWN and self._snake.get_dir() != settings.DIRECTION_UP:
                        self._snake.set_dir(1)
                    
            self._screen.blit(self._snake.get_head_image(), self._snake.get_nod(0)) 
            self.reload_screen()      
            pygame.display.flip()
            self.set_game_status() 
            clock.tick(settings.LOOP_PER_SECOND)          

    def set_game_status(self):
        if settings.GAMEOVER == 0:
            self._running = False
            #add gameover message

    def load_head_images(self):
        head_image = settings.SNAKE_HEAD_IMAGE.convert_alpha()
        head_image = pygame.transform.scale(head_image, (settings.CELL_SIZE, settings.CELL_SIZE))        
        self._head_images.append(pygame.transform.rotate(head_image, -90)) 
        self._head_images.append(pygame.transform.rotate(head_image, 180))
        self._head_images.append(pygame.transform.rotate(head_image, 90))
        self._head_images.append(head_image)

    def grow(self):
        self._apple = None
        self._snake.grow()

    def get_random_position(self):
        row = random.randrange(0, self._matrix.shape[0], settings.CELL_SIZE)
        col = random.randrange(0, self._matrix.shape[1], settings.CELL_SIZE)
        return (row, col)
    
    def load_apple(self):
        if not self._apple:
            self._apple = self.get_random_position()
            self._screen.blit(settings.APPLE_IMAGE.convert_alpha(), self._apple)
        else:
            self._screen.blit(settings.APPLE_IMAGE.convert_alpha(), self._apple)            

    def load_snake(self):
        self._snake = Snake(self.get_random_position())
        if len(self._snake.get_snake()) > 1:
            self._screen.blit(settings.SNAKE_BODY_IMAGE.convert_alpha(), self._snake.get_nod(0))
        else:
            self._screen.blit(self._head_images[settings.DIRECTION_RIGHT], self._snake.get_nod(0))
            self._snake.set_head(self._head_images[settings.DIRECTION_RIGHT])

    def calculate_move(self,head_x, head_y):        
        if self._snake.get_dir() == settings.DIRECTION_RIGHT:
            new_head = (head_x + settings.CELL_SIZE, head_y)
            head_image = self._head_images[settings.DIRECTION_RIGHT]
        elif self._snake.get_dir() == settings.DIRECTION_LEFT:
            new_head = (head_x - settings.CELL_SIZE, head_y)
            head_image = self._head_images[settings.DIRECTION_LEFT]
        elif self._snake.get_dir() == settings.DIRECTION_UP:
            new_head = (head_x, head_y - settings.CELL_SIZE)
            head_image = self._head_images[settings.DIRECTION_UP]
        elif self._snake.get_dir() == settings.DIRECTION_DOWN:
            new_head = (head_x, head_y + settings.CELL_SIZE)
            head_image = self._head_images[settings.DIRECTION_DOWN]
        return new_head, head_image
    
    def reload_screen(self):
        self.load_apple()
        for nod in self._snake.get_snake():
            x, y = nod
            if nod != self._snake.get_nod(0):
                self._screen.blit(settings.SNAKE_BODY_IMAGE, (x, y))

    def detect_overlap(self, x):
        overlap = False
        if x == "apple":
            snake_i, snake_j = self._snake.get_nod(0)
            apple_i, apple_j = self._apple
            overlap = not (
                snake_i + settings.CELL_SIZE <= apple_i or
                snake_i >= apple_i + settings.CELL_SIZE or
                snake_j + settings.CELL_SIZE <= apple_j or
                snake_j >= apple_j + settings.CELL_SIZE
            )
        else:
            if len(self._snake.get_snake()) > 1:             
                temp = self._snake.get_snake().copy()
                head = temp[0]
                temp.pop(0)
                for i in temp:
                    if i == head:
                        overlap = True
        if overlap:
            x = 1
        return overlap
        

game = Game()



