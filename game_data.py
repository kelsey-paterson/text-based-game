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

room_map = [[str(x) + y for y in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']] for x in range(1, 10)]
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