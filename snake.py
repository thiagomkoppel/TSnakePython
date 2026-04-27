import random
import settings

class Snake:

    def __init__(self, position):
        self.node = [position]
        self._dir = self.get_random_dir()
        self._head_set = None

    def get_random_dir(self):
        return random.randint(0, 3)
    
    def get_snake(self):
        return self.node

    def get_node(self, i):
        return self.node[i]
    
    def get_dir(self):
        return self._dir
    
    def get_head_image(self):
        return self._head_set

    def set_head(self, image):
        self._head_set = image

    def set_dir(self, key):
        self._dir = key

    def insert(self, index, pos):
        self.node.insert(index, pos)

    def pop(self):
        self.node.pop()

    def grow(self):
        self.node.append(self.node[-1])

    


