from item import Item

class Inventory:
    def __init__(self, 
                 capacity: float, 
                 inventory: list[Item] = []):
        self.__capacity = capacity
        self.__inventory = inventory
    

    ##### Getters, setters, printers
    @property
    def capacity(self) -> float:
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity_value) -> None:
        self.__capacity = capacity_value

    @property
    def inventory(self) -> list[Item]:
        return self.__inventory
    @inventory.setter
    def inventory(self, inventory_value) -> None:
        assert isinstance(inventory_value, list[Item]), f"Must be list of Items"
        self.__inventory = inventory_value
    

    ##### Methods
    def get_weight(self) -> float:
        weight: float = 0.0
        for item in self.__inventory:
            weight += item.weight
        return weight

    def add(self, item: Item) -> bool:
        if item.weight + self.get_weight() <= self.__capacity:
            self.__inventory.append(item)
            return True
        else:
            print(f'Could not add {item.name} to inventory.')
            return False
    
    def remove(self, item: Item) -> bool:
        try:
            self.__inventory.remove(item)
            return True
        except Exception as e:
            print(f'Could not remove {item.name} from inventory.')
            return False