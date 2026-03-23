import pygame


class CollisionManager:
    @staticmethod
    def player_hit_car(player, cars):
        return pygame.sprite.spritecollide(player, cars, False)

    @staticmethod
    def player_reached_top(player, top_limit):
        return player.rect.top <= top_limit