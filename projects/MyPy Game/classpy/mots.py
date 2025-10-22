class Monster:
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage

    def attack_player(self, player):
        if player.status["hp"] <= 0:
            print("This player is death")
            return

        damage: int = self.damage - player.status["armor"]
        damage = max(0, damage)

        player.status["hp"] -= damage

        print(f"{self.name} attacks {player.name} for {damage} damage.")
        if player.status["hp"] <= 0:
            print(f"{player.name} is death")

        print()
