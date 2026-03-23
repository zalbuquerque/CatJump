#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.AssetManager import AssetManager
from code.Const import ASSET_BACKGROUND, WIN_WIDTH, WIN_HEIGHT


class Background:
    def __init__(self):
        self.image = AssetManager.image(ASSET_BACKGROUND, (WIN_WIDTH, WIN_HEIGHT))

    def draw(self, screen):
        screen.blit(self.image, (0, 0))