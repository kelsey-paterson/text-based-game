# Main game script

# Import python modules
import pygame as pg

# Import proprietary game modules

from game_data import *
from game_display import *
from game_objects import *

# Create main game while loop
while game_state.is_running:

    for event in pg.event.get():

        # If user presses escape
        if event.type == pg.QUIT:
            game_state.is_running = False
