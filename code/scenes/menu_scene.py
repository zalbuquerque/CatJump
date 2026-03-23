from __future__ import annotations

import pygame

from code.asset_loader import load_image
from code.const import IMG_BG, WIN_HEIGHT, WIN_WIDTH
from code.menu import Menu
from code.scenes.base_scene import BaseScene


class MenuScene(BaseScene):
    def __init__(self, game) -> None:
        super().__init__(game)
        self.menu = Menu()
        self.background = load_image(IMG_BG, (WIN_WIDTH, WIN_HEIGHT), alpha=False)

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                from code.scenes.game_scene import GameScene

                self.next_scene = GameScene(self.game)
            elif event.key == pygame.K_ESCAPE:
                self.game.running = False

    def update(self) -> None:
        self.menu.update()

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.background, (0, 0))
        self.menu.draw(screen, self.game.best_score)
