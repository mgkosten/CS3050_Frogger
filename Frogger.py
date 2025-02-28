import arcade

WINDOW_WIDTH = 28*16
WINDOW_HEIGHT = 32*16
WINDOW_TITLE = "Frogger"

MOVEMENT_SPEED = 5
SPRITE_SQUARE = 16
SCALE = 2
SCALED_SQUARE = SPRITE_SQUARE*SCALE

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

        # -- Load the car textures -- #
        self.car_1 = self.spritesheet.get_texture(arcade.LBWH(19, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_2 = self.spritesheet.get_texture(arcade.LBWH(55, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_3 = self.spritesheet.get_texture(arcade.LBWH(1, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.car_4 = self.spritesheet.get_texture(arcade.LBWH(37, 116, SPRITE_SQUARE, SPRITE_SQUARE))
        self.truck = self.spritesheet.get_texture(arcade.LBWH(73, 116, SPRITE_SQUARE*2, SPRITE_SQUARE))
    

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
                arcade.draw_texture_rect(self.top_homes, arcade.LBWH(x, SCALED_SQUARE*14, self.top_homes.width*SCALE, self.top_homes.height*SCALE))
            if x % (SCALED_SQUARE*3) == SCALED_SQUARE*2:
                arcade.draw_texture_rect(self.top_grass, arcade.LBWH(x, SCALED_SQUARE*14, self.top_grass.width*SCALE, self.top_grass.height*SCALE))
                arcade.draw_texture_rect(self.top_grass, arcade.LBWH(x+self.top_grass.width*SCALE, SCALED_SQUARE*14, self.top_grass.width*SCALE, self.top_grass.height*SCALE))


    def create_example_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        # Example of frog starting in the middle
        self.frog_sprites = arcade.SpriteList()
        self.frog_sprites.append(arcade.Sprite(self.frog_up, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*1.5))

        # Car/Truck examples
        self.car_1_sprites = arcade.SpriteList()
        self.car_1_sprites.append(arcade.Sprite(self.car_1, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*2.5))
        self.car_2_sprites = arcade.SpriteList()
        self.car_2_sprites.append(arcade.Sprite(self.car_2, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*3.5))
        self.car_3_sprites = arcade.SpriteList()
        self.car_3_sprites.append(arcade.Sprite(self.car_3, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*4.5))
        self.car_4_sprites = arcade.SpriteList()
        self.car_4_sprites.append(arcade.Sprite(self.car_4, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*5.5))
        self.truck_sprites = arcade.SpriteList()
        self.truck_sprites.append(arcade.Sprite(self.truck, scale=SCALE, center_x=WINDOW_WIDTH/2, center_y=SCALED_SQUARE*6.5))


    # Resets game
    def reset(self):
        pass

    # Renders everything
    def on_draw(self):
        self.clear()

        self.draw_background()

        self.frog_sprites.draw()
        self.car_1_sprites.draw()
        self.car_2_sprites.draw()
        self.car_3_sprites.draw()
        self.car_4_sprites.draw()
        self.truck_sprites.draw()
    
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