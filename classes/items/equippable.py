from classes.items.item import Item

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
    
    