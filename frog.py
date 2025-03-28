'''Frog class'''
# pylint: disable=wildcard-import, unused-wildcard-import
import arcade
from constants import *

class Frog:
    '''Frog class for the player character'''
    def __init__(self):
        self.xpos = WINDOW_WIDTH/2
        self.ypos = SCALED_SQUARE*1.5
        self.lives = 3
        self.sprite = None
        self.textures = {}

    def load_textures(self, spritesheet):
        '''Load frog texture and sprite'''
        self.textures['frog_up'] = spritesheet.get_texture(
            arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_left'] = spritesheet.get_texture(
            arcade.LBWH(37, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_down'] = spritesheet.get_texture(
            arcade.LBWH(73, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_right'] = spritesheet.get_texture(
            arcade.LBWH(109, 1, SPRITE_SQUARE, SPRITE_SQUARE))

        self.sprite = arcade.Sprite(self.textures['frog_up'], SCALE, self.xpos, self.ypos)

    def update(self):
        '''Call in on_update to keep the sprite position updated'''
        self.sprite.center_x = self.xpos
        self.sprite.center_y = self.ypos

    def move(self, key):
        '''Move the frog on key press and change the sprite texture'''
        if key in [arcade.key.UP, arcade.key.W]:
            self.ypos += SCALED_SQUARE
            self.sprite.texture = self.textures['frog_up']
        elif key in [arcade.key.DOWN, arcade.key.S]:
            self.ypos -= SCALED_SQUARE
            self.sprite.texture = self.textures['frog_down']
        elif key in [arcade.key.LEFT, arcade.key.A]:
            self.xpos -= SCALED_SQUARE
            self.sprite.texture = self.textures['frog_left']
        elif key in [arcade.key.RIGHT, arcade.key.D]:
            self.xpos += SCALED_SQUARE
            self.sprite.texture = self.textures['frog_right']

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

    def death(self):
        '''Call when the player frog dies to decrement lives and reset position'''
        self.lives -= 1

        # Reset to starting position
        self.xpos = WINDOW_WIDTH/2
        self.ypos = SCALED_SQUARE*1.5
