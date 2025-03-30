'''Turt class - named turt instead of turtle to avoid conflict with built-in class'''
# pylint: disable=wildcard-import, unused-wildcard-import
import arcade
from constants import *

class Turt:
    '''
    Class representing a group of turtles in the water
        length: number of turtles in the group
        xpos: center x position of leftmost turtle
        ypos: center y position of the turtle group
    '''
    def __init__(self, length, xpos, ypos):
        self.speed = -OBSTACLE_SPEED
        self.length = length
        self.xpos = xpos
        self.ypos = ypos
        self.sprite_list = arcade.SpriteList()

    def load_textures(self, spritesheet):
        '''Load turtle textures and sprites'''
        x = self.xpos
        y = self.ypos
        turtle_texture = spritesheet.get_texture(
            arcade.LBWH(19, 152, SPRITE_SQUARE, SPRITE_SQUARE))

        for _ in range(self.length):
            self.sprite_list.append(arcade.Sprite(turtle_texture, SCALE, x, y))
            x += SCALED_SQUARE

    def update(self, delta_time):
        '''Call in on_update to move the turtle group'''
        self.xpos += self.speed * delta_time
        if self.xpos < -SCALED_SQUARE * self.length:
            self.xpos = WINDOW_WIDTH + SCALED_SQUARE/2

        x = self.xpos
        for sprite in self.sprite_list:
            sprite.center_x = x
            x += SCALED_SQUARE
