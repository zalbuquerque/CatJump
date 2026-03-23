from __future__ import annotations

import pygame

from code.asset_loader import load_image
from code.const import GRAVITY, GROUND_Y, IMG_PLAYER, JUMP_STRENGTH, MAX_FALL_SPEED, PLAYER_SPEED, WIN_WIDTH
from code.entity import Entity


class Player(Entity):
    def __init__(self) -> None:
        rect = pygame.Rect(120, GROUND_Y - 72, 72, 72)
        super().__init__('Player', rect)
        self.velocity_y = 0.0
        self.on_ground = True
        self.sprite = load_image(IMG_PLAYER, (72, 72))

    def jump(self) -> None:
        if self.on_ground:
            self.velocity_y = JUMP_STRENGTH
            self.on_ground = False

    def update(self, pressed_keys: pygame.key.ScancodeWrapper | None = None) -> None:
        if pressed_keys:
            if pressed_keys[pygame.K_a] and self.rect.left > 0:
                self.rect.x -= PLAYER_SPEED
            if pressed_keys[pygame.K_d] and self.rect.right < WIN_WIDTH:
                self.rect.x += PLAYER_SPEED

        self.velocity_y += GRAVITY
        if self.velocity_y > MAX_FALL_SPEED:
            self.velocity_y = MAX_FALL_SPEED

        self.rect.y += int(self.velocity_y)

        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.velocity_y = 0
            self.on_ground = True

    def draw(self, surface: pygame.Surface) -> None:
        surface.blit(self.sprite, self.rect.topleft)
