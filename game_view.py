'''Frogger game implemented using Python Arcade.'''

import arcade
from constants import *
from game import Game
from frog import Frog
from turt import Turt
from log import Log
from car import Car

# pylint: disable=fixme

class GameView(arcade.View):
    '''GameView class for running and displaying the game'''
    def __init__(self):
        super().__init__()
        # Define Textures dictionary
        self.textures = {}

        # Creating Containers for obstacles (and player)
        self.player : Frog = None
        self.turtles : list[Turt] = []
        self.logs : list[Log] = []
        self.cars : list[Car] = []

        # Creating SpriteList
        self.sprite_list = arcade.SpriteList()


    def load_background_textures(self, spritesheet):
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

        self.load_background_textures(spritesheet)

        # Load player, log, vehicle, and turtle textures
        self.player.load_textures(spritesheet)
        self.sprite_list.append(self.player.sprite)

        for log in self.logs:
            log.load_textures(spritesheet)
            self.sprite_list.extend(log.sprite)

        for car in self.cars:
            car.load_textures(spritesheet)
            self.sprite_list.append(car.sprite)

        for turtle in self.turtles:
            turtle.load_textures(spritesheet)
            self.sprite_list.extend(turtle.sprite)


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
                                         arcade.LBWH(x, SCALED_SQUARE*13,
                                                     SCALED_SQUARE*2, SCALED_SQUARE*1.5))
            if x % (SCALED_SQUARE*3) == SCALED_SQUARE*2:
                arcade.draw_texture_rect(self.textures['grass'],
                                         arcade.LBWH(x, SCALED_SQUARE*13,
                                                     SCALED_SQUARE*.5, SCALED_SQUARE*1.5))
                arcade.draw_texture_rect(self.textures['grass'],
                                         arcade.LBWH(x+SCALED_SQUARE*.5, SCALED_SQUARE*13,
                                                     SCALED_SQUARE*.5, SCALED_SQUARE*1.5))


    def create_sprites(self):
        '''Create some example sprites to demonstrate the process'''

        self.player = Frog(WINDOW_WIDTH/2, SCALED_SQUARE*1.5)

        # TODO: change the initial xpos for each of these and add more of each
        # Example vehicles
        self.cars.append(Car(1, -1, WINDOW_WIDTH/2, SCALED_SQUARE*2.5))
        self.cars.append(Car(2, 1, WINDOW_WIDTH/2, SCALED_SQUARE*3.5))
        self.cars.append(Car(3, -1, WINDOW_WIDTH/2, SCALED_SQUARE*4.5))
        self.cars.append(Car(4, 1, WINDOW_WIDTH/2, SCALED_SQUARE*5.5))
        self.cars.append(Car(5, -1, WINDOW_WIDTH/2, SCALED_SQUARE*6.5))

        # # Example of 3 turtles - rows 1 and 4 of water
        self.turtles.append(Turt(3, WINDOW_WIDTH/2, SCALED_SQUARE*8.5))
        self.turtles.append(Turt(2, WINDOW_WIDTH/2, SCALED_SQUARE*11.5))
        # # Example of a small, medium, and large log - rows 2, 3, and 5 of water
        self.logs.append(Log(3, WINDOW_WIDTH/2, SCALED_SQUARE*9.5))
        self.logs.append(Log(4, WINDOW_WIDTH/2, SCALED_SQUARE*10.5))
        self.logs.append(Log(6, WINDOW_WIDTH/2, SCALED_SQUARE*12.5))


    # Resets game
    def reset(self):
        '''Resets the game'''
        # TODO: what is this stuff doing?
        x = SCALED_SQUARE * .5
        y = SCALED_SQUARE * 8.5

        row1 = []
        row1.append(Log(3, 0, y))
        row1.append(Log(3, 4*x, y))


    # Renders everything
    def on_draw(self):
        self.clear()

        self.draw_background()
        self.sprite_list.draw()

    # Frame update
    def on_update(self, delta_time):
        pass

    # Triggers when a key is released
    def on_key_release(self, key, modifiers):
        # pylint: disable=unused-argument
        # TODO: do we need this function?
        pass

    # Triggers when a key is pressed
    def on_key_press(self, symbol, modifiers):
        # pylint: disable=unused-argument
        self.player.move(symbol)


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

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
