# Tests for game display module

import unittest
# from game_data import *
# from game_display import *
from game_objects import *
import pygame as py
py.init()
  
class TestMove(unittest.TestCase):
  # Set up
  def setUp(self):
    self.test_player = Player('test_player')
    self.test_player.x = 4

  def test_move_left(self):
    """Test that player moves left"""
    player_position = self.test_player.x
    self.test_player.move(event_key)     
    self.assertEqual(self.test_player.x, player_position + 1)

  def test_move_right(self):
    """Test that player moves right"""
    player_position = self.test_player.x
    self.test_player.move(event_key)    
    self.assertEqual(self.test_player.x, player_position - 1)

  def test_move_forward(self):
    """Test that player moves forward"""
    player_position = self.test_player.y
    self.test_player.move(event_key)
    self.assertEqual(self.test_player.y, player_position + 1)

  def test_move_back(self):
    """Test that player moves backward"""
    player_position = self.test_player.y
    self.test_player.move(event_key)
    self.assertEqual(self.test_player.y, player_position - 1)

  def test_upper_bound_x(self):
    """Test that player does not move above 9 in x"""
    self.test_player.x = 9
    self.test_player.move(event_key)
    self.assertEqual(self.test_player.x, 9)

  def test_lower_bound_x(self):
    """Test that player does not move below 0 in x"""
    self.test_player.x = 0
    self.test_player.move(event_key)
    self.assertEqual(self.test_player.x, 0)

  def test_lower_bound_y(self):
    """Test that player does not move below 0 in y"""
    self.test_player.y = 0
    self.test_player.move(event_key)
    self.assertEqual(self.test_player.y, 0)

  def tearDown(self):
    del self.test_player
    py.quit()

if __name__ == '__main__':
    unittest.main()