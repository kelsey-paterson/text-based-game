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

# GAME INTRO 

def pick_stats(event):
    '''User picks which stats they want'''

    # When all stats have been chosen
    if go.game_state.stat_num == 2:
      gdi.Intro_Text_1.text = 'Press enter to confirm'
      if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
        prepare_game_screen()

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

def prepare_game_screen():
  '''Prepares game screen for main game display'''
  
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


# CHOOSING PATH & VIEWING ROOM 


def display_choosing_path_text():
  # TODO: Update dynamically depending on map position
  gdi.window.fill((0, 0, 0))
  gdi.Game_Text_1.text = 'choose a path'
  gdi.Game_Text_2.text = 'Press A to move left, D to move right or W to move forward'

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
      # go.go.game_state.choosing_path = True

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

# COMBAT

def use_potion(potion_names, p_type, event):
  pass
    # # Finds the name of selected potion from player inventory based on type choosen by player.
    # potion_named = ''
    # for i in potion_names:
    #     if p_type in i:
    #         potion_named = i

    # if p_type == 'health':
    #     player.combat_health += player.inventory[potion_named].health
    # if p_type == 'attack':
    #     player.combat_attack += player.inventory[potion_named].attack
    # if p_type == 'agility':
    #     player.combat_agility += player.inventory[potion_named].agility

    # # go.game_state.choose_attack = True
    # # go.game_state.choose_potion = False

def which_potion(event):
  pass
    # potion_count = 0
    # potion_names = []
    # keys = []
    # potion_types = []
    # window.fill((0, 0, 0))

    # for i in player.inventory.keys():  # Potion
    #     if 'potion' in i:
    #         potion_count += 1
    #         potion_names.append(i)

    # if potion_count == 0:
    #     Text_1.text = 'You don''t have any potions'
    #     Text_2.text = '(Press enter to go back to choosing attack)'
    #     if event.type == pg.KEYDOWN:
    #         if event.key == pg.K_RETURN:
    #             go.game_state.choose_attack = True
    #             go.game_state.choose_potion = False

    # if potion_count > 0:
    #     for i in potion_names:
    #         if 'agility' in i:
    #             keys.append('S')
    #             potion_types.append('agility')
    #         if 'health' in i:
    #             keys.append('H')
    #             potion_types.append('health')
    #         if 'attack' in i:
    #             keys.append('A')
    #             potion_types.append('attack')

    #     if potion_count == 1:
    #         Text_2.text = ''
    #         Text_1.text = 'To use your {} potion, Press Enter'.format(potion_types[0])
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_RETURN:
    #                 use_potion(potion_names, potion_types[0], event)

    #     else:
    #         Text_1.text = 'Which potion do you want to use?'
    #         Text_2.text = 'Press'
    #         for i in range(potion_count-1):
    #             Text_2.text += ' {} for {},'.format(keys[i], potion_types[i])
    #         Text_2.text = Text_2.text[:-1] + 'and {} for {}.'.format(keys[potion_count], potion_types[potion_count])
    #         Text_2.text = 'and' + Text_2.text[:-1]
    #         if event.type == pg.KEYDOWN:
    #             if event.key == pg.K_a and 'attack' in potion_types:
    #                 p_type = 'attack'
    #             if event.key == pg.K_s and 'agility' in potion_types:
    #                 p_type = 'agility'
    #             if event.key == pg.K_h and 'health' in potion_types:
    #                 p_type = 'health'
    #             use_potion(potion_names, p_type, event)


def combat_chance_calc(attack_type, a_weapon_strength):
  '''Calculate player attack and randomly calculate hit bools from predetermined weightings'''
  # Parameters used
  attack_factors = gd.combat_factors[attack_type]
  attack_factor = attack_factors['attack']
  is_hit_factor = attack_factors['is_hit'] * go.player.luck
  critical_hit_factor = attack_factors['critical_hit'] * go.player.luck

  # Calculations:
  player_attack = round(attack_factor * (1 + ((go.player.attack + a_weapon_strength) / 10)), 0)
  is_hit = helper.getRandom([True, False], (is_hit_factor, 1))
  is_critical_hit = helper.getRandom([True, False], (critical_hit_factor, 1))
  return (player_attack, is_hit, is_critical_hit)


