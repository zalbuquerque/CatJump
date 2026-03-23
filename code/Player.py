#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Entity import Entity
from code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    ENTITY_SPEED,
    PLAYER_KEY_UP,
    PLAYER_KEY_DOWN,
    PLAYER_KEY_LEFT,
    PLAYER_KEY_RIGHT
)


class Player(Entity):
    def __init__(self, name, image, start_pos):
        super().__init__(start_pos[0], start_pos[1], image)
        self.name = name
        self.speed = ENTITY_SPEED[name]
        self.start_pos = start_pos

    def reset(self):
        self.rect.topleft = self.start_pos

    def update(self, keys):
        if keys[PLAYER_KEY_LEFT[self.name]]:
            self.rect.x -= self.speed
        if keys[PLAYER_KEY_RIGHT[self.name]]:
            self.rect.x += self.speed
        if keys[PLAYER_KEY_UP[self.name]]:
            self.rect.y -= self.speed
        if keys[PLAYER_KEY_DOWN[self.name]]:
            self.rect.y += self.speed

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT