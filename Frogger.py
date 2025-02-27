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


        # -- Create the background -- #
        self.background = self.spritesheet.get_texture(arcade.LBWH(1, 65, 28, 32), y_up=True)
        self.median = self.spritesheet.get_texture(arcade.LBWH(135, 275, SPRITE_SQUARE, SPRITE_SQUARE), y_up=True)
        self.top_homes = self.spritesheet.get_texture(arcade.LBWH(1, 275, 32, 24), y_up=True)
        self.top_grass = self.spritesheet.get_texture(arcade.LBWH(35, 275, 8, 24), y_up=True)

    # Resets game
    def reset(self):
        pass

    # Renders everything
    def on_draw(self):
        self.clear()

        # Draw the background
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
    
    # Frame update
    def on_update(self):
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


    # Start the arcade game loop
    arcade.run()


if __name__ == "__main__":
    main()