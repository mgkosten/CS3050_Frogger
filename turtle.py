from constants import *

class Turtle:
    def __init__(self):
        # Define Textures dictionary
        self.textures = {}
        self.triple_turtle_sprites = None
        self.double_turtle_sprites = None

    def load_textures(self, spritesheet):
        '''Loads interactive textures for the turtles
           from the spritesheet into the textures dictionary'''
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

    def create_sprites(self):
        '''Create some example sprites to demonstrate the process'''
        # Example of 3 turtles - row 2 of water
        self.triple_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(3):
            self.triple_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
            x -= SCALED_SQUARE
        # Example of 2 turtles - row 4 of water
        self.double_turtle_sprites = arcade.SpriteList()
        x = WINDOW_WIDTH-SCALED_SQUARE*.5
        y += SCALED_SQUARE
        for _ in range(2):
            self.double_turtle_sprites.append(arcade.Sprite(self.textures['turtle_2'], SCALE, x, y))
            x -= SCALED_SQUARE

    def move(self):
        # moves the
        if self.triple_turtle_sprites:
            for turtle in self.triple_turtle_sprites:
                turtle.center_x -= OBSTACLE_SPEED
                if turtle.center_x < 0:
                    turtle.center_x = WINDOW_WIDTH

        if self.double_turtle_sprites:
            for turtle in self.double_turtle_sprites:
                turtle.center_x -= OBSTACLE_SPEED
                if turtle.center_x < 0:
                    turtle.center_x = WINDOW_WIDTH

    def draw(self):
        self.triple_turtle_sprites.draw()
        self.double_turtle_sprites.draw()