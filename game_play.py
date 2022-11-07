''' Module containing all functions related to game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play as gp

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
  gdi.display_main_game_screen()
  if go.game_state.choosing_path:
    choose_path(event)
  elif go.game_state.view_room:
    view_room()
  elif go.game_state.combat:
    combat()
  elif go.game_state.chest:
    open_chest()

def choose_path(event):
  pass
  # Hint_text.text = ''
  print(event.type)
  # print(event.key)
  if event.type == pg.KEYDOWN:
    if event.key in (pg.K_a, pg.K_w, pg.K_s, pg.K_d):
      go.player.move(event.key)
      enter_room()

def enter_room():
  if go.player.location not in go.room_dict.keys():
    # If new room, update room dict with current room
    go.room_dict[go.player.location] = go.Room()
    go.room_dict[go.player.location].generate_room_content()
    # go.game_states.first_room = False
    go.game_state.view_room = True
  else:
    pass
      # been_in_room()
      # go.game_states.choosing_path = True

def combat():
  '''Player is in combat'''
  pass

def open_chest():
  '''Player enters room with a chest'''
  pass

def view_room():
  print('viewing room now...')
  current_room = go.room_dict[go.player.location]
  current_room.generate_room_text()

