from classes.character import Character
from classes.items.item import Item

character_import_file = 'csv/characters.csv'
Character.instantiate_from_csv(character_import_file)
print(Character.all_characters)

item_import_file = 'csv/items.csv'
Item.instantiate_from_csv(item_import_file)
print(Item.all_items)

for item in Item.all_items:
    print(item.name, item.item_type, item.description)