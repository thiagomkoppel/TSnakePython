import pygame
import settings
import random
from screen import Screen
from snake import Snake

class Game:
        
    def __init__(self):
        self._gameover = 1
        self._apple = None
        self._snake = None
        self._running = None
        self._dir_flag = True
        self._head_images = []
        pygame.init()
        self._screen = Screen()
        self.load_head_images()
        self._screen.fill(settings.BACKGROUND_RGB)
        self.load_snake()
        self.load_apple()
        self.GameLoop(self._screen.get_screen())
        pygame.quit()

    def GameLoop(self, screen):
        self._running = True
        clock = pygame.time.Clock()
        pygame.time.set_timer(settings.MOVE_EVENT, settings.TIMER)
        while self._running:            
            if not self._apple: self.load_apple()            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False
                elif event.type == settings.MOVE_EVENT:
                    head_x, head_y = self._snake.get_node(0)
                    move, head_image = self.calculate_move(head_x, head_y)
                    self._snake.set_head(head_image)  
                    self._snake.insert(0, move)                         
                    if self.snake_hits_itself():
                        self._gameover = 0
                    elif self._snake.get_node(0) == self._apple:
                        self._apple = None
                        self.load_apple()
                    else:                  
                        self._snake.pop() #removes last node due to snake movement               
                    self._dir_flag = True
                elif event.type == pygame.KEYDOWN and self._dir_flag:
                    if event.key == pygame.K_RIGHT and self._snake.get_dir() != settings.DIRECTION_LEFT:
                        self._snake.set_dir(0)
                        self._dir_flag = False                        
                    elif event.key == pygame.K_LEFT and self._snake.get_dir() != settings.DIRECTION_RIGHT:
                        self._snake.set_dir(2)
                        self._dir_flag = False
                    elif event.key == pygame.K_UP and self._snake.get_dir() != settings.DIRECTION_DOWN:
                        self._snake.set_dir(3)
                        self._dir_flag = False
                    elif event.key == pygame.K_DOWN and self._snake.get_dir() != settings.DIRECTION_UP:
                        self._snake.set_dir(1)
                        self._dir_flag = False            
            self.draw()      
            pygame.display.flip()
            self.set_game_status() 
            clock.tick(settings.LOOP_PER_SECOND)          

    def set_game_status(self):
        if self._gameover == 0:
            self._running = False
            #add gameover message

    def load_head_images(self):
        head_image = settings.SNAKE_HEAD_IMAGE   
        self._head_images.append(pygame.transform.rotate(head_image, -90)) 
        self._head_images.append(pygame.transform.rotate(head_image, 180))
        self._head_images.append(pygame.transform.rotate(head_image, 90))
        self._head_images.append(head_image)

    def get_random_position(self):
        while True:
            x = random.randrange(0, settings.SCREEN_WIDTH, settings.CELL_SIZE)
            y = random.randrange(0, settings.SCREEN_HEIGHT, settings.CELL_SIZE)
            pos = (x, y)
            if not self._snake:
                return pos
            if pos not in self._snake.get_snake():
                return pos
    
    def load_apple(self):
        if not self._apple:
            self._apple = self.get_random_position()                        

    def load_snake(self):
        self._snake = Snake(self.get_random_position())
        if len(self._snake.get_snake()) > 1:
            self._screen.blit(settings.SNAKE_BODY_IMAGE, self._snake.get_node(0))
        else:
            self._screen.blit(self._head_images[settings.DIRECTION_RIGHT], self._snake.get_node(0))
            self._snake.set_head(self._head_images[settings.DIRECTION_RIGHT])

    def calculate_move(self,head_x, head_y):        
        if self._snake.get_dir() == settings.DIRECTION_RIGHT:
            if head_x > settings.SCREEN_WIDTH - settings.CELL_SIZE:
                head_x = 0 - settings.CELL_SIZE
            new_head = (head_x + settings.CELL_SIZE, head_y)
            head_image = self._head_images[settings.DIRECTION_RIGHT]
        elif self._snake.get_dir() == settings.DIRECTION_LEFT:
            if head_x < 0:
                head_x = settings.SCREEN_WIDTH
            new_head = (head_x - settings.CELL_SIZE, head_y)
            head_image = self._head_images[settings.DIRECTION_LEFT]
        elif self._snake.get_dir() == settings.DIRECTION_UP:
            if head_y < 0:
                head_y = settings.SCREEN_HEIGHT
            new_head = (head_x, head_y - settings.CELL_SIZE)
            head_image = self._head_images[settings.DIRECTION_UP]
        elif self._snake.get_dir() == settings.DIRECTION_DOWN:
            if head_y > settings.SCREEN_HEIGHT - settings.CELL_SIZE:
                head_y = 0 - settings.CELL_SIZE
            new_head = (head_x, head_y + settings.CELL_SIZE)
            head_image = self._head_images[settings.DIRECTION_DOWN]
        return new_head, head_image
    
    def snake_hits_itself(self):
        head = self._snake.get_node(0)
        body = self._snake.get_snake()[1:]
        return head in body
           
    def draw(self):
        self._screen.fill(settings.BACKGROUND_RGB)
        # apple
        self._screen.blit(settings.APPLE_IMAGE, self._apple)
        # snake body
        for segment in self._snake.get_snake()[1:]:
            self._screen.blit(settings.SNAKE_BODY_IMAGE, segment)
        # head
        self._screen.blit(self._snake.get_head_image(), self._snake.get_node(0))

if __name__ == "__main__":    
    game = Game()



