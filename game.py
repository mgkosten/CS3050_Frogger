'''Game class'''
# pylint: disable=wildcard-import, unused-wildcard-import
from enum import Enum
import arcade
from constants import *

class GameStates(Enum):
    '''GameStates enum for tracking state/screen of the Game'''
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2

class Game:
    '''Game class'''
    def __init__(self):
        self.game_time = DURATION
        self.timer_text = arcade.Text(f"Time: {int(self.game_time)}",
                                      0, 0, TEXT_COLOR, SCALED_SQUARE)
        self.timer_text.x = WINDOW_WIDTH-self.timer_text.content_width

        self.game_over = False
        self.points = 0
        self.score_text = arcade.Text(f"Score: {self.points}", 0, 0, TEXT_COLOR, SCALED_SQUARE*.5)
        self.paused = False
        self.state = GameStates.MAIN_MENU

    def draw_text(self):
        '''Call in on_draw to draw text for GameView'''
        self.timer_text.draw()
        self.score_text.draw()
        if self.paused:
            arcade.draw_text("PAUSED", WINDOW_WIDTH/2, WINDOW_HEIGHT/2-SCALED_SQUARE,
                             TEXT_COLOR, SCALED_SQUARE, anchor_x="center")


    def update_timer(self, frame_time):
        '''Call in on_update to update the timer'''
        self.game_time -= frame_time
        self.timer_text.text = f"Time: {int(self.game_time)}"

    def update_points(self):
        '''Call in on_update to update the points'''
        self.score_text.text = f"Time: {int(self.points)}"

    def reset(self):
        '''Reset the game to beginning state'''
        self.game_time = DURATION
        self.game_over = False
        self.points = 0
        self.paused = False
        self.state = GameStates.PLAYING
