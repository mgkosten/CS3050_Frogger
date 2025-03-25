'''Frogger game implemented using Python Arcade.'''

import arcade
from constants import *
from game import Game
from frog import Frog
from turtle import Turtle
from log import Log
from car import Car

# pylint: disable=too-many-instance-attributes
# pylint: disable=fixme

class GameView(arcade.View):
    '''GameView class for running and displaying the game'''
    def __init__(self):
        super().__init__()
        # Define Textures dictionary
        self.textures = {}

        # Creating Containers for obstacles (and player)
        self.player = Frog(WINDOW_WIDTH/2, SCALED_SQUARE*1.5)
        self.turtles = []
        self.logs = []
        self.cars = []

        # Creating SpriteList
        self.spriteList = arcade.SpriteList()

        # self.small_log_sprites = None
        # self.medium_log_sprites = None
        # self.large_log_sprites = None
        # self.triple_turtle_sprites = None
        # self.double_turtle_sprites = None



    def _load_background_textures(self, spritesheet):
        '''Loads background textures from the spritesheet into the textures dictionary'''
        self.textures['water'] = spritesheet.get_texture(arcade.LBWH(1, 390, 28, 32))
        self.textures['median'] = spritesheet.get_texture(
            arcade.LBWH(135, 196, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['homes'] = spritesheet.get_texture(
            arcade.LBWH(1, 188, SPRITE_SQUARE*2, SPRITE_SQUARE*1.5))
        self.textures['grass'] = spritesheet.get_texture(
            arcade.LBWH(35, 188, SPRITE_SQUARE*.5, SPRITE_SQUARE*1.5))
        # Title Letters
        self.textures['title_f'] = spritesheet.get_texture(
            arcade.LBWH(1, 232, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['title_r'] = spritesheet.get_texture(
            arcade.LBWH(19, 232, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['title_o'] = spritesheet.get_texture(
            arcade.LBWH(37, 232, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['title_g'] = spritesheet.get_texture(
            arcade.LBWH(55, 232, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['title_e'] = spritesheet.get_texture(
            arcade.LBWH(73, 232, SPRITE_SQUARE, SPRITE_SQUARE))


    def load_textures(self):
        '''Loads sprite textures from the spritesheet'''
        # I can't figure out how get_texture_grid() works, but I think that might be useful
        # Load the spritesheet - https://www.spriters-resource.com/arcade/frogger/sheet/11067/
        spritesheet = arcade.load_spritesheet('assets/spritesheet_transparent.png')

        # Call helper methods to load textures
        self._load_background_textures(spritesheet)
        self.player.load_textures(spritesheet)
        self.spriteList.append(self.player.sprite)

        for log in self.logs:
            log.load_textures(spritesheet)
            self.spriteList.extend(log.sprite)

        for car in self.cars:
            car.load_textures(spritesheet)
            self.spriteList.append(car.sprite)

        for turtle in self.turtles:
            turtle.load_textures(spritesheet)
            self.spriteList.extend(turtle.sprite)

        # self.player.load_textures(spritesheet)
        # self.cars.load_textures(spritesheet)
        # self.logs.load_texture(spritesheet)
        # self.turtles.load_textures(spritesheet)

    def draw_background(self):
        '''Draws the background image including median strips and ending homes.'''
        arcade.draw_texture_rect(self.textures['water'],
                                 arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        # Draw the title
        title_x = WINDOW_WIDTH/2-SCALED_SQUARE*3.5
        title_y = SCALED_SQUARE*14.5
        arcade.draw_texture_rect(self.textures['title_f'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_r'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_o'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_g'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_g'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_e'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        title_x += SCALED_SQUARE
        arcade.draw_texture_rect(self.textures['title_r'],
                                 arcade.LBWH(title_x, title_y, SCALED_SQUARE, SCALED_SQUARE))
        # Draw medians and homes
        for x in range(0, WINDOW_WIDTH, SCALED_SQUARE):
            # Draw medians
            arcade.draw_texture_rect(self.textures['median'],
                                     arcade.LBWH(x, SCALED_SQUARE, SCALED_SQUARE, SCALED_SQUARE))
            arcade.draw_texture_rect(self.textures['median'],
                                     arcade.LBWH(x, SCALED_SQUARE*7, SCALED_SQUARE, SCALED_SQUARE))
            # Draw homes
            if x % (SCALED_SQUARE*3) == 0:
                arcade.draw_texture_rect(self.textures['homes'],
                                         arcade.LBWH(x, SCALED_SQUARE*13, SCALED_SQUARE*2, SCALED_SQUARE*1.5))
            if x % (SCALED_SQUARE*3) == SCALED_SQUARE*2:
                arcade.draw_texture_rect(self.textures['grass'],
                                         arcade.LBWH(x, SCALED_SQUARE*13, SCALED_SQUARE*.5, SCALED_SQUARE*1.5))
                arcade.draw_texture_rect(self.textures['grass'],
                                         arcade.LBWH(x+SCALED_SQUARE*.5, SCALED_SQUARE*13,
                                                     SCALED_SQUARE*.5, SCALED_SQUARE*1.5))


    def create_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        # pylint: disable=too-many-statements
        # Example of frog starting in the middle of bottom median

        self.turtles.append(Turtle(1000, WINDOW_WIDTH/2,WINDOW_HEIGHT))
        self.logs.append(Log(1,1,1, 1))
        self.cars.append(Car(1, 1, 15, 5))



        # self.frog_sprites = arcade.SpriteList()
        # y = SCALED_SQUARE*1.5
        # self.frog_sprites.append(arcade.Sprite(self.textures['frog_up'], SCALE, WINDOW_WIDTH/2, y))
        # # Car/Truck examples - ordered by rows of highway
        # self.car_1_sprites = arcade.SpriteList()
        # y += SCALED_SQUARE
        # self.car_1_sprites.append(arcade.Sprite(self.textures['car_1'], SCALE,
        #                                         WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        # self.car_2_sprites = arcade.SpriteList()
        # y += SCALED_SQUARE
        # self.car_2_sprites.append(arcade.Sprite(self.textures['car_2'], SCALE,
        #                                         SCALED_SQUARE*.5, y))
        # self.car_3_sprites = arcade.SpriteList()
        # y += SCALED_SQUARE
        # self.car_3_sprites.append(arcade.Sprite(self.textures['car_3'], SCALE,
        #                                         WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        # self.car_4_sprites = arcade.SpriteList()
        # y += SCALED_SQUARE
        # self.car_4_sprites.append(arcade.Sprite(self.textures['car_4'], SCALE,
        #                                         SCALED_SQUARE*.5, y))
        # self.truck_sprites = arcade.SpriteList()
        # y += SCALED_SQUARE
        # self.truck_sprites.append(arcade.Sprite(self.textures['truck'], SCALE,
        #                                         WINDOW_WIDTH-SCALED_SQUARE, y))
        # # Example of a small log - row 1 of water
        # self.small_log_sprites = arcade.SpriteList()
        # x = SCALED_SQUARE*.5
        # y = SCALED_SQUARE*8.5
        # self.small_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        # x += SCALED_SQUARE
        # self.small_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
        # x += SCALED_SQUARE
        # self.small_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))
        # # Example of 3 turtles - row 2 of water
        # self.triple_turtle_sprites = arcade.SpriteList()
        # x = WINDOW_WIDTH-SCALED_SQUARE*.5
        # y += SCALED_SQUARE
        # for _ in range(3):
        #     self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
        #     x -= SCALED_SQUARE
        # # Example of a medium log - row 3 of water
        # self.medium_log_sprites = arcade.SpriteList()
        # x = SCALED_SQUARE*.5
        # y += SCALED_SQUARE
        # self.medium_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        # x += SCALED_SQUARE
        # for _ in range(2):
        #     self.medium_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
        #     x += SCALED_SQUARE
        # self.medium_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))
        # # Example of 2 turtles - row 4 of water
        # self.double_turtle_sprites = arcade.SpriteList()
        # x = WINDOW_WIDTH-SCALED_SQUARE*.5
        # y += SCALED_SQUARE
        # for _ in range(2):
        #     self.double_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
        #     x -= SCALED_SQUARE
        # # Example of a large log - row 5 of water
        # self.large_log_sprites = arcade.SpriteList()
        # x = SCALED_SQUARE*.5
        # y += SCALED_SQUARE
        # self.large_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        # x += SCALED_SQUARE
        # for _ in range(4):
        #     self.large_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
        #     x += SCALED_SQUARE
        # self.large_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))


    # Resets game
    def reset(self):
        '''Resets the game'''
        x = SCALED_SQUARE * .5
        y = SCALED_SQUARE * 8.5

        row1 = []
        row1.append(Log(3, 0, y))
        row1.append(Log(3, 4*x, y))


    # Renders everything
    def on_draw(self):
        self.clear()

        self.draw_background()
        self.spriteList.draw()


        # Draw example sprites
        # self.cars.draw()
        # self.car_1_sprites.draw()
        # self.car_2_sprites.draw()
        # self.car_3_sprites.draw()
        # self.car_4_sprites.draw()
        # self.truck_sprites.draw()
        # self.small_log_sprites.draw()
        # self.medium_log_sprites.draw()
        # self.large_log_sprites.draw()
        # self.player.draw()
        # self.turtles.draw()
        # self.cars.draw()

    # Frame update
    # TODO: Add info to change direction frog is facing based on movement
    def on_update(self, delta_time):
        pass

    # Triggers when a key is released
    def on_key_release(self, key, modifiers):
        # pylint: disable=unused-argument
        pass

    # Triggers when a key is pressed
    def on_key_press(self, symbol, modifiers):
        # pylint: disable=unused-argument

        self.player.move(symbol)

    # TODO: Add way to move frog when key is held down: timer or something


def main():
    """ Main function """
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Load textures
    game.create_sprites()
    game.load_textures()


    # # Create example sprites
    # game.create_example_sprites()
    # self.cars.create_cars()
    # self.turtles.create_sprites()

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
