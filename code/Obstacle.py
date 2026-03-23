from abc import abstractmethod
from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image)
        self.speed = speed

    @abstractmethod
    def move(self):
        pass

    def update(self, *args, **kwargs):
        self.move()