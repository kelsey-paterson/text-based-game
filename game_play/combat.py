''' Module containing all functions related to combat in game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play.chest as ch
import game_play.room_and_path as rp
import helper
import random

# -----------------------  FUNCTIONS ----------------------------#

def combat_attack_chance_calc(attack_type, a_weapon_strength):
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

def combat_defence_chance_calc(d_weapon_strength):
  '''Calculate player defence and randomly calculate hit bools from predetermined weightings'''
  evade_chance = go.player.luck * 0.5
  does_evade = helper.getRandom([True, False], (evade_chance, 1))
  # TODO: this calc is wierd, review at some stage
  defence = round(1.6 * (1 + ((go.player.defence + d_weapon_strength) / 10)), 0)

  return (does_evade, defence)
  

def combat_weapon_strength(attack_or_defence):
  weapon_strength = 1 # creates attack weapon strength parameter, default is 1 if weapon not in inventory
  for item in go.player.inventory.keys():
    if attack_or_defence == 'attack' and 'sword' in item:
      weapon_strength = go.player.inventory[item].attack
    elif attack_or_defence == 'defence' and 'shield' in item:
      weapon_strength = go.player.inventory[item].defence
  
  return weapon_strength

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
  
  
def display_evade_result(does_evade):
  '''Updates game screen depending on result of player evade/defend'''
  enemy = go.enemy[go.player.location]
  gdi.window.fill((0, 0, 0))
  if does_evade:
    gdi.Game_Text_1.text = 'You dodged the {}''s attack successfully!'.format(enemy.type)
    gdi.Game_Text_2.text = '(Press Enter)'
  elif not does_evade:
    gdi.Game_Text_1.text = 'Your dodge was unsuccessful. Your health has taken a hit'
    gdi.Game_Text_2.text = '(Press Enter)'

def combat_handle_enter(event):
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_RETURN:
      go.game_state.player_turn = not go.game_state.player_turn
      go.game_state.mid_combat_transition = False
      go.game_state.choose_defence = True
      go.game_state.choose_attack = True

def update_combat_stats(player_attack, is_hit, is_critical_hit):
  enemy = go.enemy[go.player.location]
  if is_hit and is_critical_hit:
    enemy.combat_health -= player_attack * 1.5

  elif is_hit:
    enemy.combat_health -= player_attack


def combat_player_turn(event):
  '''combat during player turn'''
  gdi.window.fill((0, 0, 0))

  if go.game_state.choose_attack:
    gdi.Game_Text_1.text = 'Choose your Attack... '
    gdi.Game_Text_2.text = '(Press L for Light and H for Heavy or P to use a potion)'
    attack = handle_choose_attack(event)

    if attack == 'light attack' or attack == 'heavy attack':
      weapon_strength = combat_weapon_strength('attack')
      (player_attack, is_hit, is_critical_hit) = combat_attack_chance_calc(attack, weapon_strength)

      display_attack_result(is_hit, is_critical_hit)
      update_combat_stats(player_attack, is_hit, is_critical_hit)
  elif not go.game_state.choose_attack:
    go.game_state.mid_combat_transition = True
    
def handle_choose_defence(event):
  '''handles user input for choosing defence'''
  if event.type == pg.KEYDOWN:
    # Evade
    if event.key == pg.K_e:
      outcome = 'evade'
      go.game_state.choose_defence = False
      return outcome
      # Hint_text.text = ''
    # Block
    elif event.key == pg.K_b:
      outcome = 'block'
      go.game_state.choose_defence = False
      return outcome
      # Hint_text.text = ''
    # Potion chosen
    elif event.key == pg.K_p:
      outcome = 'potion'
      go.game_state.choose_defence = False
      go.game_state.choose_potion = True
      return outcome

def combat_enemy_turn(event):
  '''combat during enemy turn'''
  enemy = go.enemy[go.player.location]
  gdi.window.fill((0, 0, 0))

  if go.game_state.choose_defence:
    gdi.Game_Text_1.text = 'The {} is attacking...'.format(enemy.type)
    gdi.Game_Text_2.text = '(Press E to evade, B to block or P to use a potion)'
    defence_type = handle_choose_defence(event)

    if defence_type == 'evade' or defence_type == 'block':
      weapon_strength = combat_weapon_strength('defence')
      (does_evade, enemy_attack_after_defence) = combat_defence_chance_calc(weapon_strength)
      if defence_type == 'evade':
        display_evade_result(does_evade)
        if not does_evade:
          go.player.combat_health -= enemy.attack

      elif defence_type == 'block':
        gdi.Game_Text_1.text = 'You partially defend the attack. Your health has taken a small hit'
        gdi.Game_Text_2.text = '(Press Enter)'
        go.player.combat_health -= enemy_attack_after_defence

  elif not go.game_state.choose_defence:
    go.game_state.mid_combat_transition = True
  #     if go.game_state.first_combat:
  #         Hint_text.text = gt.defend_hint_text

def end_of_combat():
  '''Returns true if end of combat conditions met'''
  enemy = go.enemy[go.player.location]
  if enemy.combat_health <= 0 or go.player.combat_health <= 0:
    return True
  else:
    return False

def game_over(event):
  pass

def end_of_combat_text():
  gdi.window.fill((0, 0, 0))
  enemy = go.enemy[go.player.location]
  if enemy.combat_health <= 0:
    gdi.Game_Text_1.text = 'The {} is defeated! You gained {} XP'.format(enemy.type, gd.xp_gained[enemy.type])
  else:
    gdi.Game_Text_1.text = 'Your health is depleted'
  gdi.Game_Text_2.text = '(Press Enter)'

def end_of_combat_handle_enter(event):
  enemy = go.enemy[go.player.location]
  if event.type == pg.KEYDOWN:
    if event.key == pg.K_RETURN:
      if enemy.combat_health <= 0:
        go.player.xp += gd.xp_gained[enemy.type]
        go.player.reset_combat()
        go.game_state.reset_combat()
        # gdi.window.fill((0, 0, 0))
      elif go.player.combat_health <= 0:
        game_over(event)

def engage_combat(event):
  '''Player is in combat'''
  # Clear game screen and hint text
  # gdi.window.fill((0, 0, 0))
    # Hint_text.text = ''
  enemy = go.room_dict[go.player.location].enemy

  if not end_of_combat():
    gdi.display_enemy_stats()
    if go.game_state.player_turn:
      combat_player_turn(event)
    else:
      combat_enemy_turn(event)
  elif end_of_combat():
    end_of_combat_text()
    end_of_combat_handle_enter(event)

