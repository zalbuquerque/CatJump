#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame

from code.Player import Player
from code.Car import Car
from code.AssetManager import AssetManager
from code.Const import (
    ASSET_PLAYER,
    ASSET_CAR,
    PLAYER_SIZE,
    PLAYER_START_POS,
    LEVEL_CAR_SPEED,
    LEVEL_CAR_COUNT,
    LANE_Y
)


class EntityFactory:
    @staticmethod
    def create_player(player_name):
        image = AssetManager.image(
            ASSET_PLAYER[player_name],
            PLAYER_SIZE[player_name]
        )
        return Player(player_name, image, PLAYER_START_POS[player_name])

    @staticmethod
    def create_cars(level_name):
        cars = []
        car_speed = LEVEL_CAR_SPEED[level_name]
        car_count = LEVEL_CAR_COUNT[level_name]

        for index in range(car_count):
            lane_y = LANE_Y[index % len(LANE_Y)]
            image = AssetManager.image(random.choice(ASSET_CAR), (70, 38))

            x = random.randint(0, 700)

            if index % 2 == 0:
                speed = car_speed
            else:
                speed = -car_speed
                image = pygame.transform.flip(image, True, False)

            cars.append(Car(x, lane_y, image, speed))

        return cars


