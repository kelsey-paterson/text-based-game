# Tests for game display module

import unittest
# from game_data import *
# from game_display import *
from game_objects import *
import pygame as py
py.init()
  
class generate_room_content(unittest.TestCase):
  # Set up
  def setUp(self):
    # set-up stuff
    test_room = Room()

  def test_enemy_created(self):
    """Test """
    # Change chances to force result
    self.test_room.generate_room_content    
    self.assertEqual(self.test_room.content, 'Enemy')

  def test_chest_created(self):
    """Test """
    # Change chances to force result
    self.test_room.generate_room_content    
    self.assertEqual(self.test_room.content, 'Chest')

  def test_empty_created(self):
    """Test """
    # Change chances to force result
    self.test_room.generate_room_content    
    self.assertEqual(self.test_room.content, 'Chest')


  def tearDown(self):
    del self.test_room
    py.quit()
    # Update chance object to original values.

if __name__ == '__main__':
    unittest.main()