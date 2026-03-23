import pygame
from code.Const import (
    C_WHITE,
    C_LIGHT_GRAY,
    C_GREEN,
    MENU_OPTION,
    SCORE_POS
)


class Menu:
    def __init__(self):
        self.title_font = pygame.font.SysFont('arial', 44, bold=True)
        self.text_font = pygame.font.SysFont('arial', 28)
        self.small_font = pygame.font.SysFont('arial', 22)

    def draw(self, screen, selected_option, top_scores):
        title = self.title_font.render('TRAVESSIA URBANA', True, C_WHITE)
        subtitle = self.text_font.render('Demo 2D em Python', True, C_LIGHT_GRAY)

        screen.blit(title, title.get_rect(center=SCORE_POS['Title']))
        screen.blit(subtitle, subtitle.get_rect(center=SCORE_POS['Subtitle']))

        for index, option in enumerate(MENU_OPTION):
            color = C_GREEN if index == selected_option else C_WHITE
            text = self.text_font.render(option, True, color)
            screen.blit(text, text.get_rect(center=SCORE_POS[index]))

        controls1 = self.small_font.render('P1: W A S D', True, C_LIGHT_GRAY)
        controls2 = self.small_font.render('P2: SETAS', True, C_LIGHT_GRAY)
        controls3 = self.small_font.render('ENTER: selecionar  |  ESC: voltar', True, C_LIGHT_GRAY)

        screen.blit(controls1, controls1.get_rect(center=(400, 420)))
        screen.blit(controls2, controls2.get_rect(center=(400, 450)))
        screen.blit(controls3, controls3.get_rect(center=(400, 480)))

        record_title = self.small_font.render('TOP SCORES', True, C_GREEN)
        screen.blit(record_title, record_title.get_rect(center=(400, 525)))

        x = 160
        y = 550
        for mode, level, time_left in top_scores[:3]:
            record_text = self.small_font.render(
                f'{mode} | Level {level} | {time_left}s',
                True,
                C_WHITE
            )
            screen.blit(record_text, (x, y))
            y += 25