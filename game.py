'''Game class'''
from enum import Enum

DURATION = 100

class GameStates(Enum):
    '''GameStates enum for tracking state/screen of the Game'''
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2


class Game:
    '''Game class'''
    def __init__(self):
        self.timer = DURATION
        self.game_time = 0
        self.game_over = False
        self.points = 0
        self.paused = False
        self.state = GameStates.MAIN_MENU

    def update_timer(self, frame_time):
        '''Call in on_update to update the timer'''
        self.game_time += frame_time
        if self.game_time > self.timer:
            self.game_over = True
            self.state = GameStates.GAME_OVER

    def reset(self):
        '''Reset the game to beginning state'''
        self.game_time = 0
        self.game_over = False
        self.timer = DURATION
        self.points = 0
        self.paused = False
        self.state = GameStates.PLAYING
