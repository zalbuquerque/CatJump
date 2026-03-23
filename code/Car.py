from code.Obstacle import Obstacle
from code.Const import WIN_WIDTH


class Car(Obstacle):
    def __init__(self, x, y, image, speed):
        super().__init__(x, y, image, speed)

    def move(self):
        self.rect.x += self.speed

        if self.speed > 0 and self.rect.left > WIN_WIDTH:
            self.rect.right = 0
        elif self.speed < 0 and self.rect.right < 0:
            self.rect.left = WIN_WIDTH