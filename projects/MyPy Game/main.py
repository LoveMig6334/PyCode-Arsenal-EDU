import copy
import random
import time

from classpy.chr import Character
from classpy.mots import Monster


class Mage(Character):
    extra_spell: dict = {
        "fire_wall": {"mana_cost": 40, "damage": 40, "element": "fire"},
        "fire_bolt": {"mana_cost": 25, "damage": 25, "element": "fire"},
        "lighting_bolt": {"mana_cost": 30, "damage": 45, "element": "lightning"},
        "thunder_strike": {"mana_cost": 50, "damage": 60, "element": "lightning"},
        "ice_wall": {"mana_cost": 40, "damage": 35, "element": "ice"},
        "ice_shard": {"mana_cost": 20, "damage": 20, "element": "ice"},
    }

    def __init__(self, name: str, level: int, status: dict, spell: dict):
        mage_status = copy.deepcopy(status)
        mage_status["mana"] *= 2

        super().__init__(name, level, mage_status, spell)
        print(f"{self.name} has been created as a Mage.")

    def special_ability(self):
        print(f"{self.name} meditates to regain mana!")
        self.status["mana"] += 50
        print(f"{self.name} now has {self.status['mana']} mana.")
        print()

    def spell_learn(self, spell_name: str):
        if spell_name in self.know_spell:
            print(f"{self.name} has already learned this spell.")
            return

        if spell_name not in self.extra_spell:
            print(f"{self.name} cannot lean this spell.")
            return

        self.know_spell[spell_name] = self.extra_spell[spell_name]
        print(f"{self.name} has learned the spell '{spell_name}'.")
        print()


class Warrior(Character):
    def __init__(self, name, level, status, spell):
        warrior_status = copy.deepcopy(status)
        warrior_status["damage"] *= 1.2
        warrior_status["armor"] *= 1.1

        super().__init__(name, level, warrior_status, spell)
        print(f"{self.name} has been created as a Warrior.")

    def special_ability(self, target):
        print(f"{self.name} performs a devastating special attack!")
        self.status["damage"] *= 2

        self.attack_player(target=target)

        self.status["damage"] //= 2


def event_1(self) -> None:
    print(f"You ({self.name}) found a treasure chest")
    print("Do you want to open it ?")

    answer = input("Yes or No:")

    if answer.lower() == "yes":
        print("You found a sword")
    elif answer.lower() == "no":
        print("You left the chest")
    else:
        print("Invalid answer")


def event_2(self, monster) -> None:
    print(f"You got attack by a {monster.name}")

    monster.attack_player(player=self)


def create_warrior(start_status, start_spell):
    return Warrior(name="Warrior1", level=1, status=start_status, spell=start_spell)


def create_mage(start_status, start_spell):
    return Mage(name="Mage1", level=1, status=start_status, spell=start_spell)


def main() -> None:
    start_status = {
        "hp": 100,
        "damage": 10,
        "armor": 5,
        "speed": 10,
        "mana": 100,
    }

    start_spell = {
        "fireball": {"mana_cost": 20, "damage": 30, "element": "fire"},
        "heal": {"mana_cost": 15, "heal": 20, "element": "light"},
    }

    # Creating Mage and Warrior
    mage = create_mage(start_status, start_spell)
    warrior = create_warrior(start_status, start_spell)
    time.sleep(5)

    # Show initial statuses
    mage.show_status()
    warrior.show_status()
    time.sleep(5)

    # Mage uses a spell and special ability
    mage.cast_spell("fireball", warrior)
    mage.special_ability()
    time.sleep(5)

    # Warrior performs special attack
    warrior.special_ability(target=mage)

    # Show final statuses
    mage.show_status()
    warrior.show_status()
    time.sleep(5)

    mage.spell_learn("ice_wall")
    mage.cast_spell("ice_wall", warrior)
    time.sleep(5)

    warrior.attack_player(target=mage)

    mage.show_status()
    warrior.show_status()
    time.sleep(5)

    monster_list: list = [
        Monster(name="slime", hp=10, damage=15),
        Monster(name="goblin", hp=20, damage=20),
        Monster(name="orc", hp=50, damage=20),
    ]

    def random_event(self) -> None:
        event: int = random.randint(1, 2)

        if event == 1:
            event_1(self)
        elif event == 2:
            event_2(self, monster_list[random.randint(0, len(monster_list) - 1)])

    random_event(mage)
    random_event(warrior)
    time.sleep(5)

    monster_list[0].attack_player(player=mage)
    mage.show_status()


if __name__ == "__main__":
    main()
