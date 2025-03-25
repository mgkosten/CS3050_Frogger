from constants import *
import arcade

class Log:
    def __init__(self, length, direction, xpos, ypos):
        self.length = length
        self.speed = direction * OBSTACLE_SPEED
        self.xpos = xpos
        self.ypos = ypos
        self.sprite = arcade.SpriteList()

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

    def load_textures(self, spritesheet):
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

