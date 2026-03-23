#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame

from code.Const import (
    WIN_WIDTH,
    WIN_HEIGHT,
    GAME_TITLE,
    GAME_STATE,
    C_WHITE,
    C_RED,
    C_GREEN,
    C_YELLOW,
    MENU_OPTION,
    TOP_LIMIT,
    ASSET_SOUND
)
from code.AssetManager import AssetManager
from code.EntityFactory import EntityFactory
from code.CollisionManager import CollisionManager
from code.ScoreRepository import ScoreRepository
from code.Menu import Menu
from code.Background import Background
from code.Level import Level


class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        pygame.display.set_caption(GAME_TITLE)
        self.clock = pygame.time.Clock()

        self.background = Background()
        self.menu_sound = AssetManager.sound(ASSET_SOUND['Menu'])
        self.game_over_sound = AssetManager.sound(ASSET_SOUND['GameOver'])

        self.menu = Menu()
        self.repository = ScoreRepository()
        self.level = Level()

        self.big_font = pygame.font.SysFont('arial', 40, bold=True)
        self.medium_font = pygame.font.SysFont('arial', 28)

        self.state = GAME_STATE['Menu']
        self.menu_index = 0

        self.players = []
        self.cars = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()

        self.time_left = 0
        self.last_second_tick = pygame.time.get_ticks()
        self.players_count = 1

    def start_game(self, players_count):
        self.players_count = players_count
        self.players.clear()
        self.cars.empty()
        self.all_sprites.empty()

        if players_count >= 1:
            player1 = EntityFactory.create_player('Player1')
            self.players.append(player1)
            self.all_sprites.add(player1)

        if players_count == 2:
            player2 = EntityFactory.create_player('Player2')
            self.players.append(player2)
            self.all_sprites.add(player2)

        self.level.reset()
        self.load_level()
        self.state = GAME_STATE['Playing']

    def load_level(self):
        self.cars.empty()
        self.all_sprites.empty()

        for player in self.players:
            player.reset()
            self.all_sprites.add(player)

        self.time_left = self.level.time_left
        self.last_second_tick = pygame.time.get_ticks()

        for car in self.level.cars:
            self.cars.add(car)
            self.all_sprites.add(car)

    def save_current_score(self):
        mode = '1P' if self.players_count == 1 else '2P'
        level_number = self.level.get_level_number()
        self.repository.save_score(mode, level_number, max(0, int(self.time_left)))

    def update_timer(self):
        current_time = pygame.time.get_ticks()

        if current_time - self.last_second_tick >= 1000:
            self.time_left -= 1
            self.last_second_tick = current_time

            if self.time_left <= 0:
                self.game_over_sound.play()
                self.save_current_score()
                self.state = GAME_STATE['GameOver']

    def update_playing(self):
        keys = pygame.key.get_pressed()

        for player in self.players:
            player.update(keys)

        self.cars.update()
        self.update_timer()

        if self.state != GAME_STATE['Playing']:
            return

        for player in self.players:
            if CollisionManager.player_hit_car(player, self.cars):
                self.game_over_sound.play()
                self.save_current_score()
                self.state = GAME_STATE['GameOver']
                return

        for player in self.players:
            if CollisionManager.player_reached_top(player, TOP_LIMIT):
                advanced = self.level.next_level()

                if advanced:
                    self.load_level()
                else:
                    self.save_current_score()
                    self.state = GAME_STATE['Victory']
                return

    def draw_hud(self):
        level_text = self.medium_font.render(
            f'Level: {self.level.get_level_number()}',
            True,
            C_WHITE
        )
        time_text = self.medium_font.render(
            f'Tempo: {int(self.time_left)}',
            True,
            C_YELLOW
        )

        self.screen.blit(level_text, (20, 15))
        self.screen.blit(time_text, (650, 15))

    def draw_game_over(self):
        self.background.draw(self.screen)

        title = self.big_font.render('GAME OVER', True, C_RED)
        info1 = self.medium_font.render('ENTER - voltar ao menu', True, C_WHITE)
        info2 = self.medium_font.render('ESC - sair', True, C_WHITE)

        self.screen.blit(title, title.get_rect(center=(400, 220)))
        self.screen.blit(info1, info1.get_rect(center=(400, 300)))
        self.screen.blit(info2, info2.get_rect(center=(400, 350)))

    def draw_victory(self):
        self.background.draw(self.screen)

        title = self.big_font.render('VOCE VENCEU!', True, C_GREEN)
        info1 = self.medium_font.render('ENTER - voltar ao menu', True, C_WHITE)
        info2 = self.medium_font.render('ESC - sair', True, C_WHITE)

        self.screen.blit(title, title.get_rect(center=(400, 220)))
        self.screen.blit(info1, info1.get_rect(center=(400, 300)))
        self.screen.blit(info2, info2.get_rect(center=(400, 350)))

    def handle_menu_action(self):
        option = MENU_OPTION[self.menu_index]

        if option == 'NEW GAME 1P':
            self.menu_sound.play()
            self.start_game(1)

        elif option == 'NEW GAME 2P':
            self.menu_sound.play()
            self.start_game(2)

        elif option == 'SCORE':
            self.menu_sound.play()
            self.state = GAME_STATE['Score']

        elif option == 'EXIT':
            pygame.quit()
            sys.exit()

    def draw_score_screen(self):
        self.background.draw(self.screen)

        title = self.big_font.render('SCORE', True, C_GREEN)
        back = self.medium_font.render('ENTER ou ESC - voltar ao menu', True, C_WHITE)

        self.screen.blit(title, title.get_rect(center=(400, 100)))

        top_scores = self.repository.get_top_scores(10)
        y = 180

        for index, (mode, level, time_left) in enumerate(top_scores):
            line = self.medium_font.render(
                f'{index + 1}. {mode} | Level {level} | {time_left}s',
                True,
                C_WHITE
            )
            self.screen.blit(line, line.get_rect(center=(400, y)))
            y += 40

        self.screen.blit(back, back.get_rect(center=(400, 520)))

    def run(self):
        while True:
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if self.state == GAME_STATE['Menu']:
                        if event.key == pygame.K_UP:
                            self.menu_index = (self.menu_index - 1) % len(MENU_OPTION)
                        elif event.key == pygame.K_DOWN:
                            self.menu_index = (self.menu_index + 1) % len(MENU_OPTION)
                        elif event.key == pygame.K_RETURN:
                            self.handle_menu_action()

                    elif self.state == GAME_STATE['Score']:
                        if event.key in (pygame.K_RETURN, pygame.K_ESCAPE):
                            self.menu_sound.play()
                            self.state = GAME_STATE['Menu']

                    elif self.state == GAME_STATE['GameOver']:
                        if event.key == pygame.K_RETURN:
                            self.menu_sound.play()
                            self.state = GAME_STATE['Menu']
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

                    elif self.state == GAME_STATE['Victory']:
                        if event.key == pygame.K_RETURN:
                            self.menu_sound.play()
                            self.state = GAME_STATE['Menu']
                        elif event.key == pygame.K_ESCAPE:
                            pygame.quit()
                            sys.exit()

            if self.state == GAME_STATE['Menu']:
                self.background.draw(self.screen)
                self.menu.draw(self.screen, self.menu_index, self.repository.get_top_scores(3))

            elif self.state == GAME_STATE['Playing']:
                self.update_playing()
                self.background.draw(self.screen)
                self.all_sprites.draw(self.screen)
                self.draw_hud()

            elif self.state == GAME_STATE['GameOver']:
                self.draw_game_over()

            elif self.state == GAME_STATE['Score']:
                self.draw_score_screen()

            elif self.state == GAME_STATE['Victory']:
                self.draw_victory()

            pygame.display.flip()

