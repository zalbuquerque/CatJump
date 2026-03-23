from pathlib import Path
import pygame

# Janela
WIN_WIDTH = 960
WIN_HEIGHT = 540
FPS = 60
GROUND_Y = 430

# Física
GRAVITY = 0.9
JUMP_STRENGTH = -17
PLAYER_SPEED = 6
SCROLL_SPEED = 7
MAX_FALL_SPEED = 20

# Evento
EVENT_SPAWN_OBSTACLE = pygame.USEREVENT + 1
EVENT_SPAWN_COIN = pygame.USEREVENT + 2
EVENT_SCORE_TICK = pygame.USEREVENT + 3

OBSTACLE_SPAWN_MS = 1450
COIN_SPAWN_MS = 2100
SCORE_TICK_MS = 200

# Fonte
FONT_NAME = "arial"
GAME_TITLE = "Jump Trail"

# Cores de apoio
C_TEXT = (31, 35, 48)
C_TEXT_LIGHT = (250, 250, 250)
C_PANEL = (255, 255, 255)
C_PANEL_BORDER = (200, 210, 225)
C_SHADOW = (0, 0, 0, 90)

# Paths
ROOT_DIR = Path(__file__).resolve().parent.parent
ASSET_DIR = ROOT_DIR / "assets"
IMAGE_DIR = ASSET_DIR / "images"

IMG_BG = IMAGE_DIR / "background.png"
IMG_PLAYER = IMAGE_DIR / "player.png"
IMG_OBSTACLE = IMAGE_DIR / "obstacle.png"
IMG_COIN = IMAGE_DIR / "coin.png"
