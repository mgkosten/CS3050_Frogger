import arcade
from constants import *

class Turt:
    def __init__(self, length, xpos, ypos):
        self.speed = OBSTACLE_SPEED
        self.length = length
        self.xpos = xpos
        self.ypos = ypos
        self.sprite = arcade.SpriteList()

    def load_textures(self, spritesheet):
        '''Loads interactive textures for the turtles
           from the spritesheet into the textures dictionary'''
        # pylint: disable=unused-variable

        x = self.xpos
        y = self.ypos
        turtle_1 = spritesheet.get_texture(
            arcade.LBWH(1, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        turtle_2 = spritesheet.get_texture(
            arcade.LBWH(19, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        turtle_3 = spritesheet.get_texture(
            arcade.LBWH(37, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        turtle_disappear_1 = spritesheet.get_texture(
            arcade.LBWH(55, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        turtle_disappear_2 = spritesheet.get_texture(
            arcade.LBWH(73, 152, SPRITE_SQUARE, SPRITE_SQUARE))

        # The textures other than 'turtle_2' above are used for swimming animation,
        # not for drawing the bigger group like with logs
        for _ in range(self.length):
            self.sprite.append(arcade.Sprite(turtle_2, SCALE, x, y))
            x += SCALED_SQUARE

    def update(self, delta_time):
        self.xpos += self.speed * delta_time
        if self.xpos > WINDOW_WIDTH and self.speed > 0:
            self.xpos = 0
        elif self.xpos < 0 and self.speed < 0:
            self.xpos = WINDOW_WIDTH

        x = self.xpos
        for sprite in self.sprite:
            sprite.center_x = x
            x += SCALED_SQUARE
