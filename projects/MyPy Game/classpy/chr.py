import copy


class Character:
    def __init__(self, name: str, level: int, status: dict, spell: dict):
        self.name = name
        self.level = level
        self.status = copy.deepcopy(status)
        self.know_spell = copy.deepcopy(spell)

    def show_status(self):
        print("-" * 20)

        print(f"Name: {self.name}")
        print(f"Level: {self.level}")

        for status, value in self.status.items():
            print(f"{status.capitalize()}: {value}")

        print("-" * 20)
        print()

    def attack_player(self, target):
        if self.status["hp"] <= 0:
            print(f"{self.name} is dead and cannot attack.")
            return

        if target.status["hp"] <= 0:
            print(f"{target.name} is already dead and cannot be attacked.")
            return

        damage = self.status["damage"] - target.status["armor"]
        damage = max(0, damage)

        target.status["hp"] -= damage
        print(f"{self.name} attacks {target.name} for {damage} damage.")

        if target.status["hp"] <= 0:
            target.status["hp"] = 0
            print(f"{target.name} is dead.")
        print()

    def cast_spell(self, spell_name: str, target):
        if spell_name not in self.know_spell:
            print(f"{self.name} doesn't know the spell '{spell_name}'.")
            return

        spell = self.know_spell[spell_name]
        mana_cost = spell.get("mana_cost", 0)

        if self.status["mana"] < mana_cost:
            print(f"{self.name} doesn't have enough mana to cast '{spell_name}'.")
            return

        self.status["mana"] -= mana_cost
        print(f"{self.name} casts {spell_name.capitalize()} spell!")

        if "damage" in spell:
            damage = spell["damage"] - target.status["armor"]
            damage = max(0, damage)

            target.status["hp"] -= damage
            print(f"{spell_name.capitalize()} hits {target.name} for {damage} damage.")

            if target.status["hp"] <= 0:
                target.status["hp"] = 0
                print(f"{target.name} is dead.")

        elif "heal" in spell:
            heal = spell["heal"]
            self.status["hp"] += heal
            print(f"{self.name} heals for {heal} HP.")

        print()

    def level_up(self):
        self.level += 1
        for status in ["hp", "damage", "armor", "speed", "mana"]:
            self.status[status] *= 1.20
            self.status[status] = int(self.status[status])

        print(f"{self.name} leveled up to level {self.level}!")
        print()
