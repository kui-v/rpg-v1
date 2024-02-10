from character import Character
from item import Item
from equippable import Equippable
from consumable import Consumable

character_import_file = './csv/characters.csv'
Character.instantiate_from_csv(character_import_file)
print(Character.all_characters)

item_import_file = './csv/items.csv'
Item.instantiate_from_csv(item_import_file)
print(Item.all_items)

eqp = Equippable(name="dvd", description="a dvd you can watch or throw", durability=5, damage=2, weight=.3)
print(eqp.damage)

con = Consumable(name="potion", description="increases health", effect_type="health_up", effect_modifier=.20, weight=.4)
print(con.effect_type)