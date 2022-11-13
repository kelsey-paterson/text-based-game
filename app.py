# Import python modules
import pygame as pg
import os
pg.init()

# Import proprietary game modules
from game_data import *
from game_display import *
from game_objects import *
from game_play.combat import *
from game_play.chest import *
from game_play.intro import *
from game_play.room_and_path import *
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
  
      if go.game_state.choosing_path:
        choose_path(event)
      elif go.game_state.view_room:
        view_room()
      elif go.game_state.room_transition:
        room_handle_enter(event)
      elif go.game_state.mid_combat_transition:
        combat_handle_enter(event)
      elif go.game_state.combat:
        engage_combat(event)
      elif go.game_state.chest:
        open_chest(event)
      elif go.game_state.chest_transition:
        chest_handle_enter(event)

  # Continually update game screen
  if game_state.main_game:
    gdi.display_main_game_screen()
  if game_state.combat:
    gdi.display_player_combat_health()
    gdi.display_enemy_stats()
    gdi.display_enemy_combat_health()
    # asurf = pg.image.load(os.path.join('images', 'bat.png'))
    # rect = asurf.get_rect()
    # rect.centery = 0
    # rect.left = 0
    # gdi.window.blit(asurf, rect)
  display_all_text()
  pg.display.flip()
  fpsClock.tick(fps)