import arcade
from constants import *
from enum import Enum

class Directions(Enum):
    left = 1
    right = 2
    up = 3
    down = 4

class Frog:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.lives = 3
        self.sprite = None
        self.direction = Directions.up

    def load_textures(self, spritesheet):
        frog_up = spritesheet.get_texture(
            arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))

        self.sprite = arcade.Sprite(frog_up, SCALE, self.xpos, self.ypos)

    # Resets game
    def reset(self):
        '''Reset frog's position'''
        # TODO: write this function which resets the frog to start position
        # I think this would be called from the GameView class when the frog dies

    def move(self, key):
        '''Move the frog on key press'''
        # TODO: call this function in on_key_press
        # TODO: Add way to move frog when key is held down: timer or something
        # TODO: show a different sprite based on which direction it's facing

        frog = self.sprite
        if key == arcade.key.UP:
            frog.center_y += SCALED_SQUARE
        elif key == arcade.key.DOWN:
            frog.center_y -= SCALED_SQUARE
        elif key == arcade.key.LEFT:
            frog.center_x -= SCALED_SQUARE
        elif key == arcade.key.RIGHT:
            frog.center_x += SCALED_SQUARE

        frog_x = frog.center_x
        frog_y = frog.center_y

        # check boundaries of frogs position (ensure not go offscreen)
        # horizontal boundary check
        if frog_x > WINDOW_WIDTH - SCALED_SQUARE / 2:
            frog.center_x = WINDOW_WIDTH - SCALED_SQUARE / 2
        elif frog_x < SCALED_SQUARE / 2:
            frog.center_x = SCALED_SQUARE / 2

        # vertical boundary check
        if frog_y > WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2:
            frog.center_y = WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2
        if frog_y < SCALED_SQUARE / 2 + SCALED_SQUARE:
            frog.center_y = SCALED_SQUARE / 2 + SCALED_SQUARE
