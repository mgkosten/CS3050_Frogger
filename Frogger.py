import arcade

class GameView(arcade.View):
    def __init__(self):
        super().__init__()
        self.background_color = arcade.color.BLACK

    # Resets game
    def reset(self):
        pass

    # Renders everything
    def on_draw(self):
        self.clear()

    # Frame update
    def on_update(self):
        pass

    # Triggers when a key is released
    def on_key_release(self, key, key_modifiers):

        pass
    # Triggers when a key is pressed
    def on_key_press(self, key, key_modifiers):
        pass