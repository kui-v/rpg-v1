import csv
from inventory import Inventory

class Character:
    all_characters = []
    ##### Initializers
    def __init__(self, 
                 name: str, 
                 inventory: Inventory,
                 hp: int = 0,
                 dmg: int = 0
                 ):
        if hp:
            assert hp >= 0, f"{name} HP should be greater than or equal to zero."
        if dmg:
            assert dmg >= 0, f"{name} DMG should be greater than or equal to zero."
        self.__name = name
        self.__inventory = inventory
        self.__hp = hp
        self.__dmg = dmg
        Character.all_characters.append(self)
    
    
    ##### Getters, setters, printers
    @property
    def name(self) -> str:
        return self.__name    
    @name.setter
    def name(self, name_value: str) -> None:
        self.__name = name_value

    @property
    def hp(self) -> int:
        return self.__hp
    @hp.setter
    def hp(self, hp_value: int) -> None:
        self.__hp = hp_value

    @property
    def dmg(self) -> int:
        return self.__dmg
    @dmg.setter
    def dmg(self, dmg_value: int) -> None:
        self.__dmg = dmg_value

    @property
    def inventory(self) -> Inventory:
        return self.__inventory
    @inventory.setter
    def inventory(self, inventory_value: Inventory) -> None:
        self.__inventory = inventory_value

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}('{self.__name}')"""
    

    ##### Class methods
    @classmethod
    def instantiate_from_csv(cls, file) -> None:
        characters = []
        with open(file) as f:
            reader = csv.DictReader(f)
            characters = list(reader)
        f.close()
        for character in characters:
            Character(
                name=character.get('name'),
                hp=int(character.get('hp')),
                dmg=int(character.get('dmg'))
            )

    ##### Instance methods
    def take_damage(self, damage_amount) -> None:
        self.__hp -= damage_amount