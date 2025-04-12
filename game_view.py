'''Frogger game implemented using Python Arcade.'''
# pylint: disable=wildcard-import, unused-wildcard-import, too-many-instance-attributes, abstract-method
import os
import arcade
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import db
from firebase import firebase_access, add_entry
from constants import *
from game import Game
from frog import Frog
from turt import Turt
from log import Log
from car import Car

# Starting View
class InstructionView(arcade.View):
    """Creates the introduction screen of the game."""
    def on_show_view(self):
        self.window.background_color = arcade.csscolor.BLACK

    def on_draw(self):
        self.clear()
        arcade.draw_text("Controls", WINDOW_WIDTH/2, WINDOW_HEIGHT-SCALED_SQUARE*2,
                         arcade.color.GREEN_YELLOW, font_size=SCALED_SQUARE*2, anchor_x='center')
        arcade.draw_text("W/Up = Move up\nA/Left = Move left\nS/Down = Move down\nD/Right = Move right\nSpace = Pause/Unpause",
                         WINDOW_WIDTH/2, WINDOW_HEIGHT-SCALED_SQUARE*4, arcade.color.GREEN_YELLOW,
                         font_size=SCALED_SQUARE, anchor_x='center', multiline=True,
                         width=WINDOW_WIDTH, align="center")
        arcade.draw_text("Press the Space Bar to play!", WINDOW_WIDTH/2,
                         SCALED_SQUARE*3, arcade.color.GREEN_YELLOW, font_size=SCALED_SQUARE,
                         anchor_x='center', multiline=True, width=WINDOW_WIDTH, align="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            game_view = GameView()
            game_view.make_objects()
            game_view.load_textures()
            self.window.show_view(game_view)
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()

# Where the game is played
class GameView(arcade.View):
    '''GameView class for running and displaying the game'''
    def __init__(self):
        super().__init__()

        # Define Textures dictionary
        self.textures = {}

        # Levels
        self.level = 1

        # home frog count
        self.frog_home_count = 0

        # death animation
        self.current_animation_index = 0
        self.frog_death_x = 0
        self.frog_death_y = 0

        # max y value of frog player through each level
        self.max_frog_y = SCALED_SQUARE*1.5

        # Creating Containers for obstacles (and player)
        self.player = Frog()
        self.turtles = []
        self.logs = []
        self.cars = []
        self.frog_homes = []
        self.death_animations = []

        # Creating SpriteList
        self.sprite_list = arcade.SpriteList()
        self.car_sprites = arcade.SpriteList()
        self.turtle_sprites = arcade.SpriteList()
        self.log_sprites = arcade.SpriteList()
        self.frog_home_sprites = arcade.SpriteList()
        self.death_frog_sprites = arcade.SpriteList()

        # Creating timer and game backend
        self.backend = Game()

        # Making CRT Filter
        self.crt_filter = arcade.experimental.crt_filter.CRTFilter(FILTER_WIDTH, FILTER_HEIGHT,
                                                                   resolution_down_scale=DSCALE,
                                                                   hard_scan=SCAN, hard_pix=PIX,
                                                                   display_warp=WARP,
                                                                   mask_dark=DARKMASK,
                                                                   mask_light=LIGHTMASK)
        self.paused = False

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
            self.log_sprites.extend(log.sprite_list)

        for car in self.cars:
            car.setup(spritesheet)
            self.car_sprites.append(car.sprite)

        for turtle in self.turtles:
            turtle.load_textures(spritesheet)
            self.turtle_sprites.extend(turtle.sprite_list)

        for frog_home in self.frog_homes:
            frog_home.load_textures(spritesheet, 'frog_down')
            self.frog_home_sprites.append(frog_home.sprite)

        # Adding obstacle sprites to main sprite list
        self.sprite_list.extend(self.log_sprites)
        self.sprite_list.extend(self.car_sprites)
        self.sprite_list.extend(self.turtle_sprites)
        self.sprite_list.extend(self.frog_home_sprites)

        for i, death_anim in enumerate(self.death_animations):
            death_anim.load_textures(spritesheet, ('death_animation_' + str(i + 1)))
            self.death_frog_sprites.append(death_anim.sprite)

        self.player.load_textures(spritesheet, 'frog_up')
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
        '''Create obstacles: cars, logs, and turtles'''
        for i in range(4):
            self.turtles.append(Turt(3, SCALED_SQUARE*4*i))
            self.turtles.append(Turt(2, WINDOW_WIDTH-SCALED_SQUARE*3.5*i))

        for i in range(3):
            self.cars.append(Car(1, SCALED_SQUARE*4.5*i))
            self.cars.append(Car(2, WINDOW_WIDTH-SCALED_SQUARE*4*i))
            self.cars.append(Car(3, WINDOW_WIDTH-SCALED_SQUARE*4*i))
            self.cars.append(Car(4, SCALED_SQUARE*4.5*i))

            self.logs.append(Log(LogType.SHORT, SCALED_SQUARE*5.5*i))
            self.logs.append(Log(LogType.MEDIUM, SCALED_SQUARE*6*i))

        for i in range(2):
            self.cars.append(Car(5, SCALED_SQUARE*5.5*i))
            self.logs.append(Log(LogType.LONG, SCALED_SQUARE*8.5*i))


        # create frog_home sprites
        for _ in range(5):
            self.frog_homes.append(Frog())

        # set values
        for frog in self.frog_homes:
            frog.xpos = -WINDOW_WIDTH
            frog.ypos = -WINDOW_HEIGHT

        # death animation sprites
        for _ in range(7):
            self.death_animations.append(Frog())

        # set location
        for animation in self.death_animations:
            animation.xpos = -WINDOW_WIDTH
            animation.ypos = -WINDOW_HEIGHT

    # Resets game
    def reset(self):
        '''Resets the game'''
        self.backend.reset()
        self.player.reset()
        self.player.lives = 3
        self.level = 1

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

        found_home = False

        # start home x values
        x_val = SCALED_SQUARE

        # loop to make 5 homes
        for i in range(5):
            homes.append(x_val + (SCALED_SQUARE * 3) * i)

        # determine if frog is home
        if self.player.ypos >= SCALED_SQUARE * 13:
            for home in homes:
                if home - SCALED_SQUARE / 2 <= self.player.xpos < home + SCALED_SQUARE / 2:
                    # add to score for reaching home
                    self.backend.points += 160
                    self.backend.points += (round(self.backend.game_time) * 10)
                    # reset max y for frog
                    self.max_frog_y = SCALED_SQUARE*1.5
                    # reset timer
                    self.backend.game_time = DURATION
                    # set frog home
                    self.frog_homes[self.frog_home_count].xpos = home
                    self.frog_homes[self.frog_home_count].ypos = SCALED_SQUARE * 13.5
                    self.frog_home_count += 1
                    found_home = True
            if found_home:
                # reset frog
                self.player.reset()
            else:
                self.frog_death()

    def collision_detect(self, delta_time):
        '''Collision detection'''
        # Collision detection with cars
        if arcade.check_for_collision_with_list(self.player.sprite, self.car_sprites):
            # reset frog to starting position
            self.frog_death()

        # determine if in water or not
        if SCALED_SQUARE * 8 < self.player.ypos < SCALED_SQUARE * 13:
            # check if on log or not
            if arcade.check_for_collision_with_list(self.player.sprite, self.log_sprites):
                for log in self.logs:
                    if arcade.check_for_collision_with_list(self.player.sprite, log.sprite_list):
                        self.player.xpos += log.speed * delta_time * (1 + (0.15 * self.level))
            elif arcade.check_for_collision_with_list(self.player.sprite, self.turtle_sprites):
                self.player.xpos += self.turtles[0].speed * delta_time * (1 + (0.15 * self.level))
            else:
                self.frog_death()

        # if frog already in home
        if arcade.check_for_collision_with_list(self.player.sprite, self.frog_home_sprites):
            self.frog_death()

        self.check_home()

    def player_score(self):
        """player points for each jump towards home"""
        # check if player moved forward past max y
        if self.player.ypos > self.max_frog_y:
            self.backend.points += 10
            self.max_frog_y = self.player.ypos

    def frog_death(self):
        """Initiates frog death, reset frog & start animation"""
        self.player.lives -= 1

        # Cache the position before hiding the frog
        self.frog_death_x = self.player.xpos
        self.frog_death_y = self.player.ypos

        # reset frog positioning
        self.player.reset()

        # reset max y value of frog player through each level
        self.max_frog_y = SCALED_SQUARE * 1.5

        # reset so run every death
        self.current_animation_index = 0

        # start running animation
        arcade.schedule(self.play_next_death_frame, 0.1)

    def play_next_death_frame(self, delta_time):
        """Creates animation for when frog dies"""
        if self.current_animation_index < len(self.death_animations):
            # Show the next animation
            animation = self.death_animations[self.current_animation_index]

            # set animation positions
            animation.xpos = self.frog_death_x
            animation.ypos = self.frog_death_y

            # # reset frog positioning
            # self.player.reset()

            # Reset the PREVIOUS animation to off-screen (optional, but keeps one showing at a time)
            if self.current_animation_index > 0:
                prev_animation = self.death_animations[self.current_animation_index - 1]
                prev_animation.xpos = -WINDOW_WIDTH
                prev_animation.ypos = -WINDOW_HEIGHT

            self.current_animation_index += 1
        else:
            # Reset the last animation
            last_animation = self.death_animations[-1]
            last_animation.xpos = -WINDOW_WIDTH
            last_animation.ypos = -WINDOW_HEIGHT

            # Reset game state
            self.backend.game_time = DURATION
            # stop running death animation
            arcade.unschedule(self.play_next_death_frame)

    # Renders everything
    def on_draw(self):
        if FILTER_ON:
            self.crt_filter.use()
            self.crt_filter.clear()

            self.draw_background()
            self.backend.timer_text.draw()
            self.backend.score_text.draw()
            self.sprite_list.draw()
            self.death_frog_sprites.draw()

            if self.paused:
                arcade.draw_text("PAUSED", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                 arcade.color.GREEN_YELLOW, 50, anchor_x="center")

            self.window.use()
            self.clear()
            self.crt_filter.draw()
        else:
            self.window.use()
            self.clear()

            self.draw_background()
            self.backend.timer_text.draw()
            self.backend.score_text.draw()
            self.sprite_list.draw()
            self.death_frog_sprites.draw()

            if self.paused:
                arcade.draw_text("PAUSED", WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2,
                                 arcade.color.GREEN_YELLOW, 50, anchor_x="center")

    # Frame update
    def on_update(self, delta_time):
        if not self.paused:
            for turtle in self.turtles:
                turtle.update(delta_time, self.level)
            for log in self.logs:
                log.update(delta_time, self.level)
            for car in self.cars:
                car.update(delta_time, self.level)
            for frog_home in self.frog_homes:
                frog_home.update()
            for animation in self.death_animations:
                animation.update()
            self.player.update()

            self.backend.update_timer(delta_time)
            if self.backend.game_time <= 0:
                self.frog_death()

            self.collision_detect(delta_time)
            self.player_score()
            self.backend.update_points()

            if self.frog_home_count >= 5:
                # reset home frogs back offscreen
                for frog in self.frog_homes:
                    frog.xpos = -WINDOW_WIDTH
                    frog.ypos = -WINDOW_HEIGHT

                # reset count
                self.frog_home_count = 0

                # increment level
                self.level += 1

            if self.player.lives <= 0 and not self.backend.game_over:
                # Show game over screen
                self.backend.game_over = True

                # reset high score

                next_view = GameOverView(self.backend.points)
                self.window.show_view(next_view)

                self.backend.points = 0

                print('GAME OVER')

    # Triggers when a key is pressed
    def on_key_press(self, symbol, modifiers):
        # pylint: disable=unused-argument
        move_keys = [arcade.key.UP, arcade.key.DOWN, arcade.key.RIGHT, arcade.key.LEFT,
                     arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D]
        if symbol in move_keys:
            self.player.move(symbol)
        elif symbol == arcade.key.ESCAPE:
            arcade.close_window()
        elif symbol == arcade.key.SPACE:
            if self.paused:
                self.paused = False
            else:
                self.paused = True

class GameOverView(arcade.View):
    """Creates the game over screen"""
    def __init__(self, score):
        super().__init__()
        self.score = score

        #path to credentials file
        script_dir = os.path.dirname(__file__)
        service_account_path = os.path.join(script_dir, "credentials.json")

        # initialize firebase
        db = firebase_access(service_account_path)
        db = firestore.client()
        if not db:
            print("Firestore initialization failed")
            exit()
        add_entry(db, self.score)

    def on_show_view(self):
        self.window.background_color = arcade.color.BLACK

    def on_draw(self):
        self.clear()
        arcade.draw_text("Score: ", self.window.width / 2, self.window.height / 2,
                         arcade.color.GREEN_YELLOW, 50, anchor_x="center")
        arcade.draw_text(str(self.score), self.window.width / 2, self.window.height / 2 - 75,
                         arcade.color.GREEN_YELLOW, 50, anchor_x="center")
        arcade.draw_text("Press space to play again!", self.window.width / 2,
                         self.window.height / 2 - 150, arcade.color.GREEN_YELLOW,
                         50, anchor_x="center")

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            next_view = InstructionView()
            self.window.show_view(next_view)
        if symbol == arcade.key.ESCAPE:
            arcade.close_window()



def main():
    """ Main function """

    # Create and setup the GameView
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)
    start_view = InstructionView()
    window.show_view(start_view)
    arcade.run()


if __name__ == "__main__":
    main()
