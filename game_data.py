# Contains all text and numeric data for game
welcome_text = ['Welcome to Rogue', 'Please enter Player name:']

game_intro_text = 'You enter the cave and find a wooden sword on the ground. There are dark passages ahead. ' \
                  'Which path will you take?'

game_intro_text2 = 'Press A to move left, D to move right or W to move forward'

stats = ['health', 'attack', 'defence', 'agility', 'luck']

explain_stat = {
'health': 'How much attack you can withstand', 
'attack': 'How much damage your attacks land on your enemy', 
'defence': 'How much you can defend an incoming enemy attack', 
'agility': 'Chance of evading an incoming attack', 
'luck': 'Chance of good loot from chests and enemies'
}

explain_enemy = {
  'bat': '',
  'ogre': '',
  'troll': '',
  'dragon': ''
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
    'bat': 100,
  },
  '2': {
    'bat': 60,
    'ogre': 40,
  },  
  '3': {
    'bat': 10,
    'ogre': 20,
    'troll': 10
  },
  '4': {
    'bat': 60,
    'ogre': 40,
  }
}

enemy_stats = {
  'bat': {
    'attack': 5,
    'defence': 5,
    'health': 10,
    'agility': 20,
  },
  'ogre': {
    'attack': 20,
    'defence': 30,
    'health': 20,
    'agility': 5,
  },
  'troll': {
    'attack': 40,
    'defence': 30,
    'health': 30,
    'agility': 5
  },
  'dragon': {
    'attack': 50,
    'defence': 50,
    'health': 50,
    'agility': 30
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

# Build enemy text object from the above
enemy_text = {
  'bat': [bat_text, bat_text_explain],
  'ogre': [ogre_text, ogre_text_explanation],
  'troll': [troll_text, troll_text_explanation],
  'dragon': [dragon_text, dragon_text_explanation]
}

chest_chance_dict = {
  'sword': {
      'wood': [50, 30, 10, 5, 5], 
      'iron': [40, 50, 50, 40, 30], 
      'gold': [10, 30, 40, 50, 50], 
      'diamond': [5, 10, 15, 20, 30], 
      'dragon scale': [1, 2, 2, 3, 4],
  },
  'shield': {
      'wood': [50, 30, 10, 5, 5], 
      'iron': [40, 50, 50, 40, 30], 
      'gold': [10, 30, 40, 50, 50], 
      'diamond': [5, 10, 15, 20, 30], 
      'dragon scale': [1, 2, 2, 3, 4],
  }, 
  'potion': {
    'types': [
      'health', 'agility', 'attack'
    ],
    'potion_strength': {
      'common': 50,
      'rare': 20,
      'legendary': 5
    }
  } }

item_stats = {
  'sword': {
    'wood': {
      'attack': '10',
    },
    'iron': {
      'attack': '15',
    },
    'gold': {
      'attack': '20',
    },
    'gold': {
      'attack': '25',
    },
    'diamond': {
      'attack': '30'
    },
    'dragon_scales': {
      'attack': '35',
    }
  },
  'shield':     {
    'wood': {
      'defence': '10',
    },
    'iron': {
      'defence': '15',
    },
    'gold': {
      'defence': '20',
    },
    'gold': {
      'defence': '25',
    },
    'diamond': {
      'defence': '30'
    },
    'dragon_scales': {
      'defence': '35',
    }
  },
  'potion': {
    'health': {
      'common': '10',
      'rare': '20',
      'legendary': '30'
    },
    'agility': {
      'common': '10',
      'rare': '20',
      'legendary': '30'
    },
    'attack': {
      'common': '10',
      'rare': '20',
      'legendary': '30'
    }
  }
}

combat_factors = {
  'light attack': {
    'attack': 1.2,
    'is_hit': 1,
    'critical_hit': 0.02
  },
  'heavy attack': {
    'attack': 1.6,
    'is_hit': 0.5,
    'critical_hit': 0.04
  }
}

chest_chances = {
  'sword': 10, 
  'shield': 10,
  'potion': 15,
}

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