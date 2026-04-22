import random
import settings

class Snake:

    def __init__(self, position):
        self._nods = [position]
        self._dir = self.get_random_dir()
        self._head_set = None

    def get_random_dir(self):
        return random.randint(0, 3)
    
    def get_snake(self):
        return self._nods

    def get_nod(self, i):
        return self._nods[i]
    
    def get_dir(self):
        return self._dir
    
    def get_head_image(self):
        return self._head_set

    def set_head(self, image):
        self._head_set = image

    def set_dir(self, key):
        self._dir = key

    def insert(self, index, pos):
        self._nods.insert(index, pos)

    def pop(self):
        self._nods.pop()

    def grow(self):
        self._nods.append(self._nods[-1])

    


