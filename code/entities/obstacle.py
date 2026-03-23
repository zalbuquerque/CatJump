from __future__ import annotations

import random
import pygame

from code.asset_loader import load_image
from code.const import GROUND_Y, IMG_OBSTACLE, SCROLL_SPEED, WIN_WIDTH
from code.entity import Entity


class Obstacle(Entity):
    def __init__(self) -> None:
        width = random.choice((42, 52, 58))
        height = random.choice((52, 70, 84))
        rect = pygame.Rect(WIN_WIDTH + random.randint(0, 100), GROUND_Y - height, width, height)
        super().__init__('Obstacle', rect)
        self.sprite = load_image(IMG_OBSTACLE, (width, height))

    def update(self) -> None:
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.alive = False

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.sprite, self.rect.topleft)