def combat_weapon_strength(attack_or_defence):
  weapon_strength = 1 # creates attack weapon strength parameter, default is 1 if weapon not in inventory
  for item in go.player.inventory.keys():
    if attack_or_defence == 'attack' and 'sword' in item:
      weapon_strength = go.player.inventory[item].attack
    elif attack_or_defence == 'defence' and 'shield' in item:
      weapon_strength = go.player.inventory[item].defence
  
  return weapon_strength

def combat_enemy_turn():
  '''combat during enemy turn'''
  pass

def handle_choose_attack(event):
  '''handles user input for choosing attack'''
  if event.type == pg.KEYDOWN:
    # Light attack
    if event.key == pg.K_l:
      outcome = 'light attack'
      go.game_state.choose_attack = False
      return outcome
      # Hint_text.text = ''
    # Heavy attack
    elif event.key == pg.K_h:
      outcome = 'heavy attack'
      go.game_state.choose_attack = False
      return outcome
      # Hint_text.text = ''
    # Potion chosen
    elif event.key == pg.K_p:
      outcome = 'potion'
      go.game_state.choose_attack = False
      go.game_state.choose_potion = True
      return outcome
  

def generate_combat_hints():
  if go.game_state.first_combat:
    pass
  # TODO: complete hint text
  # Hint_text.text = gt.attack_hint_text

def handle_choose_potion(event):
  # TODO: Complete below function for selecting a potion
  # which_potion(event)
  pass

def display_attack_result( is_hit, is_critical_hit):
  '''Updates game screen depending on result of player attack'''
  enemy = go.enemy[go.player.location]
  gdi.window.fill((0, 0, 0))
  if is_hit and is_critical_hit:
    gdi.Game_Text_1.text = 'The {} took a critical hit!'.format(enemy.type)
  elif is_hit:
    gdi.Game_Text_1.text = 'The {} took a direct hit!'.format(enemy.type)
  else:
    gdi.Game_Text_1.text = 'Your attack missed!'
  
  gdi.Game_Text_2.text = '(Press Enter)'

def combat_player_turn_handle_enter(event):
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_RETURN:
        go.game_state.player_turn = False
        # go.game_state.choose_defence = True

def update_combat_stats(player_attack, is_hit, is_critical_hit):
  enemy = go.enemy[go.player.location]
  if is_hit and is_critical_hit:
    enemy.combat_health -= player_attack * 1.5

  elif is_hit:
    enemy.combat_health -= player_attack


def combat_player_turn(event):
  '''combat during player turn'''

  if go.game_state.choose_attack:
    gdi.Game_Text_1.text = 'Choose your Attack... '
    gdi.Game_Text_2.text = '(Press L for Light and H for Heavy or P to use a potion)'
    attack = handle_choose_attack(event)

    if attack == 'light attack' or attack == 'heavy attack':
      weapon_strength = combat_weapon_strength('attack')
      (player_attack, is_hit, is_critical_hit) = combat_chance_calc(attack, weapon_strength)

      display_attack_result(is_hit, is_critical_hit)
      update_combat_stats(player_attack, is_hit, is_critical_hit)
  elif not go.game_state.choose_attack:
    combat_player_turn_handle_enter(event)

