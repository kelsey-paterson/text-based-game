''' Module defining classes for use in game_play '''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
import game_data as gd
import game_display as gdi
import random
import string
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
        self.view_room = False
        self.combat = False
        self.chest = False

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
      self.x = 4
      self.y = 0

    
    def move(self, event_key):
      # TODO: need to limit to where there is paths drawn i.e. in line with text displayed.
      if event_key == pg.K_a and self.x > 0:
          self.x -= 1
          game_state.choosing_path = False
      elif event_key == pg.K_d and self.x < 9:
          self.x += 1
          game_state.choosing_path = False
      elif event_key == pg.K_w and self.y < 9:
          self.y += 1
          game_state.choosing_path = False
      elif event_key == pg.K_s and self.y > 0:
          self.y -= 1
          game_state.choosing_path = False

      # Update player location on map
      self.location = gd.room_map[self.y][self.x]

      # Update map display
      room_x = 150 + (self.x * 13)
      room_y = 400 - (self.y * 13)
      self.rect_map.append(pg.Rect(room_x, room_y, 12, 12))
    
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
    # chest_chance = gd.room_chances['chest'] + (1 * player.luck)
    enemy_chance = gd.room_chances['enemy']
    # empty_chance = gd.room_chances['empty']
    # Delete after testing
    chest_chance = 0
    empty_chance = 0
    # TODO: test if self.visited state required.
    # self.visited = True
    self.content = random.choices(['Enemy', 'Chest', 'Empty'], 
    weights=(enemy_chance, chest_chance, empty_chance), k=1)[0]

  def generate_room_text(self):
    gdi.window.fill((0, 0, 0))
    if self.content == 'Enemy':
        self.pick_enemy()
        gdi.Game_Text_2.text = '(Press Enter to Begin Combat)'
    if self.content == 'Chest':
        gdi.Game_Text_1.text = gd.chest_text
        gdi.Game_Text_2.text = '(Press Enter to Open)'
        self.chest_opened = False
    if self.content == 'Empty':
        gdi.Game_Text_1.text = gd.empty_text
        gdi.Game_Text_2.text = '(Press Enter to Continue)'

  def pick_enemy(self):
    print('picking enemy!')
    for level in gd.enemy_chances.keys():
      if self.location[0] == level:
        enemies = list(gd.enemy_chances[level].keys())
        weights = list(gd.enemy_chances[level].values())
        self.enemy = random.choices(enemies, weights=(weights), k=1)[0]
        print(self.enemy)


      # enemy[self.location] = Enemy(self.enemy)
      # window.fill((0, 0, 0))
      # Game_Text_1.text = enemy[self.location].text
      # if self.enemy not in enemy:
      #     Hint_text.text += enemy[self.location].explanation

# ------------------ CREATE GAME OBJECTS ---------------- #

game_state = GameState()
player = Player('')

# ------------------ CREATE GAME DICTS ---------------- #
room_dict = {player.location: Room()}
