import csv

class Character:
    all_characters = []
    ##### Initializers
    def __init__(self, name: str):
        self.__name = name
    
    
    ##### Getters, setters, printers
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name_value: str) -> None:
        self.__name = name_value

    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}('{self.__name}')"""
    

    ##### Methods
    @classmethod
    def instantiate_from_csv(file):
        characters = []
        with open(file) as f:
            reader = csv.DictReader(f)
            characters = list(reader)
        f.close()

        for character in characters:
            Character(
                name=character.get('name')
            )