'''Log class'''
# pylint: disable=wildcard-import, unused-wildcard-import
import arcade
from constants import *

class Log:
    '''
    Class for logs in the water
        length: width of the log in number of squares (at least 2)
        xpos: center x position of leftmost log sprite
        ypos: center y position of the log
    '''
    def __init__(self, length, xpos, ypos):
        self.length = length
        self.speed = OBSTACLE_SPEED
        self.xpos = xpos
        self.ypos = ypos
        self.sprite = arcade.SpriteList()

    def load_textures(self, spritesheet):
        '''Load log textures and sprites'''
        x = self.xpos
        y = self.ypos
        left_log = spritesheet.get_texture(arcade.LBWH(1, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        mid_log = spritesheet.get_texture(arcade.LBWH(19, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        right_log = spritesheet.get_texture(arcade.LBWH(37, 134, SPRITE_SQUARE, SPRITE_SQUARE))

        self.sprite.append(arcade.Sprite(left_log, SCALE, x, y))
        x += SCALED_SQUARE
        for _ in range(self.length - 2):
            self.sprite.append(arcade.Sprite(mid_log, SCALE, x, y))
            x += SCALED_SQUARE
        self.sprite.append(arcade.Sprite(right_log, SCALE, x, y))

    def update(self, delta_time):
        '''Call in on_update to move the log'''
        self.xpos += (self.speed - self.length*5)* delta_time
        if self.xpos > WINDOW_WIDTH and self.speed > 0:
            self.xpos = -200
        elif self.xpos < 0 and self.speed < 0:
            self.xpos = WINDOW_WIDTH

        x = self.xpos
        for sprite in self.sprite:
            sprite.center_x = x
            x += SCALED_SQUARE
