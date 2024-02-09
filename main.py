from character import Character

character_file = 'characters.txt'
Character.instantiate_from_csv(character_file)
print(Character.all_characters)