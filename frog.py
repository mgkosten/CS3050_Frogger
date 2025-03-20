import arcade
from constants import *
from enum import Enum

class Directions(Enum):
    left = 1
    right = 2
    up = 3
    down = 4

class Frog:
    def __init__(self):
        self.lives = 3
        self.frog_sprites = None
        # Define Textures dictionary
        self.textures = {}
        self.direction = Directions.up

    def load_textures(self, spritesheet):
        '''Loads frog textures from the spritesheet into the textures dictionary'''
        # Player Frog
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


    def create_sprites(self, frog_textures):
        '''Create the frog sprite'''
        # Example of frog starting in the middle of bottom median
        self.frog_sprites = arcade.SpriteList()
        y = SCALED_SQUARE * 1.5
        self.frog_sprites.append(arcade.Sprite(self.textures['frog_up'], SCALE, WINDOW_WIDTH / 2, y))
        # Add all the other directions to the spritelist

    # Resets game
    def reset(self):
        '''Reset frog's position'''
        # TODO: write this function which resets the frog to start position
        # I think this would be called from the GameView class when the frog dies

    # Renders everything
    def draw(self):
        '''Draw all frog sprites according to its direction'''
        self.frog_sprites.draw()
        # TODO: show a different sprite based on which direction it's facing

    def move(self, key):
        '''Move the frog on key press'''
        # TODO: call this function in on_key_press
        # upper_bound = WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2
        # lower_bound =

        frog = self.frog_sprites[0]
        if key == arcade.key.UP:
            frog.center_y += SCALED_SQUARE
        elif key == arcade.key.DOWN:
            frog.center_y -= SCALED_SQUARE
        elif key == arcade.key.LEFT:
            frog.center_x -= SCALED_SQUARE
        elif key == arcade.key.RIGHT:
            frog.center_x += SCALED_SQUARE

        # this stuff is from update for bound checking
        frog_x = frog.center_x
        frog_y = frog.center_y

        # check boundaries of frogs position (ensure not go offscreen)
        # horizontal boundary check
        if frog_x > WINDOW_WIDTH - SCALED_SQUARE / 2:
            frog.center_x = WINDOW_WIDTH - SCALED_SQUARE / 2
        elif frog_x < SCALED_SQUARE / 2:
            frog.center_x = SCALED_SQUARE / 2

        # vertical boundary check
        if frog_y > WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2:
            frog.center_y = WINDOW_HEIGHT - SCALED_SQUARE / 2 - SCALED_SQUARE * 2
        if frog_y < SCALED_SQUARE / 2 + SCALED_SQUARE:
            frog.center_y = SCALED_SQUARE / 2 + SCALED_SQUARE