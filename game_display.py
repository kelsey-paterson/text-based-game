'''Module containing parameters & functions relating to content displaying on game screen'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
from game_objects import *
import game_data as gd

# -----------------------  PARAMETERS -------------------------- #

# Define game window size
window_width = 1440
window_height = 770


# Assign game window icon & title
logo = pg.image.load('images/sword.png')  # Load game logo
pg.display.set_icon(logo)                 # Set game logo
pg.display.set_caption('Rogue')           # Set title on game window

# -------------------------- CLASSES ---------------------------- #

class ClickButton:
  ''' Class for clickable button '''
  def __init__(self, label, x, y, font):
        self.label = label
        self.x = x
        self.y = y
        self.label_surface = font.render(self.label, True, (0, 255, 0))
        self.rect = self.label_surface.get_rect()
        self.rect.center = (self.x, self.y)
        self.font = font

  def display_button(self):
      pg.draw.rect(window, (0, 128, 0), self.rect)
      window.blit(self.label_surface, self.rect)

  def update_label(self, new_label):
      self.label = new_label
      self.label_surface = self.font.render(self.label, True, (0, 255, 0))
      self.rect = self.label_surface.get_rect()
      self.rect.center = (self.x, self.y)


class ScreenText:
    # font: object
  ''' Narration text displayed to the main window '''

  def __init__(self, some_text, text_x, text_y, font, line_length, line_space):
    self.text = some_text
    self.text_y = text_y
    self.text_x = text_x
    self.font = font
    self.length = line_length
    self.space = line_space
    self.temp_text = ''

  def display_text_line(self, words_to_print, text_line):
    ''' Display line of text on main window '''

    text_surface = self.font.render(words_to_print, True, (0, 128, 0))
    rect = text_surface.get_rect()
    rect.center = (self.text_x, text_line)
    window.blit(text_surface, rect)

  def limit_text_width(self, printable_words):
    ''' limit line length of text and print multiple lines '''
    
    # Set-up
    words_to_print = ''
    char_count = 0
    word_count = 0

    # Loops through each word in array
    for word in printable_words:
      word_count += 1
      char_count += (len(word) + 1)

      if word != '/':
          words_to_print += (word + ' ')  # adds words to string variable for printing

      if char_count >= self.length or word == '/':
          return (words_to_print, word_count)

      if word_count == len(printable_words):  # Once all words in array have been added to variable, print screen.
          return (words_to_print, word_count)

  def display_text(self):
    ''' Display text on main window '''

    # Set-up
    text_line = self.text_y
    words_to_print = ''
    printable_words = self.text.split()
    word_count_total = 0

    # Get line of text to print and print
    while word_count_total < len(printable_words):
      (words_to_print, word_count) = self.limit_text_width(printable_words)
      self.display_text_line(words_to_print, text_line)
      word_count_total += word_count


# ---------------------- OBJECTS ------------------------------- #

# Create game window
window = pg.display.set_mode((window_width, window_height), pg.DOUBLEBUF)

# Create game fonts
my_font = pg.font.Font('fonts/BarcadeBrawlRegular-plYD.ttf', 12)

# Create menu buttons
Button1 = ClickButton('Start Game', window_width / 2, 400, my_font)
Button2 = ClickButton('Load Game', window_width / 2, 450, my_font)
Button3 = ClickButton('Quit Game', window_width / 2, 500, my_font)
# Button4 = ClickButton('Menu', window_right_text_x + 50, window_height - 75, my_font)

# Create display texts
Intro_Text_1 = ScreenText(gd.welcome_text[0], window_width / 2, 250, my_font, 40, 50)

# ------------------------- FUNCTIONS --------------------------- #

def start_game_menu(event):
  '''function displays initial game menu'''

  Button1.display_button()
  Button2.display_button()
  Button3.display_button()
  Intro_Text_1.display_text()


