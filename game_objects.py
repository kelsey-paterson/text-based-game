''' Module defining classes for use in game_play '''


# ---------------------- CLASSES ------------------------ #
class GameState:
  # Controls what is displayed in game main while loop

    def __init__(self):
        self.is_running = True
        self.start_game_menu = True

# ------------------ CREATE GAME OBJECTS ---------------- #

game_state = GameState()

