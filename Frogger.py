import arcade

MOVEMENT_SPEED = 5
# Movement speed for player probably should be SCALED_SQUARE b/c that is the size of each row
# A separate movement speed constant for the obstacles is a good idea

# Change this SCALE constant to resize the window and everything is scaled appropriately
SCALE = 2
SPRITE_SQUARE = 16
SCALED_SQUARE = SPRITE_SQUARE*SCALE

WINDOW_WIDTH = 28*8*SCALE
WINDOW_HEIGHT = 32*8*SCALE
WINDOW_TITLE = "Frogger"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # Reduce the number of instance attributes to make pylint happy

        # Define Textures dictionary
        self.textures = {}

        # Define example SpriteLists - ideally these would be collapsed to only a few SpriteLists
        self.frog_sprites = None
        self.car_1_sprites = None
        self.car_2_sprites = None
        self.car_3_sprites = None
        self.car_4_sprites = None
        self.truck_sprites = None
        self.small_log_sprites = None
        self.medium_log_sprites = None
        self.large_log_sprites = None
        self.triple_turtle_sprites = None
        self.double_turtle_sprites = None


    def load_textures(self):
        '''Loads sprite textures from the spritesheet'''
        # I can't figure out how get_texture_grid() works, but I think that might be useful

        # Load the spritesheet - https://www.spriters-resource.com/arcade/frogger/sheet/11067/
        spritesheet = arcade.load_spritesheet('assets/spritesheet_transparent.png')

        # -- Load the background textures -- #
        self.textures['water'] = spritesheet.get_texture(arcade.LBWH(1, 390, 28, 32))
        self.textures['median'] = spritesheet.get_texture(
            arcade.LBWH(135, 196, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['homes'] = spritesheet.get_texture(
            arcade.LBWH(1, 188, SPRITE_SQUARE*2, SPRITE_SQUARE*1.5))
        self.textures['grass'] = spritesheet.get_texture(
            arcade.LBWH(35, 188, SPRITE_SQUARE*.5, SPRITE_SQUARE*1.5))

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

        # -- Load the frog textures -- #
        # Player
        self.textures['frog_up'] = spritesheet.get_texture(
            arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_up_jump'] = spritesheet.get_texture(
            arcade.LBWH(19, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_left'] = spritesheet.get_texture(
            arcade.LBWH(37, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_left_jump'] = spritesheet.get_texture(
            arcade.LBWH(55, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_down'] = spritesheet.get_texture(
            arcade.LBWH(73, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_down_jump'] = spritesheet.get_texture(
            arcade.LBWH(91, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_right'] = spritesheet.get_texture(
            arcade.LBWH(109, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_right_jump'] = spritesheet.get_texture(
            arcade.LBWH(127, 1, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['frog_home'] = spritesheet.get_texture(
            arcade.LBWH(45, 196, SPRITE_SQUARE, SPRITE_SQUARE))

        # Lady Frog
        self.textures['lady_frog_up'] = spritesheet.get_texture(
            arcade.LBWH(1, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_up_jump'] = spritesheet.get_texture(
            arcade.LBWH(19, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_left'] = spritesheet.get_texture(
            arcade.LBWH(37, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_left_jump'] = spritesheet.get_texture(
            arcade.LBWH(55, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_down'] = spritesheet.get_texture(
            arcade.LBWH(73, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_down_jump'] = spritesheet.get_texture(
            arcade.LBWH(91, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_right'] = spritesheet.get_texture(
            arcade.LBWH(109, 19, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lady_frog_right_jump'] = spritesheet.get_texture(
            arcade.LBWH(127, 19, SPRITE_SQUARE, SPRITE_SQUARE))

        # -- Load interactive textures -- #
        # Vehicles
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

        # Logs
        self.textures['log_left'] = spritesheet.get_texture(
            arcade.LBWH(1, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['log_middle'] = spritesheet.get_texture(
            arcade.LBWH(19, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['log_right'] = spritesheet.get_texture(
            arcade.LBWH(37, 134, SPRITE_SQUARE, SPRITE_SQUARE))

        # Turtles
        self.textures['turtle_1'] = spritesheet.get_texture(
            arcade.LBWH(1, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['turtle_2'] = spritesheet.get_texture(
            arcade.LBWH(19, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['turtle_3'] = spritesheet.get_texture(
            arcade.LBWH(37, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['turtle_disappear_1'] = spritesheet.get_texture(
            arcade.LBWH(55, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['turtle_disappear_2'] = spritesheet.get_texture(
            arcade.LBWH(73, 152, SPRITE_SQUARE, SPRITE_SQUARE))

        # Alligators
        self.textures['alligator_1'] = spritesheet.get_texture(
            arcade.LBWH(55, 134, SPRITE_SQUARE*3, SPRITE_SQUARE))
        self.textures['alligator_2'] = spritesheet.get_texture(
            arcade.LBWH(105, 134, SPRITE_SQUARE*3, SPRITE_SQUARE))
        self.textures['alligator_home_1'] = spritesheet.get_texture(
            arcade.LBWH(99, 196, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['alligator_home_2'] = spritesheet.get_texture(
            arcade.LBWH(117, 196, SPRITE_SQUARE, SPRITE_SQUARE))

        # Snakes
        self.textures['snake_1'] = spritesheet.get_texture(
            arcade.LBWH(1, 170, SPRITE_SQUARE*3, SPRITE_SQUARE))
        self.textures['snake_2'] = spritesheet.get_texture(
            arcade.LBWH(19, 170, SPRITE_SQUARE*3, SPRITE_SQUARE))
        self.textures['snake_3'] = spritesheet.get_texture(
            arcade.LBWH(37, 170, SPRITE_SQUARE*3, SPRITE_SQUARE))

        # Otters
        self.textures['otter_1'] = spritesheet.get_texture(
            arcade.LBWH(91, 152, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['otter_2'] = spritesheet.get_texture(
            arcade.LBWH(109, 152, SPRITE_SQUARE, SPRITE_SQUARE))

        self.textures['fly'] = spritesheet.get_texture(
            arcade.LBWH(81, 196, SPRITE_SQUARE, SPRITE_SQUARE))

        # -- Load additional textures -- #
        # Death animation
        self.textures['death_animation_1'] = spritesheet.get_texture(
            arcade.LBWH(1, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_2'] = spritesheet.get_texture(
            arcade.LBWH(19, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_3'] = spritesheet.get_texture(
            arcade.LBWH(37, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_4'] = spritesheet.get_texture(
            arcade.LBWH(55, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_5'] = spritesheet.get_texture(
            arcade.LBWH(73, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_6'] = spritesheet.get_texture(
            arcade.LBWH(91, 80, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['death_animation_7'] = spritesheet.get_texture(
            arcade.LBWH(109, 80, SPRITE_SQUARE, SPRITE_SQUARE))

        # Timer
        self.textures['timer_green_full'] = spritesheet.get_texture(
            arcade.LBWH(57, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_green_three_quarter'] = spritesheet.get_texture(
            arcade.LBWH(67, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_green_half'] = spritesheet.get_texture(
            arcade.LBWH(77, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_green_quarter'] = spritesheet.get_texture(
            arcade.LBWH(87, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_red_full'] = spritesheet.get_texture(
            arcade.LBWH(97, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_red_three_quarter'] = spritesheet.get_texture(
            arcade.LBWH(107, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_red_half'] = spritesheet.get_texture(
            arcade.LBWH(117, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))
        self.textures['timer_red_quarter'] = spritesheet.get_texture(
            arcade.LBWH(127, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))

        # Miscellaneous
        self.textures['points_100'] = spritesheet.get_texture(
            arcade.LBWH(1, 214, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['points_200'] = spritesheet.get_texture(
            arcade.LBWH(19, 214, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['lives'] = spritesheet.get_texture(
            arcade.LBWH(37, 214, SPRITE_SQUARE/2, SPRITE_SQUARE/2))


    def draw_background(self):
        '''Draws the background image including median strips and ending homes.'''

        # -- Draw the background -- #
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

        for x in range(0, WINDOW_WIDTH, SCALED_SQUARE):
            # Draw starting median
            arcade.draw_texture_rect(self.textures['median'],
                arcade.LBWH(x, SCALED_SQUARE, SCALED_SQUARE, SCALED_SQUARE))
            # Draw center median
            arcade.draw_texture_rect(self.textures['median'],
                arcade.LBWH(x, SCALED_SQUARE*7, SCALED_SQUARE, SCALED_SQUARE))

            # Draw the homes
            if x % (SCALED_SQUARE*3) == 0:
                arcade.draw_texture_rect(self.textures['homes'],
                    arcade.LBWH(x, SCALED_SQUARE*13, SCALED_SQUARE*2, SCALED_SQUARE*1.5))
            if x % (SCALED_SQUARE*3) == SCALED_SQUARE*2:
                arcade.draw_texture_rect(self.textures['grass'],
                    arcade.LBWH(x, SCALED_SQUARE*13, SCALED_SQUARE*.5, SCALED_SQUARE*1.5))
                arcade.draw_texture_rect(self.textures['grass'],
                    arcade.LBWH(x+SCALED_SQUARE*.5, SCALED_SQUARE*13,
                                SCALED_SQUARE*.5, SCALED_SQUARE*1.5))


    def create_example_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        # pylint is unhappy about this function - says there are too many statements

        # Example of frog starting in the middle of bottom median
        self.frog_sprites = arcade.SpriteList()
        y = SCALED_SQUARE*1.5
        self.frog_sprites.append(arcade.Sprite(self.textures['otter_1'], SCALE, WINDOW_WIDTH/2, y))

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

        # Example of a small log - row 1 of water
        self.small_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE*.5
        y = SCALED_SQUARE*8.5
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))

        # Example of 3 turtles - row 2 of water
        self.triple_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(3):
            self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
            x -= SCALED_SQUARE

        # Example of a medium log - row 3 of water
        self.medium_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE*.5
        y += SCALED_SQUARE
        self.medium_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        x += SCALED_SQUARE
        for _ in range(2):
            self.medium_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
            x += SCALED_SQUARE
        self.medium_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))

        # Example of 2 turtles - row 4 of water
        self.double_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(2):
            self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
            x -= SCALED_SQUARE

        # Example of a large log - row 5 of water
        self.large_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE*.5
        y += SCALED_SQUARE
        self.large_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        x += SCALED_SQUARE
        for _ in range(4):
            self.large_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
            x += SCALED_SQUARE
        self.large_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))


    # Resets game
    def reset(self):
        pass

    # Renders everything
    def on_draw(self):
        self.clear()

        self.draw_background()

        # Draw example sprites
        self.car_1_sprites.draw()
        self.car_2_sprites.draw()
        self.car_3_sprites.draw()
        self.car_4_sprites.draw()
        self.truck_sprites.draw()
        self.small_log_sprites.draw()
        self.triple_turtle_sprites.draw()
        self.medium_log_sprites.draw()
        self.double_turtle_sprites.draw()
        self.large_log_sprites.draw()
        self.frog_sprites.draw()

    # Frame update
    def on_update(self, delta_time):
        pass

    # Triggers when a key is released
    def on_key_release(self, key, key_modifiers):

        pass
    # Triggers when a key is pressed
    def on_key_press(self, key, key_modifiers):
        pass

def main():
    """ Main function """
    window = arcade.Window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    # Create and setup the GameView
    game = GameView()

    # Show GameView on screen
    window.show_view(game)

    # Load textures
    game.load_textures()

    # Create example sprites
    game.create_example_sprites()

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()
