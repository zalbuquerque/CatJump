#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import LEVEL_TIME
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self):
        self.level_names = ['Level1', 'Level2']
        self.current_level_index = 0
        self.time_left = 0
        self.cars = []

    def reset(self):
        self.current_level_index = 0
        self.load()

    def load(self):
        level_name = self.get_level_name()
        self.time_left = LEVEL_TIME[level_name]
        self.cars = EntityFactory.create_cars(level_name)

    def next_level(self):
        self.current_level_index += 1

        if self.current_level_index >= len(self.level_names):
            return False

        self.load()
        return True

    def get_level_name(self):
        return self.level_names[self.current_level_index]

    def get_level_number(self):
        return self.current_level_index + 1
