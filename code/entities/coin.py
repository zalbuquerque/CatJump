from __future__ import annotations

import random
import pygame

from code.asset_loader import load_image
from code.const import GROUND_Y, IMG_COIN, SCROLL_SPEED, WIN_WIDTH
from code.entity import Entity


class Coin(Entity):
    def __init__(self) -> None:
        y = random.choice((GROUND_Y - 50, GROUND_Y - 110, GROUND_Y - 160))
        rect = pygame.Rect(WIN_WIDTH + random.randint(50, 150), y, 28, 28)
        super().__init__('Coin', rect)
        self.sprite = load_image(IMG_COIN, (28, 28))

    def update(self) -> None:
        self.rect.x -= SCROLL_SPEED
        if self.rect.right < 0:
            self.alive = False

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.sprite, self.rect.topleft)
