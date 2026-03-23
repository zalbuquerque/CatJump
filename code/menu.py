from __future__ import annotations

import pygame

from code.const import C_PANEL, C_PANEL_BORDER, C_TEXT, C_TEXT_LIGHT, FONT_NAME, GAME_TITLE, WIN_WIDTH


class Menu:
    def __init__(self) -> None:
        self.title_font = pygame.font.SysFont(FONT_NAME, 58, bold=True)
        self.text_font = pygame.font.SysFont(FONT_NAME, 28)
        self.small_font = pygame.font.SysFont(FONT_NAME, 22)
        self.blink = 0

    def update(self) -> None:
        self.blink = (self.blink + 1) % 60

    def draw(self, screen: pygame.Surface, best_score: int) -> None:
        title = self.title_font.render(GAME_TITLE, True, C_TEXT)
        title_rect = title.get_rect(center=(WIN_WIDTH // 2, 90))
        screen.blit(title, title_rect)

        subtitle = self.text_font.render('Demo jogável 2D com sprites', True, C_TEXT)
        screen.blit(subtitle, subtitle.get_rect(center=(WIN_WIDTH // 2, 145)))

        panel = pygame.Rect(165, 190, 630, 235)
        shadow = panel.move(8, 8)
        shadow_surf = pygame.Surface((shadow.width, shadow.height), pygame.SRCALPHA)
        pygame.draw.rect(shadow_surf, (0, 0, 0, 70), shadow_surf.get_rect(), border_radius=20)
        screen.blit(shadow_surf, shadow.topleft)
        pygame.draw.rect(screen, C_PANEL, panel, border_radius=20)
        pygame.draw.rect(screen, C_PANEL_BORDER, panel, width=2, border_radius=20)

        lines = [
            'Controles:',
            'ENTER - Iniciar jogo',
            'SPACE / W / SETA PARA CIMA - Pular',
            'A e D - Mover para esquerda e direita',
            'ESC - Sair',
            'Objetivo: desviar dos obstáculos e coletar moedas.',
            f'Recorde da sessão: {best_score}',
        ]

        for index, text in enumerate(lines):
            surf = self.small_font.render(text, True, C_TEXT)
            screen.blit(surf, (200, 220 + index * 28))

        if self.blink < 30:
            prompt = self.text_font.render('Pressione ENTER para jogar', True, C_TEXT_LIGHT)
            prompt_bg = pygame.Rect(305, 450, 350, 46)
            pygame.draw.rect(screen, C_TEXT, prompt_bg, border_radius=14)
            screen.blit(prompt, prompt.get_rect(center=prompt_bg.center))
