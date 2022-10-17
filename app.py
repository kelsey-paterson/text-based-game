# Main game script

# Import python modules
import pygame as pg
pg.init()

# Import proprietary game modules

from game_data import *
from game_display import *
from game_objects import *
from game_play import *

# Create main game loop
while game_state.is_running:


  for event in pg.event.get():

    # Quits game if user presses escape
    if event.type == pg.QUIT:
      game_state.is_running = False

    # Game Intro Page
    elif game_state.start_game_menu:
      start_game_menu(event)

  # Continually update game screen
  pg.display.flip()
  