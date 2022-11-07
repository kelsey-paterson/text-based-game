# Contains all text and numeric data for game
welcome_text = ['Welcome to Rogue', 'Please enter Player name:']

game_intro_text = 'You enter the cave and find a wooden sword on the ground. There are dark passages ahead. ' \
                  'Which path will you take?'

game_intro_text2 = 'Press A to move left, D to move right or W to move forward'

stats = ['health', 'attack', 'defence', 'agility', 'luck']

explain = {
'health': 'How much attack you can withstand', 
'attack': 'How much damage your attacks land on your enemy', 
'defence': 'How much you can defend an incoming enemy attack', 
'agility': 'Chance of evading an incoming attack', 
'luck': 'Chance of good loot from chests and enemies'
}

# TODO: Tweak to improve gameplay
room_chances = {
  'chest': 10,
  'enemy': 20,
  'empty': 10
  }

# TODO: Refine the following probabilities for better gameplay.
enemy_chances = {
  '1': {
    'Bat': 100,
  },
  '2': {
    'Bat': 60,
    'Ogre': 40,
  },  
  '3': {
    'Bat': 10,
    'Ogre': 20,
    'Troll': 10
  },
  '4': {
    'Bat': 60,
    'Ogre': 40,
  }
  
}

chest_text = 'You find an old wooden chest.'
empty_text = 'The room is empty'

bat_text = 'A Bat swooped in from the ceiling....'
bat_text_explain = 'GAME HINT: / Bats are highly evasive but don''t pack much of a punch.'

ogre_text = 'A horribly ugly ogre has appeared out of the darkness....'
ogre_text_explanation = 'GAME HINT: / Ogres have high defence but are very slow'

troll_text = 'Oh no. They have a cave troll....'
troll_text_explanation = 'GAME HINT: / Trolls pack a heavy hit but are very slow'

dragon_text = 'Dear lord..is that a....?'
dragon_text_explanation = 'GAME HINT: / Dragons are the worst type of enemy you could hope to meet in the ' \
                          'dungeons..gah maybe you should high tail it out of there!'

have_object_text = 'Drat! I already have one of those.'

attack_hint_text = 'GAME HINT: / / Light attacks deal a bit of damage but have a higher chance of connecting with ' \
                   'your enemy. / ' \
                   ' / Heavy attacks deal a big hit but are slow to be delivered. Your enemy has a ' \
                   'chance to evade. / / Try mixing your attack type, depending on the enemy you face.'

defend_hint_text = 'GAME HINT: / / Evade - use your agility to attempt to dodge enemy attacks / / Block - hunker down ' \
                   'to defend the ' \
                   'enemy blow.'

health_stat_explanation = 'How much attack you can withstand'
attack_stat_explanation = 'How much damage your attacks land on your enemy'
defence_stat_explanation = 'How much you can defend an incoming enemy attack'
agility_stat_explanation = 'Chance of evading an incoming attack'
luck_stat_explanation = 'Chance of good loot from chests and enemies'


def create_map():
  # TODO: Make dynamic, so map extents can be readily changed
  room_map = [[str(x) + y for y in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']] for x in range(1, 10)]
  available_paths = {}

  for i in range(len(room_map)):
      for j in range(len(room_map[0])):
          if '1' in room_map[i][j]:
              available_paths[room_map[i][j]] = ['A', 'W', 'D']
          else:
              available_paths[room_map[i][j]] = ['A', 'W', 'D', 'S']
          if 'a' in room_map[i][j]:
              available_paths[room_map[i][j]].remove('A')
          if 'j' in room_map[i][j]:
              available_paths[room_map[i][j]].remove('D')

  return (room_map, available_paths)


room_map, available_paths = create_map()