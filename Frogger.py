import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK

    def reset(self):
        pass

    def on_draw(self):
        self.clear()

    def on_update(self):
        pass

    def on_key_release(self, key, key_modifiers):

        pass

    def on_key_press(self, key, key_modifiers):
        pass