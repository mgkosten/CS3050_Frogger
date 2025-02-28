import arcade

MOVEMENT_SPEED = 5 # Movement speed for the player should probably be equal to SCALED_SQUARE b/c that is the height of each row; A separate movement speed for the obstacles is a good idea

SCALE = 2 # I think I set this up in a way that you can change this SCALE constant to resize the window and everything is scaled appropriately
SPRITE_SQUARE = 16
SCALED_SQUARE = SPRITE_SQUARE*SCALE

WINDOW_WIDTH = 28*8*SCALE
WINDOW_HEIGHT = 32*8*SCALE
WINDOW_TITLE = "Frogger"

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK

        # Load the spritesheet
        self.spritesheet = arcade.load_spritesheet('assets/spritesheet.png')
        # TODO: Figure out how to remove the black/grey backgrounds from sprites


        # -- Load the background -- #
        self.background = self.spritesheet.get_texture(arcade.LBWH(1, 390, 28, 32))
        self.median = self.spritesheet.get_texture(arcade.LBWH(135, 196, SPRITE_SQUARE, SPRITE_SQUARE))
        self.top_homes = self.spritesheet.get_texture(arcade.LBWH(1, 188, SPRITE_SQUARE*2, SPRITE_SQUARE*1.5))
        self.top_grass = self.spritesheet.get_texture(arcade.LBWH(35, 188, SPRITE_SQUARE*.5, SPRITE_SQUARE*1.5))

        # -- Load the frog textures -- #
        self.frog_up = self.spritesheet.get_texture(arcade.LBWH(1, 1, SPRITE_SQUARE, SPRITE_SQUARE))

        # -- Load the vehicle textures -- #
        self.car_1 = self.spritesheet.get_texture(arcade.LBWH(19, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_2 = self.spritesheet.get_texture(arcade.LBWH(55, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_3 = self.spritesheet.get_texture(arcade.LBWH(1, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_4 = self.spritesheet.get_texture(arcade.LBWH(37, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.truck = self.spritesheet.get_texture(arcade.LBWH(73, 116, SPRITE_SQUARE*2, SPRITE_SQUARE))

        # -- Load the log textures -- #
        # TODO: I can't figure out how to make get_texture_grid() work, but I think that it might be useful
        self.log_left = self.spritesheet.get_texture(arcade.LBWH(1, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.log_middle = self.spritesheet.get_texture(arcade.LBWH(19, 134, SPRITE_SQUARE, SPRITE_SQUARE))
        self.log_right = self.spritesheet.get_texture(arcade.LBWH(37, 134, SPRITE_SQUARE, SPRITE_SQUARE))
    

    def draw_background(self):
        '''Draws the background image including median strips and ending homes.'''
        # -- Draw the background -- #
        arcade.draw_texture_rect(self.background, arcade.LBWH(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        for x in range(0, WINDOW_WIDTH, SCALED_SQUARE):
            # Draw starting median
            arcade.draw_texture_rect(self.median, arcade.LBWH(x, SCALED_SQUARE, SCALED_SQUARE, SCALED_SQUARE))
            # Draw center median
            arcade.draw_texture_rect(self.median, arcade.LBWH(x, SCALED_SQUARE*7, SCALED_SQUARE, SCALED_SQUARE))
            
            # Draw the homes
            if x % (SCALED_SQUARE*3) == 0:
                arcade.draw_texture_rect(self.top_homes, arcade.LBWH(x, SCALED_SQUARE*13, self.top_homes.width*SCALE, self.top_homes.height*SCALE))
            if x % (SCALED_SQUARE*3) == SCALED_SQUARE*2:
                arcade.draw_texture_rect(self.top_grass, arcade.LBWH(x, SCALED_SQUARE*13, self.top_grass.width*SCALE, self.top_grass.height*SCALE))
                arcade.draw_texture_rect(self.top_grass, arcade.LBWH(x+self.top_grass.width*SCALE, SCALED_SQUARE*13, self.top_grass.width*SCALE, self.top_grass.height*SCALE))


    def create_example_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        # Example of frog starting in the middle
        self.frog_sprites = arcade.SpriteList()
        self.frog_sprites.append(arcade.Sprite(self.frog_up, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*1.5))

        # Car/Truck examples
        self.car_1_sprites = arcade.SpriteList()
        self.car_1_sprites.append(arcade.Sprite(self.car_1, scale=SCALE, center_x=WINDOW_WIDTH-SCALED_SQUARE*.5, center_y=SCALED_SQUARE*2.5))
        self.car_2_sprites = arcade.SpriteList()
        self.car_2_sprites.append(arcade.Sprite(self.car_2, scale=SCALE, center_x=SCALED_SQUARE*.5, center_y=SCALED_SQUARE*3.5))
        self.car_3_sprites = arcade.SpriteList()
        self.car_3_sprites.append(arcade.Sprite(self.car_3, scale=SCALE, center_x=WINDOW_WIDTH-SCALED_SQUARE*.5, center_y=SCALED_SQUARE*4.5))
        self.car_4_sprites = arcade.SpriteList()
        self.car_4_sprites.append(arcade.Sprite(self.car_4, scale=SCALE, center_x=SCALED_SQUARE*.5, center_y=SCALED_SQUARE*5.5))
        self.truck_sprites = arcade.SpriteList()
        self.truck_sprites.append(arcade.Sprite(self.truck, scale=SCALE, center_x=WINDOW_WIDTH-SCALED_SQUARE, center_y=SCALED_SQUARE*6.5))
        
        # Example of a small log
        self.small_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE/SCALE
        y = SCALED_SQUARE*9.5
        self.small_log_sprites.append(arcade.Sprite(self.log_left, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.log_middle, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE
        self.small_log_sprites.append(arcade.Sprite(self.log_right, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE

        # Example of a medium log
        self.medium_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE/SCALE
        y = SCALED_SQUARE*12.5
        self.medium_log_sprites.append(arcade.Sprite(self.log_left, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE
        for i in range(2):
            self.medium_log_sprites.append(arcade.Sprite(self.log_middle, scale=SCALE, center_x=x, center_y=y))
            x += SCALED_SQUARE
        self.medium_log_sprites.append(arcade.Sprite(self.log_right, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE

        # Example of a large log
        self.large_log_sprites = arcade.SpriteList()
        x = SCALED_SQUARE/SCALE
        y = SCALED_SQUARE*10.5
        self.large_log_sprites.append(arcade.Sprite(self.log_left, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE
        for i in range(4):
            self.large_log_sprites.append(arcade.Sprite(self.log_middle, scale=SCALE, center_x=x, center_y=y))
            x += SCALED_SQUARE
        self.large_log_sprites.append(arcade.Sprite(self.log_right, scale=SCALE, center_x=x, center_y=y))
        x += SCALED_SQUARE


    # Resets game
    def reset(self):
        pass

    # Renders everything
    def on_draw(self):
        self.clear()

        self.draw_background()

        self.car_1_sprites.draw()
        self.car_2_sprites.draw()
        self.car_3_sprites.draw()
        self.car_4_sprites.draw()
        self.truck_sprites.draw()
        self.small_log_sprites.draw()
        self.medium_log_sprites.draw()
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

    # Create example sprites
    game.create_example_sprites()

    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()