def combat_enemy_turn(event):
  pass
  # if go.game_state.player_turn == 'enemy':
  #     gdi.Game_Text_1.text = 'The {} is attacking... '.format(enemy.type)
  #     gdi.Game_Text_2.text = '(Press E to attempt to evade, B to block or P to use a potion)'
  #     if go.game_state.first_combat:
  #         Hint_text.text = gt.defend_hint_text

  #     if go.game_state.choose_defence:
  #         if event.type == pg.KEYDOWN:
  #             if event.key == pg.K_e:
  #                 go.game_state.evade = random.choices(['Yes', 'No'], weights=(player.luck * 0.5, 1), k=1)[0]
  #                 go.game_state.e_attack = enemy.attack
  #                 go.game_state.choose_defence = False
  #                 go.game_state.defend = 'No'
  #                 go.game_state.first_combat = False
  #                 Hint_text.text = ''
  #             if event.key == pg.K_b:
  #                 go.game_state.defend = 'Yes'
  #                 go.game_state.e_attack = round(1.6 * (1 + ((player.defence + d_weapon_strength) / 10)), 0)
  #                 go.game_state.choose_defence = False
  #                 go.game_state.first_combat = False
  #                 Hint_text.text = ''

  #     if not go.game_state.choose_defence:
  #         if go.game_state.evade == 'Yes':
  #             gdi.Game_Text_1.text = 'You dodged the {}''s attack successfully!'.format(enemy.type)
  #             gdi.Game_Text_2.text = '(Press Enter)'
  #             if event.type == pg.KEYDOWN:
  #                 if event.key == pg.K_RETURN:
  #                     go.game_state.player_turn = 'player'
  #                     go.game_state.choose_attack = True

  #         if go.game_state.evade == 'No':
  #             gdi.Game_Text_1.text = 'Your dodge was unsuccessful. Your health has taken a hit'
  #             gdi.Game_Text_2.text = '(Press Enter)'
  #             player.combat_health -= go.game_state.e_attack
  #             go.game_state.e_attack = 0
  #             if event.type == pg.KEYDOWN:
  #                 if event.key == pg.K_RETURN:
  #                     go.game_state.player_turn = 'player'
  #                     go.game_state.choose_attack = True

  #         if go.game_state.defend == 'Yes':
  #             gdi.Game_Text_1.text = 'You partially defend the attack. Your health has taken a small hit'
  #             gdi.Game_Text_2.text = '(Press Enter)'
  #             player.combat_health -= go.game_state.e_attack
  #             go.game_state.e_attack = 0
  #             if event.type == pg.KEYDOWN:
  #                 if event.key == pg.K_RETURN:
  #                     go.game_state.player_turn = 'player'
  #                     go.game_state.choose_attack = True

def end_of_combat():
  '''Returns true if end of combat conditions met'''
  enemy = go.enemy[go.player.location]
  pass
  if enemy.health <= 0:
    return True
  elif go.player.combat_health <= 0:
    return True
#   if enemy.combat_health <= 0:
#     xp_gained = {'Bat': 10, 'Ogre': 20, 'Troll': 30, 'Dragon': 50}
#     gdi.Game_Text_1.text = 'The {} is defeated! You gained {} XP'.format(enemy.type, xp_gained[enemy.type])
#     gdi.Game_Text_2.text = '(Press Enter)'
#     Hint_text.text = ''
#     go.game_state.first_combat = False
#     if event.type == pg.KEYDOWN:
#         if event.key == pg.K_RETURN:
#             player.xp += xp_gained[enemy.type]
#             go.game_state.choosing_path = True
#             go.game_state.in_combat = False
#             go.game_state.view_room = False
# if player.combat_health <= 0:
#     gdi.Game_Text_1.text = 'Your health is depleted'
#     gdi.Game_Text_2.text = '(Press Enter)'
#     # TODO: Finish game_over function
#     if event.type == pg.KEYDOWN:
#         if event.key == pg.K_RETURN:
#             game_over(event)

# if not go.game_state.game_over:


def engage_combat(event):
  '''Player is in combat'''
  # Clear game screen and hint text
  gdi.window.fill((0, 0, 0))
    # Hint_text.text = ''
  enemy = go.room_dict[go.player.location].enemy

  if not end_of_combat():
    gdi.display_enemy_stats(enemy)
    gdi.display_player_combat_health()
    if go.game_state.player_turn:
      combat_player_turn(event)
    else:
      combat_enemy_turn(event)
  elif end_of_combat():
    print('combat over...')


# CHEST 


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

# MAIN GAME 

def main_game(event):
  '''Moving between main game states (and transition states)'''
  
  if go.game_state.choosing_path:
    choose_path(event)
  elif go.game_state.view_room:
    view_room()
  elif go.game_state.room_transition:
    room_handle_enter(event)
  elif go.game_state.combat:
    engage_combat(event)
  elif go.game_state.chest:
    open_chest(event)
  elif go.game_state.chest_transition:
    chest_handle_enter(event)





