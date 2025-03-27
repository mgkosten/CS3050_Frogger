import arcade
from constants import *
from enum import Enum

class Directions(Enum):
    left = 1
    right = 2
    up = 3
    down = 4

class Frog:
    def __init__(self):
        self.xpos = WINDOW_WIDTH/2
        self.ypos = SCALED_SQUARE*1.5
        self.lives = 3
        self.sprite = None
        self.direction = Directions.up

    def load_textures(self, spritesheet):
        '''Load frog texture and sprite'''
        frog_up = spritesheet.get_texture(
            arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))

        self.sprite = arcade.Sprite(frog_up, SCALE, self.xpos, self.ypos)

    def update(self):
        self.sprite.center_x = self.xpos
        self.sprite.center_y = self.ypos

    def move(self, key):
        '''Move the frog on key press'''
        # TODO: Add way to move frog when key is held down: timer or something
        # TODO: show a different sprite based on which direction it's facing

        if key in [arcade.key.UP, arcade.key.W]:
            self.ypos += SCALED_SQUARE
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.ypos -= SCALED_SQUARE
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.xpos -= SCALED_SQUARE
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.xpos += SCALED_SQUARE

        # check boundaries of frogs position (ensure not go offscreen)
        # horizontal boundary check
        if self.xpos > WINDOW_WIDTH - SCALED_SQUARE / 2:
            self.xpos = WINDOW_WIDTH - SCALED_SQUARE / 2
        elif self.xpos < SCALED_SQUARE / 2:
            self.xpos = SCALED_SQUARE / 2

        # vertical boundary check
        if self.ypos > WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2:
            self.ypos = WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2
        elif self.ypos < SCALED_SQUARE / 2 + SCALED_SQUARE:
            self.ypos = SCALED_SQUARE / 2 + SCALED_SQUARE

    # Resets game
    def death(self):
        '''Call when the player frog dies'''
        self.lives -= 1

        # Reset to starting position
        self.xpos = WINDOW_WIDTH/2
        self.ypos = SCALED_SQUARE*1.5