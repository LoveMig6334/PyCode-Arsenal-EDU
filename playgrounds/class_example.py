import time


class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed

    def speed_modifier(self, modifier: float):
        self.speed *= modifier

    def damage_modifier(self, modifier: float):
        self.speed *= modifier


warrior = Character(100, 10, 5)
print(f"{warrior} was Created \n")

time.sleep(2)

print(
    f"Status of a warrior \nHealth : {warrior.health}\nDamage: {warrior.damage}\nSpeed: {warrior.speed}\n"
)

time.sleep(5)

warrior.status_change(1.5)
print("warrior.status_change was updated \n")

time.sleep(2)

print(
    f"Status of a warrior \nHealth : {warrior.health}\nDamage: {warrior.damage}\nSpeed: {warrior.speed}"
)
