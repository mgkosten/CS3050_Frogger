'''File to hold constants, import as needed'''
import sys
from enum import Enum
from pyglet.math import Vec2

FILTER_ON = True
match sys.platform:
    case 'win32':
        # Windows
        import ctypes
        DISPLAY_SCALE = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100
    case 'darwin':
        # Mac
        from AppKit import NSScreen
        DISPLAY_SCALE = NSScreen.mainScreen().backingScaleFactor()
    case _:
        # Turn off filter for other OS until figure out display scaling
        DISPLAY_SCALE = 1
        FILTER_ON = False

SCALE = 3.5/DISPLAY_SCALE
SPRITE_SQUARE = 16
SCALED_SQUARE = int(SPRITE_SQUARE*SCALE)
WINDOW_WIDTH = int(28*8*SCALE)
WINDOW_HEIGHT = int(32*8*SCALE)
WINDOW_TITLE = "Frogger"

# The CRT filter doesn't respect native display scales so we have to hack it a little bit
FILTER_WIDTH = int(WINDOW_WIDTH*DISPLAY_SCALE)
FILTER_HEIGHT = int(WINDOW_HEIGHT*DISPLAY_SCALE)

# CRT CONSTANTS
DSCALE = 6
SCAN = -8
PIX = -3
WARP = Vec2(1.0 / 32.0, 1.0 / 24.0)
DARKMASK = .5
LIGHTMASK = 1.5

DURATION = 60
OBSTACLE_SPEED = WINDOW_WIDTH/15

class LogType(Enum):
    '''LogType enum to represent short, medium, and long logs'''
    SHORT = 0
    MEDIUM = 1
    LONG = 2
