# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play as gp

# -----------------------  FUNCTIONS ----------------------------#

def clear_button_content():
  '''Clears all content from buttons'''
  gdi.Button1.update_label('')
  gdi.Button2.update_label('')
  gdi.Button3.update_label('')
  gdi.window.fill((0, 0, 0))

def handle_name_input(event):
  '''Take name input from user and save to player.name'''
  gdi.Input.handle_event(event)
  gdi.Input.draw()
  if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
    go.game_state.name_input = False
    go.game_state.pick_stats = True
    go.player.name = gdi.Input.player

def handle_pick_stats(event):
  '''handles user picking stats events'''
  gdi.display_pick_stats()
  gp.pick_stats(event)
  # room_dict[go.player.location] = go.Room()
  # if event.type == pg.KEYDOWN:
  #     if event.key == pg.K_RETURN and go.game_state.stats_picked:
      # go.player.inventory['wood sword'] = go.Item('wood sword')
  #         go.game_state.main_game = True
  #         go.game_state.choosing_path = True
  #         go.game_state.pick_stats = False
  #         go.game_state.first_room = True

def name_input_setup():
  '''Setup input box for player name'''
  gdi.Intro_Text_1.text = gd.welcome_text[1]
  gdi.Input.active = True
  go.game_state.start_game_menu = False
  go.game_state.name_input = True