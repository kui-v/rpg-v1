import csv

class Item:
    all_items = []
    ##### Initializers
    def __init__(self,
                 name: str,
                 item_type: str):
        assert item_type in ('consumable', 'equippable'), f"{name} should be a consumable or equippable--not {item_type}"
        self.__name = name
        self.__item_type = item_type
        Item.all_items.append(self)
    

    ##### Getters, setters, printers
    @property
    def name(self) -> str:
        return self.__name
    @name.setter
    def name(self, name_value) -> None:
        self.__name = name_value

    @property
    def item_type(self) -> str:
        return self.__item_type
    @item_type.setter
    def item_type(self, item_type_value) -> None:
        self.__item_type = item_type_value
    
    def __repr__(self) -> str:
        return f"""{self.__class__.__name__}('{self.__name}')"""
    

    ##### Class methods
    @classmethod
    def instantiate_from_csv(cls, file):
        items = []
        with open(file) as f:
            reader = csv.DictReader(f)
            items = list(reader)
        f.close()
        for item in items:
            Item(
                name=item.get('name')
            )