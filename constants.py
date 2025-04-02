'''File to hold constants, import as needed'''
from pyglet.math import Vec2

# Scale needs to be an integer so for loops work but change as needed locally
SCALE = 2
SPRITE_SQUARE = 16
SCALED_SQUARE = SPRITE_SQUARE*SCALE
OBSTACLE_SPEED = 55

WINDOW_WIDTH = 28*8*SCALE
WINDOW_HEIGHT = 32*8*SCALE
WINDOW_TITLE = "Frogger"



# CRT CONSTANTS
DSCALE = 6
SCAN = -8
PIX = -3
WARP = Vec2(1.0 / 32.0, 1.0 / 24.0)
DARKMASK = .5
LIGHTMASK = 1.5
