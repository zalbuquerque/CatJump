import os
import pygame

# C
C_WHITE = (255, 255, 255)
C_BLACK = (0, 0, 0)
C_RED = (220, 70, 70)
C_GREEN = (60, 180, 75)
C_LIGHT_GRAY = (180, 180, 180)
C_YELLOW = (255, 220, 0)

# E
EVENT_CAR = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Player1': 5,
    'Player2': 5,
    'CarLevel1': 3,
    'CarLevel2': 5,
}

# G
GAME_TITLE = 'Travessia Urbana'

GAME_STATE = {
    'Menu': 'menu',
    'Playing': 'playing',
    'GameOver': 'game_over',
    'Score': 'score',
    'Victory': 'victory'
}

# L
LEVEL_TIME = {
    'Level1': 20,
    'Level2': 12,
}

LEVEL_CAR_SPEED = {
    'Level1': 3,
    'Level2': 5,
}

LEVEL_CAR_COUNT = {
    'Level1': 6,
    'Level2': 8,
}

LANE_Y = (
    120,
    190,
    260,
    330,
    400,
    470
)

# M
MENU_OPTION = (
    'NEW GAME 1P',
    'NEW GAME 2P',
    'SCORE',
    'EXIT'
)

# P
PLAYER_SIZE = {
    'Player1': (40, 40),
    'Player2': (40, 40),
}

PLAYER_START_POS = {
    'Player1': (220, 520),
    'Player2': (520, 520),
}

PLAYER_KEY_UP = {
    'Player1': pygame.K_w,
    'Player2': pygame.K_UP
}

PLAYER_KEY_DOWN = {
    'Player1': pygame.K_s,
    'Player2': pygame.K_DOWN
}

PLAYER_KEY_LEFT = {
    'Player1': pygame.K_a,
    'Player2': pygame.K_LEFT
}

PLAYER_KEY_RIGHT = {
    'Player1': pygame.K_d,
    'Player2': pygame.K_RIGHT
}

PLAYER_LABEL = {
    'Player1': 'P1',
    'Player2': 'P2'
}

# S
SPAWN_TIME = {
    'Level1': 2500,
    'Level2': 1800,
}

SCORE_POS = {
    'Title': (400, 90),
    'Subtitle': (400, 140),
    'Controls': (400, 420),
    'Record': (400, 520),
    0: (400, 180),
    1: (400, 230),
    2: (400, 280),
    3: (400, 330),
}

# T
TIMEOUT_STEP = 1000
TOP_LIMIT = 50

# W
WIN_WIDTH = 800
WIN_HEIGHT = 600

# A
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSET_DIR = os.path.join(BASE_DIR, 'asset')

ASSET_BACKGROUND = os.path.join(ASSET_DIR, 'background', 'city_background.png')

ASSET_PLAYER = {
    'Player1': os.path.join(ASSET_DIR, 'player', 'cat1.png'),
    'Player2': os.path.join(ASSET_DIR, 'player', 'cat2.png'),
}

ASSET_CAR = (
    os.path.join(ASSET_DIR, 'cars', 'car_red.png'),
    os.path.join(ASSET_DIR, 'cars', 'car_blue.png'),
    os.path.join(ASSET_DIR, 'cars', 'car_green.png'),
)

ASSET_SOUND = {
    'Menu': os.path.join(ASSET_DIR, 'sounds', 'menu.wav'),
    'GameOver': os.path.join(ASSET_DIR, 'sounds', 'game_over.wav'),
}

# R
ROAD_LIMITS = {
    'TopSafe': 60,
    'BottomSafe': 80
}