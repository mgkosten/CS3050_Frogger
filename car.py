'''Car class'''
# pylint: disable=wildcard-import, unused-wildcard-import
import arcade
from constants import *

class Car:
    '''
    Class for cars in the road
        car_type: which sprite to show (integer 1-5)
        direction: -1 for moving right to left, 1 for left to right
        xpos: center x position of car
        ypos: center y position of car
    '''
    def __init__(self, car_type, direction, xpos, ypos):
        self.speed = OBSTACLE_SPEED * direction
        self.car_type = car_type
        self.xpos = xpos
        self.ypos = ypos
        self.sprite = None

    def load_textures(self, spritesheet):
        '''Load turtle textures and sprites'''
        match self.car_type:
            case 1:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(19, 116, SPRITE_SQUARE, SPRITE_SQUARE))
            case 2:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(55, 116, SPRITE_SQUARE, SPRITE_SQUARE))
            case 3:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(1, 116, SPRITE_SQUARE, SPRITE_SQUARE))
            case 4:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(37, 116, SPRITE_SQUARE, SPRITE_SQUARE))
            case 5:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(73, 116, SPRITE_SQUARE * 2, SPRITE_SQUARE))
            case _:
                raise ValueError('invalid car type, must be integer 1-5')

        self.sprite = arcade.Sprite(vehicle_texture, SCALE, self.xpos, self.ypos)

    def update(self, delta_time):
        '''Call in on_update to move the car'''
        self.xpos += (self.speed + ((self.car_type-5)*5)) * delta_time
        if self.xpos > WINDOW_WIDTH + 25 and self.speed > 0:
            self.xpos = -25
        elif self.xpos < -25 and self.speed < 0:
            self.xpos = WINDOW_WIDTH + 25

        self.sprite.center_x = self.xpos
