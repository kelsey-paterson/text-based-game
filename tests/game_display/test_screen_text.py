# Tests for game display module

import unittest
from game_data import *
from game_display import *
import pygame as py
py.init()
  
class TestLimitTextWidth(unittest.TestCase):
  # Set up
  def setUp(self):
    some_text = ''
    text_x = 3
    text_y = 3
    font = pg.font.Font('fonts/BarcadeBrawlRegular-plYD.ttf', 12)
    line_length = 40
    line_space = 50
    self.test_text = ScreenText(some_text, text_x, text_y, font, line_length, line_space)

  def test_words_to_print(self):
    """Test that method returns a string of correct length"""
    text_to_test = 'Hello there, I am quite a long sentence that cannot fit on a single line'
    text_to_test = text_to_test.split()
    (resultant_words_to_print, resultant_word_count) = self.test_text.limit_text_width(text_to_test)      
    self.assertEqual(resultant_words_to_print, 'Hello there, I am quite a long sentence ')

  def test_word_count(self):
    """Test that method returns correct word count"""
    text_to_test = 'Hello there, I am quite a long sentence that cannot fit on a single line'
    text_to_test = text_to_test.split()
    (resultant_words_to_print, resultant_word_count) = self.test_text.limit_text_width(text_to_test)      
    self.assertEqual(resultant_word_count, 8)


  def tearDown(self):
    del self.test_text
    py.quit()





if __name__ == '__main__':
    unittest.main()