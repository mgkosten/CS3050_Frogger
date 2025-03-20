import constants
import arcade
from constants import SPRITE_SQUARE
self.car.car
class Car:
    def __init__(self):
        self.car_1_sprites = None
        self.car_2_sprites = None
        self.car_3_sprites = None
        self.car_4_sprites = None

        self.speed = OBSTACLE_SPEED

    def load_textures(self, spritesheet):
        self.textures['car_1'] = spritesheet.get_texture(
            arcade.LBWH(19, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['car_2'] = spritesheet.get_texture(
            arcade.LBWH(55, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['car_3'] = spritesheet.get_texture(
            arcade.LBWH(1, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['car_4'] = spritesheet.get_texture(
            arcade.LBWH(37, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['truck'] = spritesheet.get_texture(
            arcade.LBWH(73, 116, SPRITE_SQUARE*2, SPRITE_SQUARE))

    def create_cars(self):
        self.frog_sprites = arcade.SpriteList()
        y = SCALED_SQUARE*1.5
        self.frog_sprites.append(arcade.Sprite(self.textures['frog_up'], SCALE, WINDOW_WIDTH/2, y))
        # Car/Truck examples - ordered by rows of highway
        self.car_1_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_1_sprites.append(arcade.Sprite(self.textures['car_1'], SCALE,
                                                WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        self.car_2_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_2_sprites.append(arcade.Sprite(self.textures['car_2'], SCALE,
                                                SCALED_SQUARE*.5, y))
        self.car_3_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_3_sprites.append(arcade.Sprite(self.textures['car_3'], SCALE,
                                                WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        self.car_4_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_4_sprites.append(arcade.Sprite(self.textures['car_4'], SCALE,
                                                SCALED_SQUARE*.5, y))
        self.truck_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.truck_sprites.append(arcade.Sprite(self.textures['truck'], SCALE,
                                                WINDOW_WIDTH-SCALED_SQUARE, y))

    def car_movement(self):
        self.car_1_sprites[0].center_x -= OBSTACLE_SPEED
        self.car_3_sprites[0].center_x -= OBSTACLE_SPEED
        self.truck_sprites[0].center_x -= OBSTACLE_SPEED
        if self.car_1_sprites[0].center_x < 0:
            #reset position of car
            self.car_1_sprites[0].center_x = WINDOW_WIDTH
            self.car_3_sprites[0].center_x = WINDOW_WIDTH
            self.truck_sprites[0].center_x = WINDOW_WIDTH
        self.car_2_sprites[0].center_x += OBSTACLE_SPEED
        self.car_4_sprites[0].center_x += OBSTACLE_SPEED
        if self.car_2_sprites[0].center_x > WINDOW_WIDTH:
            self.car_2_sprites[0].center_x = 0
            self.car_4_sprites[0].center_x = 0

    def on_draw(self):
        self.car_1_sprites.draw()
        self.car_2_sprites.draw()
        self.car_3_sprites.draw()
        self.car_4_sprites.draw()
        self.truck_sprites.draw()
