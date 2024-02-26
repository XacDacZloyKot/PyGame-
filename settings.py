import pygame
from pathlib import Path
import sys, os

pygame.init()

# Scale model
SCALE_HERO = 5
SCALE_ENEMY = 4

BULLET_COUNT = 5
BULLET_SPEED = 5

TOTAL_KILL = 10

BACKGROUND = pygame.image.load('resources/img/background.jpg')

# Fonts
BASE_DIR = Path(__file__).resolve().parent
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
PATH_FONT = 'resources/fonts/Ubuntu-Medium.ttf'
FONT_LARGE = pygame.font.Font(PATH_FONT, 48)
FONT_NORMAL = pygame.font.Font(PATH_FONT, 24)

# Main settings
clock = pygame.time.Clock()
WINDOW_W = 1280
WINDOW_H = 720
FPS = 60

# Color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (197, 153, 114)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (255, 0, 145)

# Input field
COLOR_INACTIVE = (0, 0, 0)
COLOR_ACTIVE = (255, 255, 255)

