''' Module containing all functions related to game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play.combat as c
import game_play.intro as i
import game_play.room_and_path as rp
import helper
import random

# -----------------------  FUNCTIONS ----------------------------#

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
  '''Given a player level, generates the chance for given item type'''
  # TODO: rewrite chance dict and following code to be more concise
  chances = []
  level_index = int(player_level) - 1
  if item_category == 'sword' or item_category == 'shield':
    for item in gd.chest_chance_dict[item_category].values():
      chances.append(item[level_index] * go.player.luck)

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


def chest_handle_enter(event):
  '''Handle enter after chest opened'''

  if event.type == pg.KEYDOWN:
    if event.key == (pg.K_RETURN):
      go.game_state.choosing_path = True








