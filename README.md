# rpg-v1
Making a scratch RPG game with Python, maybe this might go somewhere

## Classes
* Character
    * Inventory
* Consumable
    * Item
* Equippable
    * Item
* Inventory
    * Item
* GameState

## Layout
* Classes are separate
* All changes about a round should be kept in a gamestate class
    * That is, all player settings, besides Inventory, should be reset after a round

## Inventory
* Each character has an inventory object
* When a character adds some item to their inventory, how to update the character's inventory object?
    * Character.Inventory.add(item)