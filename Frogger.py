import arcade

# Change this SCALE constant to resize the window and everything is scaled appropriately
SCALE = 2
SPRITE_SQUARE = 16
SCALED_SQUARE = SPRITE_SQUARE*SCALE
MOVEMENT_SPEED = 4.5

WINDOW_WIDTH = 28*8*SCALE
WINDOW_HEIGHT = 32*8*SCALE
WINDOW_TITLE = "Frogger"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()

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
        # TODO: Figure out how to remove the black/grey backgrounds from sprites
        # TODO: Add additional sprite textures like death animation, points, timer, etc

        # Load the spritesheet
        spritesheet = arcade.load_spritesheet('assets/spritesheet.png')

        # -- Load the background textures -- #
        self.textures['background'] = spritesheet.get_texture(arcade.LBWH(1, 390, 28, 32))
        self.textures['median'] = spritesheet.get_texture(
            arcade.LBWH(135, 196, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['homes'] = spritesheet.get_texture(
            arcade.LBWH(1, 188, SPRITE_SQUARE*2, SPRITE_SQUARE*1.5))
        self.textures['grass'] = spritesheet.get_texture(
            arcade.LBWH(35, 188, SPRITE_SQUARE*.5, SPRITE_SQUARE*1.5))

        # -- Load the frog textures -- #
        # # I can't figure out how get_texture_grid() works, but I think that might be useful
        self.textures['frog_up'] = spritesheet.get_texture(
            arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))

        # -- Load the vehicle textures -- #
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

        # -- Load the log textures -- #
        self.textures['log_left'] = spritesheet.get_texture(
            arcade.LBWH(1, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['log_middle'] = spritesheet.get_texture(
            arcade.LBWH(19, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.textures['log_right'] = spritesheet.get_texture(
            arcade.LBWH(37, 134, SPRITE_SQUARE, SPRITE_SQUARE))

        # -- Load the turtle textures -- #
        self.textures['turtle'] = spritesheet.get_texture(
            arcade.LBWH(19, 152, SPRITE_SQUARE, SPRITE_SQUARE))


    def draw_background(self):
        '''Draws the background image including median strips and ending homes.'''
        # -- Draw the background -- #
        arcade.draw_texture_rect(self.textures['background'],
            arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
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
                    arcade.LBWH(x+SCALED_SQUARE*.5, SCALED_SQUARE*13, SCALED_SQUARE*.5, SCALED_SQUARE*1.5))


    def create_example_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        y = SCALED_SQUARE*1.5
        # Example of frog starting in the middle of bottom median
        self.frog_sprites = arcade.SpriteList()
        self.frog_sprites.append(arcade.Sprite(self.textures['frog_up'], SCALE, WINDOW_WIDTH/2, y))

        # Car/Truck examples - ordered by rows of highway
        self.car_1_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_1_sprites.append(arcade.Sprite(self.textures['car_1'], SCALE, WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        self.car_2_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_2_sprites.append(arcade.Sprite(self.textures['car_2'], SCALE, SCALED_SQUARE*.5, y))
        self.car_3_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_3_sprites.append(arcade.Sprite(self.textures['car_3'], SCALE, WINDOW_WIDTH-SCALED_SQUARE*.5, y))
        self.car_4_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.car_4_sprites.append(arcade.Sprite(self.textures['car_4'], SCALE, SCALED_SQUARE*.5, y))
        self.truck_sprites = arcade.SpriteList()
        y += SCALED_SQUARE
        self.truck_sprites.append(arcade.Sprite(self.textures['truck'], SCALE, WINDOW_WIDTH-SCALED_SQUARE, y))

        # Example of a small log - row 1 of water
        self.small_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE*.5
        y = SCALED_SQUARE*8.5
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_left'], SCALE, x, y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_middle'], SCALE, x, y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.textures['log_right'], SCALE, x, y))
        x += SCALED_SQUARE

        # Example of 3 turtles - row 2 of water
        self.triple_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(3):
            self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle'], SCALE, x, y))
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
        x += SCALED_SQUARE

        # Example of 2 turtles - row 4 of water
        self.double_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(2):
            self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle'], SCALE, x, y))
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
        x += SCALED_SQUARE


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
        # update frog position
        self.frog_sprites.update()

        # get frog current position
        frog = self.frog_sprites[0]
        frog_x = frog.center_x
        frog_y = frog.center_y

        # check boundaries of frogs position (ensure not go offscreen)
        # horizontal boundary check
        if frog_x > WINDOW_WIDTH - SCALED_SQUARE/2:
            frog.center_x = WINDOW_WIDTH - SCALED_SQUARE/2
        elif frog_x < SCALED_SQUARE/2:
            frog.center_x = SCALED_SQUARE/2

        # vertical boundary check
        if frog_y > WINDOW_HEIGHT - SCALED_SQUARE/2 - SCALED_SQUARE * 2:
            frog.center_y = WINDOW_HEIGHT - SCALED_SQUARE/2 - SCALED_SQUARE * 2
        if frog_y < SCALED_SQUARE/2 + SCALED_SQUARE:
            frog.center_y = SCALED_SQUARE/2 + SCALED_SQUARE

    # Triggers when a key is released
    def on_key_release(self, key, key_modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.frog_sprites[0].change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.frog_sprites[0].change_x = 0
    # Triggers when a key is pressed
    def on_key_press(self, key, key_modifiers):
        # if player presses a key, update the speed
        # if key == arcade.key.UP:
        #     self.frog_sprites[0].change_y = MOVEMENT_SPEED
        # elif key == arcade.key.DOWN:
        #     self.frog_sprites[0].change_y = -MOVEMENT_SPEED
        # elif key == arcade.key.LEFT:
        #     self.frog_sprites[0].change_x = -MOVEMENT_SPEED
        # elif key == arcade.key.RIGHT:
        #     self.frog_sprites[0].change_x = MOVEMENT_SPEED
        frog = self.frog_sprites[0]
        if key == arcade.key.UP:
            frog.center_y += SCALED_SQUARE
        elif key == arcade.key.DOWN:
            frog.center_y -= SCALED_SQUARE
        elif key == arcade.key.LEFT:
            frog.center_x -= SCALED_SQUARE
        elif key == arcade.key.RIGHT:
            frog.center_x += SCALED_SQUARE

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
