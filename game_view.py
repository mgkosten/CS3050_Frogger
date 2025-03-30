'''Frogger game implemented using Python Arcade.'''
# pylint: disable=wildcard-import, unused-wildcard-import, fixme, too-many-instance-attributes
import arcade
from constants import *
from game import Game
from frog import Frog
from turt import Turt
from log import Log
from car import Car

class GameView(arcade.View):
    '''GameView class for running and displaying the game'''
    def __init__(self):
        super().__init__()
        # Define Textures dictionary
        self.textures = {}

        # Creating Containers for obstacles (and player)
        self.player = Frog()
        self.turtles = []
        self.logs = []
        self.cars = []

        # Creating SpriteList
        self.sprite_list = arcade.SpriteList()
        self.car_sprites = arcade.SpriteList()
        self.turtle_sprites = arcade.SpriteList()
        self.log_sprites = arcade.SpriteList()

        # Creating timer and game backend
        self.backend = Game()
        self.timer = arcade.Text("Time: " + str(int(self.backend.timer - self.backend.game_time)),
                                 2*WINDOW_WIDTH/3, 0, arcade.color.GREEN_YELLOW, 24)


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
        # Lives tracker
        self.textures['lives'] = spritesheet.get_texture(
            arcade.LBWH(37, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))


    def load_textures(self):
        '''Loads sprite textures from the spritesheet'''
        # Load the spritesheet - https://www.spriters-resource.com/arcade/frogger/sheet/11067/
        spritesheet = arcade.load_spritesheet('assets/spritesheet_transparent.png')

        self.load_background_textures(spritesheet)

        # Load player, log, vehicle, and turtle textures
        for log in self.logs:
            log.load_textures(spritesheet)
            self.log_sprites.extend(log.sprite)

        for car in self.cars:
            car.load_textures(spritesheet)
            self.car_sprites.append(car.sprite)

        for turtle in self.turtles:
            turtle.load_textures(spritesheet)
            self.turtle_sprites.extend(turtle.sprite)

        # Adding obstacle sprites to main sprite list
        self.sprite_list.extend(self.log_sprites)
        self.sprite_list.extend(self.car_sprites)
        self.sprite_list.extend(self.turtle_sprites)

        self.player.load_textures(spritesheet)
        self.sprite_list.append(self.player.sprite)


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
        # Draw remaining lives
        for i in range(self.player.lives):
            arcade.draw_texture_rect(self.textures['lives'],
                                     arcade.LBWH(i*SCALED_SQUARE*.5, SCALED_SQUARE*.5,
                                                 SCALED_SQUARE*.5, SCALED_SQUARE*.5))


    def make_objects(self):
        '''Create some example sprites to demonstrate the process'''
        # TODO: change the initial xpos for each of these and add more of each
        # Example vehicles
        direction = -1
        for i in range(5):
            self.cars.append(Car(i+1,direction,WINDOW_WIDTH/2, SCALED_SQUARE*(2.5+i)))
            self.cars.append(Car(i+1,direction,2*WINDOW_WIDTH/(5+i), SCALED_SQUARE*(2.5+i)))
            self.cars.append(Car(i+1,direction,7*WINDOW_WIDTH/(7+i), SCALED_SQUARE*(2.5+i)))
            direction = direction * -1

        # Example of triple and double turtles - rows 1 and 4 of water
        self.turtles.append(Turt(3, WINDOW_WIDTH/2, SCALED_SQUARE*8.5))
        self.turtles.append(Turt(3, 2*WINDOW_WIDTH/9, SCALED_SQUARE*8.5))
        self.turtles.append(Turt(3, 7*WINDOW_WIDTH/9, SCALED_SQUARE*8.5))
        self.turtles.append(Turt(2, WINDOW_WIDTH/2, SCALED_SQUARE*11.5))
        self.turtles.append(Turt(2, WINDOW_WIDTH/7, SCALED_SQUARE*11.5))
        self.turtles.append(Turt(2, 6*WINDOW_WIDTH/7, SCALED_SQUARE*11.5))

        # Example of a small, large, and medium log - rows 2, 3, and 5 of water
        self.logs.append(Log(3, WINDOW_WIDTH/2, SCALED_SQUARE*9.5))
        self.logs.append(Log(3, 6*WINDOW_WIDTH/7, SCALED_SQUARE*9.5))
        self.logs.append(Log(3, WINDOW_WIDTH/7, SCALED_SQUARE*9.5))
        self.logs.append(Log(6, WINDOW_WIDTH/2, SCALED_SQUARE*10.5))
        self.logs.append(Log(6, WINDOW_WIDTH, SCALED_SQUARE*10.5))
        self.logs.append(Log(4, WINDOW_WIDTH/2, SCALED_SQUARE*12.5))
        self.logs.append(Log(4, WINDOW_WIDTH/5, SCALED_SQUARE*12.5))
        self.logs.append(Log(4, 8*WINDOW_WIDTH/9, SCALED_SQUARE*12.5))


    # Resets game
    def reset(self):
        '''Resets the game'''
        self.backend.reset()
        self.player.xpos = WINDOW_WIDTH/2
        self.player.ypos = SCALED_SQUARE*1.5

        self.turtles = []
        self.logs = []
        self.cars = []

        self.sprite_list = arcade.SpriteList()
        self.car_sprites = arcade.SpriteList()
        self.turtle_sprites = arcade.SpriteList()
        self.log_sprites = arcade.SpriteList()

        self.make_objects()
        self.load_textures()

    def check_home(self):
        '''Checks if the frog is in the home area'''
        # create home center x values
        homes = []
        # loop to make 5 homes
        for i in range(5):
            homes.append(28 + (SCALED_SQUARE * 3) * i)

        # determine if frog is home
        if self.player.ypos >= SCALED_SQUARE * 13:
            for home in homes:
                if home - SCALED_SQUARE / 2 <= self.player.xpos < home + SCALED_SQUARE / 2:
                    print("HOME")
                else:
                    self.player.death()

    def collision_detect(self, delta_time):
        '''Collision detection'''
        # Collision detection with cars
        if arcade.check_for_collision_with_list(self.player.sprite, self.car_sprites):
            # reset frog to starting position
            self.player.death()

        # determine if in water or not
        if SCALED_SQUARE * 8 < self.player.ypos < SCALED_SQUARE * 13:
            # check if on log or not
            if not (arcade.check_for_collision_with_list(self.player.sprite, self.log_sprites) or
                    arcade.check_for_collision_with_list(self.player.sprite, self.turtle_sprites)):
                self.player.death()
            else:
                # get correct log speed
                if arcade.check_for_collision_with_list(self.player.sprite, self.log_sprites):
                    for log in self.logs:
                        for log_sprite in log.sprite:  # Iterate over individual sprites in the log
                            if arcade.check_for_collision(self.player.sprite, log_sprite):
                                self.player.xpos += (log.speed - log.length * 5) * delta_time
                                break  # Stop after finding the correct log
                else:
                    # update speed for when on turtle
                    self.player.xpos += self.turtles[0].speed * delta_time
        self.check_home()

    # Renders everything
    def on_draw(self):
        self.clear()

        # Timer Display
        self.timer.draw()

        self.draw_background()
        self.sprite_list.draw()

    # Frame update
    def on_update(self, delta_time):
        for turtle in self.turtles:
            turtle.update(delta_time)
        for log in self.logs:
            log.update(delta_time)
        for car in self.cars:
            car.update(delta_time)
        self.player.update()

        self.backend.update_timer(delta_time)
        time = int(self.backend.timer - self.backend.game_time)
        self.timer.text = "Time: " + str(time)
        if time <= 0:
            self.player.death()

        self.collision_detect(delta_time)

        if self.player.lives == 0:
            # TODO: Show game over screen
            self.backend.game_over = True


    # Triggers when a key is released
    def on_key_release(self, key, modifiers):
        # pylint: disable=unused-argument
        # TODO: Add way to move frog when key is held down: timer or something
        pass

    # Triggers when a key is pressed
    def on_key_press(self, symbol, modifiers):
        # pylint: disable=unused-argument
        move_keys = [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT,
                     arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D]
        if symbol in move_keys:
            self.player.move(symbol)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()


def main():
    """ Main function """
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Load textures
    game.make_objects()
    game.load_textures()

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
