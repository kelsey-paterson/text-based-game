''' Module defining classes for use in game_play '''

# ---------------------- CLASSES ------------------------ #
class GameState:
  # Controls what is displayed in game main while loop

    def __init__(self):
        self.is_running = True
        self.start_game_menu = True
        self.name_input = False
        self.pick_stats = False
        self.stat_num = 0
        self.main_game = False
        self.choosing_path = True
        self.first_room = True

class Player:

    def __init__(self, player_name):
      self.name = player_name
      self.location = '1E'
      self.health = 10
      self.attack = 10
      self.defence = 10
      self.agility = 10
      self.luck = 10
      self.inventory = {}
      self.rect_map = []
      self.xp = 0
      self.level = 1

class Room:

  def __init__(self):
    self.location = player.location
    self.content = ''
    self.paths = ''
    self.enemy = ''
    self.visited = False
    self.chest_opened = False

# ------------------ CREATE GAME OBJECTS ---------------- #

game_state = GameState()
player = Player('')

# ------------------ CREATE GAME DICTS ---------------- #
room_dict = {player.location: Room()}
