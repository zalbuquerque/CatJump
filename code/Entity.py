#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod
import pygame


class Entity(pygame.sprite.Sprite, ABC):
    def __init__(self, x, y, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(topleft=(x, y))

    @abstractmethod
    def update(self, *args, **kwargs):
        pass