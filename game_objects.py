''' Module defining classes for use in game_play '''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()

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
    
    def move(self, event):
      # TODO: need to limit to where there is paths drawn i.e. in line with text displayed.
      if event.type == pg.KEYDOWN:
          if event.key == pg.K_a and self.x > 0:
              self.x -= 1
              game_state.choosing_path = False
          if event.key == pg.K_d and self.x < 9:
              self.x += 1
              game_state.choosing_path = False
          if event.key == pg.K_w and self.y < 9:
              self.y += 1
              game_state.choosing_path = False
          if event.key == pg.K_s and self.y > 0:
              self.y -= 1
              game_state.choosing_path = False
    
    

class Room:

  def __init__(self):
    self.location = player.location
    self.content = ''
    self.paths = ''
    self.enemy = ''
    self.visited = False
    self.chest_opened = False
  
  def generate_room_content(self):
    # TODO: update function
    pass
    # self.visited = True
    # chest_chance = 10 + (1 * player.luck)
    # enemy_chance = 20
    # empty_chance = 10
    # window.fill((0, 0, 0))
    # self.content = random.choices(['Enemy', 'Chest', 'Empty'], 
    # weights=(enemy_chance, chest_chance, empty_chance),k=1)[0]
    # if self.content == 'Enemy':
    #     self.pick_enemy()
    #     Text_2.text = '(Press Enter to begin Combat)'
    # if self.content == 'Chest':
    #     Text_1.text = gt.chest_text
    #     Text_2.text = '(Press Enter to Open)'
    #     self.chest_opened = False
    # if self.content == 'Empty':
    #     Text_1.text = gt.empty_text
    #     Text_2.text = '(Press Enter to Continue)'


# ------------------ CREATE GAME OBJECTS ---------------- #

game_state = GameState()
player = Player('')

# ------------------ CREATE GAME DICTS ---------------- #
room_dict = {player.location: Room()}
