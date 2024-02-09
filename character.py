import csv

class Character:
    all_characters = []
    ##### Initializers
    def __init__(self, 
                 name: str, 
                 hp: int = 0, 
                 dmg: int = 0):
        self.__name = name
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

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}('{self.__name}')"""
    

    ##### Class methods
    @classmethod
    def instantiate_from_csv(cls, file):
        characters = []
        with open(file) as f:
            reader = csv.DictReader(f)
            characters = list(reader)
        f.close()
        for character in characters:
            Character(
                name=character.get('name')
            )