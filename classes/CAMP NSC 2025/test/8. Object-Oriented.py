class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def display_status(self):
        print(f"Name: {self.name}, Health: {self.health}, Attack: {self.attack}")

    def is_alive(self):
        return self.health > 0

    def attack_hero(self, other_hero):

        if not self.is_alive():
            print(f"{self.name} cannot attack because they have been defeated.")
            return
        if not other_hero.is_alive():
            print(f"{other_hero.name} has already been defeated.")
            return

        damage = self.attack
        other_hero.health -= damage

        if other_hero.health < 0:
            other_hero.health = 0

        print(
            f"{self.name} attacks {other_hero.name} for {damage} damage! {other_hero.name} health drops to {other_hero.health}"
        )

        if not other_hero.is_alive():
            print(f"{other_hero.name} has been defeated!")


def main() -> None:
    hero1 = Hero("Link", 230, 50)
    hero2 = Hero("Zelda", 100, 12)

    hero1.display_status()
    hero2.display_status()
    print()

    hero1.attack_hero(hero2)
    hero2.display_status()
    print()

    hero2.attack_hero(hero1)
    hero1.display_status()


if __name__ == "__main__":
    main()
