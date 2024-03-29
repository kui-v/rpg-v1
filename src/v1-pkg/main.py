from character import Character
from item import Item
from equippable import Equippable
from consumable import Consumable
from inventory import Inventory

# character_import_file = './csv/characters.csv'
# Character.instantiate_from_csv(character_import_file)
# print(Character.all_characters)

# item_import_file = './csv/items.csv'
# Item.instantiate_from_csv(item_import_file)
# print(Item.all_items)

# eqp = Equippable(name="dvd", description="a dvd you can watch or throw", durability=5, damage=2, weight=.3)
# print(eqp.damage)

# con = Consumable(name="potion", description="increases health", effect_type="health_up", effect_modifier=.20, weight=.4)
# print(con.effect_type)

sword = Item('sword','equippable','just a sword',5.0)
legendary_sword = Item('legendary sword', 'equippable', 'a sword that you should not have', 20)

inv = Inventory(10)
print(inv.get_weight())
# inv.add_to_inventory(sword)
# print(inv.get_inventory_weight())
char = Character('Tester', inv, 10, 2)
print(char.inventory.get_weight())
char.inventory.add(sword)
print(char.inventory.get_weight())
char.inventory.remove(sword)
print(char.inventory.get_weight())
char.inventory.remove(legendary_sword)
char.inventory.add(legendary_sword)
print(char.inventory.get_weight())