from constants import *
import arcade

class Car:
    def __init__(self, car_type, direction, xpos, ypos):
        self.speed = OBSTACLE_SPEED * direction
        self.car_type = car_type
        self.xpos = xpos
        self.ypos = ypos
        self.sprite = None

    def update(self, delta_time):
        self.xpos += self.speed * delta_time
        if self.xpos > WINDOW_WIDTH and self.speed > 0:
            self.xpos = 0
        elif self.xpos < 0 and self.speed < 0:
            self.xpos = WINDOW_WIDTH

        self.sprite.center_x = self.xpos

    def load_textures(self, spritesheet):
        match self.car_type:
            case 1:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(19, 116, SPRITE_SQUARE, SPRITE_SQUARE))
                # y = SCALED_SQUARE * 2.5
            case 2:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(55, 116, SPRITE_SQUARE, SPRITE_SQUARE))
                # y = SCALED_SQUARE * 3.5
            case 3:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(1, 116, SPRITE_SQUARE, SPRITE_SQUARE))
                # y = SCALED_SQUARE * 4.5
            case 4:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(37, 116, SPRITE_SQUARE, SPRITE_SQUARE))
                # y = SCALED_SQUARE * 5.5
            case 5:
                vehicle_texture = spritesheet.get_texture(
                    arcade.LBWH(73, 116, SPRITE_SQUARE * 2, SPRITE_SQUARE))
                # y = SCALED_SQUARE * 6.5
            case _:
                raise Exception('invalid car type:', self.car_type)

        # TODO: I think we might not need a ypos for Car and we can just set the y for the Sprite based on car_type
        self.sprite = arcade.Sprite(vehicle_texture, SCALE, self.xpos, self.ypos)

    def car_movement(self):
        pass


