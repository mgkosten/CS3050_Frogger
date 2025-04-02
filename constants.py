'''File to hold constants, import as needed'''
from enum import Enum

# Scale needs to be an integer so for loops work but change as needed locally
SCALE = 2
SPRITE_SQUARE = 16
SCALED_SQUARE = SPRITE_SQUARE*SCALE

WINDOW_WIDTH = 28*8*SCALE
WINDOW_HEIGHT = 32*8*SCALE
WINDOW_TITLE = "Frogger"

DURATION = 60
OBSTACLE_SPEED = WINDOW_WIDTH/9

class LogType(Enum):
    SHORT = 0
    MEDIUM = 1
    LONG = 2
