from item import Item

class Consumable(Item):
    # Initializers
    def __init__(self,
                 name: str,
                 description: str,
                 weight: float,
                 effect_type: str,
                 effect_modifier: float):
        super().__init__(
            name, 'consumable', description, weight
        )
        assert effect_modifier > 0, f"{name} must be a value greater than zero."
        self.__effect_type = effect_type
        self.__effect_modifier = effect_modifier


    ##### Getters and setters
    @property
    def effect_type(self) -> str:
        return self.__effect_type
    @effect_type.setter
    def effect_type(self, effect_type_value) -> None:
        self.__effect_type = effect_type_value
    
    @property
    def effect_modifer(self) -> float:
        return self.__effect_modifier
    @effect_modifer.setter
    def effect_modifier(self, effect_modifier_value) -> None:
        self.__effect_modifier = effect_modifier_value