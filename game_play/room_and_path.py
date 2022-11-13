''' Module containing all functions related to game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play.combat as gp
import game_play.chest as ch
import game_play.intro as i
import helper
import random

# -----------------------  FUNCTIONS ----------------------------#

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

