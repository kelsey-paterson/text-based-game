''' Module containing all functions related to game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play as gp
import helper
import random

# -----------------------  FUNCTIONS ----------------------------#

def pick_stats(event):
    '''User picks which stats they want'''

    # All stats have been chosen
    if go.game_state.stat_num == 2:
      gdi.Intro_Text_1.text = 'Press enter to confirm'
      if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
        prepare_game()

        # Move to next game_state
        go.game_state.pick_stats = False
        go.game_state.main_game = True

    elif event.type == pg.MOUSEBUTTONDOWN:

      for stat in gd.stats:
        #Get add & minus button for particular stat
        add_button = gdi.AddButton[stat]
        minus_button = gdi.MinusButton[stat]

        # if the add button clicked, increment player object stat
        if add_button.rect.collidepoint(event.pos):
          player_stat = getattr(go.player, stat)
          setattr(go.player, stat, player_stat + 1) 
          go.game_state.stat_num += 1
      
        # if the minus button clicked, decrement player object stat
        if minus_button.rect.collidepoint(event.pos):
          player_stat = getattr(go.player, stat)
          setattr(go.player, stat, player_stat - 1) 
          go.game_state.stat_num += 1

    for button in gdi.AddButton.values():
      button.display_button()

    for button in gdi.MinusButton.values():
      button.display_button()

def prepare_game():
  
  # Set game text to display
  gdi.Game_Text_1.text = gd.game_intro_text
  gdi.Game_Text_2.text = gd.game_intro_text2

  # Set intro text to display nothing
  gdi.Intro_Text_1.text = ''
  # gdi.Intro_Text_2.text = ''

  # Set buttons to display nothing
  for button in gdi.AddButton.values():
    button.update_label('')
  for button in gdi.MinusButton.values():
    button.update_label('')

  # Clear screen
  gdi.window.fill((0, 0, 0))


def main_game(event):
  if go.game_state.choosing_path:
    choose_path(event)
  elif go.game_state.view_room:
    view_room()
  elif go.game_state.room_transition:
    room_handle_enter(event)
  elif go.game_state.combat:
    combat(event)
  elif go.game_state.chest:
    open_chest(event)
  elif go.game_state.chest_transition:
    chest_handle_enter(event)

def choose_path(event):
  # Hint_text.text = ''
  if not go.game_state.first_room:
    display_choosing_path_text()
  if event.type == pg.KEYDOWN:
    if event.key in (pg.K_a, pg.K_w, pg.K_s, pg.K_d):
      go.player.move(event.key)
      go.game_state.view_room = True

def view_room():
  if go.player.location not in go.room_dict.keys():
    # If new room, update room dict with current room
    go.room_dict[go.player.location] = go.Room()
    go.room_dict[go.player.location].generate_room_content()
    go.room_dict[go.player.location].generate_room_text()
    go.game_state.first_room = False
    go.game_state.view_room = False
    go.game_state.room_transition = True
  else:
    # TODO: Complete for case where been in room
    pass
      # been_in_room()
      # go.game_states.choosing_path = True

def combat():
  '''Player is in combat'''
  pass

def chest_generate_item_category():
  '''Randomly chooses item category to be in chest'''
  chest_options = list(gd.chest_chances.keys())
  chest_chances = list(gd.chest_chances.values())
  return helper.getRandom(chest_options, chest_chances)

def chest_generate_item_type(item_category):
  '''Given item category, randomly chooses item type'''
  player_level = go.player.location[0]
  item = ''

  if item_category == 'sword' or item_category == 'shield':
    type_chances = get_item_chances(player_level, item_category)
    types = list(gd.chest_chance_dict[item_category].keys())
    item = helper.getRandom(types, type_chances)

  elif item_category == 'potion':
    potion_types = gd.chest_chance_dict[item_category]['types']
    type = random.choice(potion_types)
    strength_types = list(gd.chest_chance_dict[item_category]['potion_strength'].keys())
    strength_chances = list(gd.chest_chance_dict[item_category]['potion_strength'].values())
    strength = helper.getRandom(strength_types, strength_chances)
    item = strength + ' ' + type
  
  return item

def get_item_chances(player_level, item_category):
  '''Given a player level, generates the chance for given type'''
  # TODO: rewrite chance dict and following code to be more concise
  chances = []
  level_index = int(player_level) - 1
  if item_category == 'sword' or item_category == 'shield':
    for item in gd.chest_chance_dict[item_category].values():
      chances.append(item[level_index]*go.player.luck)

  return chances

def chest_generate_open_text(item_name):
  gdi.window.fill((0, 0, 0))
  gdi.Game_Text_1.text = 'You found a {} ........'.format(item_name)
  gdi.Game_Text_2.text = '(Press Enter)'


def open_chest(event):
  '''Player opens chest'''
  # TODO: Luck variable should factor into result.
  item_category = chest_generate_item_category()
  item_type = chest_generate_item_type(item_category)
  item_name = item_type + ' ' + item_category
  chest_generate_open_text(item_name)
  go.player.inventory[item_name] = go.Item(item_category, item_type, item_name)
  go.game_state.chest_transition = True  
  go.game_state.chest = False

  # go.player.check_inventory(item_category, item_type)
  # if chest_contains == 'shield' and go.player.first_shield:
  #     gdi.Hint_text.text = 'GAME HINT: / A shield reduces or blocks part of an enemy attack'
  #     go.player.first_shield = False
  # chest_contains = ''
  # self.chest_opened = True

  # if player.first_potion:
  #     Hint_text.text = 'GAME HINT: / You can use a potion during combat to temporarily increase your stats'
  #     player.first_potion = False
  # if item_name in player.inventory.keys():
  #     Game_Text_1.text += gt.have_object_text
  # else:
  #     player.inventory[item_name] = Item(item_name)
  # self.chest_opened = True

def room_handle_enter(event):
  '''Handle enter from room content outcome'''
  if event.type == pg.KEYDOWN:
    if event.key == (pg.K_RETURN):
      if go.room_dict[go.player.location].content == 'chest':
        go.game_state.chest = True
        go.game_state.room_transition = False
      elif go.room_dict[go.player.location].content == 'enemy':
        go.game_state.combat = True
        go.game_state.room_transition = False
      else:
        # Room is empty
        go.game_state.choosing_path = True
        go.game_state.room_transition = False

def chest_handle_enter(event):
  '''Handle enter after chest opened'''

  if event.type == pg.KEYDOWN:
    if event.key == (pg.K_RETURN):
      go.game_state.choosing_path = True

def display_choosing_path_text():
  # TODO: Update dynamically depending on map position
  gdi.window.fill((0, 0, 0))
  gdi.Game_Text_1.text = 'choose a path'
  gdi.Game_Text_2.text = 'press this or that'



