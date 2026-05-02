import random
import settings

class Snake:

    def __init__(self, position):
        self._nodes = [position]
        self._dir = self.get_random_dir()
        self._head_set = None

    def get_random_dir(self):
        return random.randint(0, 3)
    
    def get_snake(self):
        return self._nodes

    def get_node(self, i):
        return self._nodes[i]
    
    def get_dir(self):
        return self._dir
    
    def get_head_image(self):
        return self._head_set

    def set_head(self, image):
        self._head_set = image

    def set_dir(self, key):
        self._dir = key

    def insert(self, index, pos):
        self._nodes.insert(index, pos)

    def pop(self):
        self._nodes.pop()


    


