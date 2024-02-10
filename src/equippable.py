from item import Item

class Equippable(Item):
    # Initializers
    def __init__(self, 
                 name: str,
                 description: str,
                 durability: int = 0,
                 damage: int = 0):
        super().__init__(
            name, 'equippable', description
        )
        assert durability >= 0, f"{name} cannot have durability less than zero."
        self.__durability = durability
        self.__damage = damage
    
    
    ##### Getters and setters
    @property
    def durability(self) -> int:
        return self.__durability
    @durability.setter
    def durability(self, durability_value) -> None:
        self.__durability = durability_value
    
    @property
    def damage(self) -> int:
        return self.__damage
    @damage.setter
    def damage(self, damage_value) -> None:
        self.__damage = damage_value