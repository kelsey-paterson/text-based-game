''' Module containing all functions related to game play'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_display as gdi
import game_play.combat as gp
import game_play.chest as ch
import game_play.room_and_path as rp
import game_play.combat as c
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


