from abc import ABC, abstractmethod
from typing import Optional

class Equipment(ABC):
    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def use(self) -> None:
        pass

class Weapon(Equipment, ABC):
    def __init__(self, name: str):
        self.name = name

    def get_name(self) -> str:
        return self.name

class Sword(Weapon):
    def __init__(self):
        super().__init__("Sword")
    def use(self) -> None:
        print("Swinging the sword! Slash!")

class Axe(Weapon):
    def __init__(self):
        super().__init__("Axe")
    def use(self) -> None:
        print("Chop-chop with the axe!")

class Spear(Weapon):
    def __init__(self):
        super().__init__("Spear")
    def use(self) -> None:
        print("Thrusting the spear!")

class Shield(Equipment):
    def get_name(self) -> str:
        return "Shield"
    def use(self) -> None:
        print("Blocking with the shield!")

class Paladin:
    def __init__(self, name: str):
        self.name = name
        self.left_hand: Optional[Equipment] = None
        self.right_hand: Optional[Equipment] = None

    def equip_left_hand(self, equipment: Equipment) -> None:
        self.left_hand = equipment
        print(f"{self.name} took {equipment.get_name()} in left hand.")

    def equip_right_hand(self, equipment: Equipment) -> None:
        self.right_hand = equipment
        print(f"{self.name} took {equipment.get_name()} in right hand.")

    def fight(self) -> None:
        print(f"\n--- {self.name} enters the battle! ---")
        if self.left_hand:
            self.left_hand.use()
        if self.right_hand:
            self.right_hand.use()
        print("-------------------------------\n")

if __name__ == "__main__":
    arthas = Paladin("Arthas")
    arthas.equip_left_hand(Sword())
    arthas.equip_right_hand(Shield())
    arthas.fight()
    arthas.equip_right_hand(Axe())
    arthas.fight()
    arthas.equip_left_hand(Spear())
    arthas.fight()