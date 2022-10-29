'''Module containing parameters & functions relating to content displaying on game screen'''

# ---------------------  IMPORT MODULES -------------------------#
import pygame as pg
pg.init()
import game_objects as go
import game_data as gd
import game_utils as gu
import helper

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
      self.display_button() #Added to eliminate displaying after updating button, check it works !!

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

      # next line character found
      if word == '/':
        return (words_to_print, word_count)

      # number of characters exceeds set line length
      elif char_count >= self.length: 
        words_to_print += (word + ' ')
        return (words_to_print, word_count)

      # all words left in printable words have been added
      elif word_count == len(printable_words):  
        words_to_print += (word + ' ')
        return (words_to_print, word_count)

      else:
        words_to_print += (word + ' ')


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

class InputBox:
    '''Input box for user to set thier name'''

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = pg.Color((0, 128, 0))
        self.text = text
        self.player = ''
        self.text_surface = my_font_12.render(text, True, self.color)
        self.active = False
        self.location = '1e'
        self.rect.center = (x, y) #Automatically centers on screen - modify if there will need to be variations of this.


    def handle_event(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                Intro_Text_1.text = 'Welcome, {}. Please pick your player stats:'.format(self.text)
                self.player = self.text
                self.text = ''
                self.color = pg.Color(0, 0, 0)
                self.text_surface = my_font_12.render(self.text, True, self.color)
                window.fill((0, 0, 0))
                self.draw()
                self.active = False
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
                window.fill((0, 0, 0))
            else:
                self.text += event.unicode
            self.text_surface = my_font_12.render(self.text, True, self.color)

    def draw(self):
        window.blit(self.text_surface, (self.rect.x + 5, self.rect.y + 5))
        pg.draw.rect(window, self.color, self.rect, 2)

    def reset(self):
        pass
        # TODO: To reset input box to take input as in start of game.

# -----------------------  PARAMETERS -------------------------- #

# Define game window size
window_width = 1440
window_height = 770

# Define name input box parameters
input_x_position = window_width / 2
input_y_position = 400
input_width = 150
input_height = 30

# Statistics display parameters
stat_y_start = 400
stat_x = 530

# Define game text parameters
#TODO: replace numbers with parameters in making game_text

# Define left pane parameters
window_left_text_x = 15
inventory_y = 30
map_box_x = 120
map_box_y = 300
left_pane_xlimit = 375

# Define right pane parameters
window_right_text_x = 1300
player_stats_y = 30
xp_y = 200
right_pane_xlimit = 1275


# Assign game window icon & title
logo = pg.image.load('images/sword.png')  # Load game logo
pg.display.set_icon(logo)                 # Set game logo
pg.display.set_caption('Rogue')           # Set title on game window

# ---------------------- OBJECTS ------------------------------- #

# Create game window
window = pg.display.set_mode((window_width, window_height), pg.DOUBLEBUF)

# Create game fonts
my_font_12 = pg.font.Font('fonts/BarcadeBrawlRegular-plYD.ttf', 12)
my_font_7 = pg.font.Font('fonts/BarcadeBrawlRegular-plYD.ttf', 7)
my_font_8 = pg.font.Font('fonts/BarcadeBrawlRegular-plYD.ttf', 8)

# Create menu buttons
Button1 = ClickButton('Start Game', window_width / 2, 400, my_font_12)
Button2 = ClickButton('Load Game', window_width / 2, 450, my_font_12)
Button3 = ClickButton('Quit Game', window_width / 2, 500, my_font_12)
# Button4 = ClickButton('Menu', window_right_text_x + 50, window_height - 75, my_font)

# Create display texts
Intro_Text_1 = ScreenText(gd.welcome_text[0], window_width / 2, 250, my_font_12, 40, 50)
Game_Text_1 = ScreenText('', 850, 250, my_font_12, 40, 50)
Game_Text_2 = ScreenText('', 850, 425, my_font_12, 40, 50)


# Create name input box
Input = InputBox(input_x_position, input_y_position, input_width, input_height)

# ------------------------- FUNCTIONS --------------------------- #

def start_game_menu(event):
  '''function displays initial game menu'''

  start_game_menu_handleclick(event)

  Button1.display_button()
  Button2.display_button()
  Button3.display_button()
  Intro_Text_1.display_text()


def start_game_menu_handleclick(event):
  '''handles button clicks in main menu'''
  if event.type == pg.MOUSEBUTTONDOWN:

    # Start game button clicked
    if start_button_clicked(event):
      gu.clear_button_content()
      gu.name_input_setup()

    # Load game button clicked
    elif load_button_clicked(event):
      gu.clear_button_content()
      #TODO: write load game function
      # load_game()

    # Quit game button clicked
    elif Button3.rect.collidepoint(event.pos):
        go.game_state.is_running = False


def start_button_clicked(event):
  return Button1.rect.collidepoint(event.pos)


def load_button_clicked(event):
  return Button2.rect.collidepoint(event.pos)


def display_pick_stats() -> object:
  window.fill((0, 0, 0))
  stat_y = stat_y_start

  # For each player stat type, display stat value + increment buttons
  for stat in gd.stats:
    display_individual_stat(stat, stat_y)
    #Add description of stat next to it.
    display_explain_stat(stat, stat_y)
    AddButton[stat] = ClickButton('+', stat_x + 200, stat_y, my_font_12)
    AddButton[stat].display_button()
    MinusButton[stat] = ClickButton('-', stat_x + 220, stat_y, my_font_12)
    MinusButton[stat].display_button()
    stat_y += 25


def display_individual_stat(stat, stat_y):
  player_stat = getattr(go.player, stat)
  text_surface = my_font_12.render(stat + ':   ' + str(player_stat), True, (0, 128, 0))
  rect = text_surface.get_rect()
  rect.centery = stat_y
  rect.left = stat_x
  window.blit(text_surface, rect)


def display_all_text():
    Game_Text_1.display_text()
    Game_Text_2.display_text()
    Intro_Text_1.display_text()
    # Intro_Text_2.display_text()
    # go.Hint_text.display_text()


def display_explain_stat(stat, stat_y):
  '''Adds explanation text for each stat field'''
  explanation = my_font_7.render(gd.explain[stat], True, (0, 128, 0))
  explanation_rect = explanation.get_rect()
  explanation_rect.centery = stat_y
  explanation_rect.left = stat_x + 295
  window.blit(explanation, explanation_rect)


def display_main_game_screen():
  '''Calls all functions that display main game elements on screen'''
  #display right pane content
  display_stats(window_right_text_x, player_stats_y)
  display_xp_level(window_right_text_x, xp_y)
  #draw right pane bounding line
  pg.draw.line(window, (0, 128, 0), (right_pane_xlimit, 0), (right_pane_xlimit, window_height))
  #display left pane content
  display_inventory(window_left_text_x, inventory_y)
  display_map(map_box_x, map_box_y)
  #draw left pane bounding line
  pg.draw.line(window, (0, 128, 0), (left_pane_xlimit, 0), (left_pane_xlimit, window_height))


def display_inventory(x, y):
  '''Displays the players inventory on the screen'''
  gap = '     '
  inventory = 'Inventory' + gap + 'Attack  Defence  Agility  Health'
  helper.render_text(inventory, x, y, my_font_7)
  lines = 1
  for item in go.player.inventory.keys():
    # Render the name of item
    helper.render_text(str(item), x, (25 * lines) + y, my_font_7)
    # Render the properties of the item
    item_properties_string = item_properties_string(item)
    helper.render_text(item_properties_string, x, (25 * lines) + y, my_font_7)
    lines += 1


def item_properties_to_string(item):
  '''Takes in an inventory item and returns the properties as spaced string for display'''
  item_properties = ['attack', 'defence', 'agility', 'health']
  string = ''
  print_gap = '       '
  for property in item_properties:
    string += getattr(go.player.inventory[item], property) + print_gap
  return string


def display_stats(x, y):
  '''Displays player stats during normal game play'''
  stats_for_display = modify_stat_string_for_display(gd.stats)
  for stat in stats_for_display:
    helper.render_text(stat, x, y, my_font_7)
    y += 25


def modify_stat_string_for_display(stats):
  '''Takes the stats array and reformats the string so it displays correctly on screen then
  adds the value of the player.stat attribute'''
  gap = '    '
  new_array = ['Player Stats:' + gap]
  for stat in stats:
    player_stat_value = str(getattr(go.player, stat))
    stat = stat.capitalize()
    stat += gap + player_stat_value
    new_array.append(stat)
  return new_array


def display_map(x, y):
  '''Displays the map and current player location on main game screen'''
  color = pg.Color((0, 128, 0))
  map_box_width = len(gd.room_map[0]) * 17
  helper.render_text('Room Map', x + 30, y - 20, my_font_7)
  helper.draw_box(x, y, map_box_width, map_box_width, color, 1)
  #TODO: Complete the below, figure out what it is doing first...
  # for i in go.player.rect_map:
  #     pg.draw.rect(window, color, i, 0)


def display_xp_level(x, y):
  '''Displays player xp_level'''
  total_length = 100
  length = go.player.xp
  text = 'XP Level   {}/100'.format(go.player.xp)
  text_2 = 'Player Level: {}'.format(go.player.level)
  helper.render_text(text, x, y, my_font_7)
  helper.render_text(text_2, x, y + 25, my_font_7)
  colour = pg.Color((0, 128, 0))
  #Draw containing xp bar box
  helper.draw_box(x, y - 25, total_length, 10, colour, 1)
  #Draw xp level bar
  helper.draw_box(x, y - 25, length, 10, colour, 0)

# ------------------ CREATE DISPLAY DICTS ---------------- #
AddButton = {}
MinusButton = {}