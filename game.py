from enum import Enum
DURATION = 100

class GameStates(Enum):
    MAIN_MENU = 0
    PLAYING = 1
    GAME_OVER = 2


class Game:
    def __init__(self):
        self.timer = 60 * DURATION
        self.game_time = 0
        self.game_over = False
        self.points = 0
        self.paused = False
        self.state = GameStates.MAIN_MENU


    def update_timer(self, frame_time):
        self.game_time += frame_time
        if self.game_time > self.timer:
            self.game_over = True
            self.state = GameStates.GAME_OVER

    def reset(self):
        self.game_time = 0
        self.game_over = False
        self.timer = 60 * DURATION
        self.points = 0
        self.paused = False
        self.state = GameStates.PLAYING

