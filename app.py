# Import python modules
import pygame as pg
pg.init()

# Import proprietary game modules
from game_data import *
from game_display import *
from game_objects import *
from game_play import *
from game_utils import *

# Set-up
fps = 200
fpsClock = pg.time.Clock()

# Create main game loop
while game_state.is_running:

  for event in pg.event.get():

    # Quits game if user presses escape
    if event.type == pg.QUIT:
      game_state.is_running = False

    # Game Intro Page
    elif game_state.start_game_menu:
      start_game_menu(event)

    # Input Player Name Page
    elif game_state.name_input:
      handle_name_input(event)

    # Pick Player Stats
    elif game_state.pick_stats:
      handle_pick_stats(event)

    # Main game window
    elif game_state.main_game:
      main_game(event)

  # Continually update game screen
  if game_state.main_game:
    gdi.display_main_game_screen()
  display_all_text()
  pg.display.flip()
  fpsClock.tick(fps)