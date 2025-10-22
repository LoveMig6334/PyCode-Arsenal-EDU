def file_write() -> None:
    with open("monsters.txt", "w") as file:
        file.write("Dragon,Fire,1500\n")
        file.write("Goblin,Earth,500\n")
        file.write("Phoenix,Fire,1200\n")
        file.write("Ogre,Earth,1000\n")


def file_read(lst: list) -> list:
    with open("monsters.txt", "r") as file:
        for line in file:
            name, monster_type, hp = line.strip().split(",")
            lst.append({"name": name, "type": monster_type, "hp": int(hp)})
    return lst


def main() -> None:
    file_write()

    monsters = []
    search_type = (input("Enter a type of monster: ")).strip()

    filtered_monsters = [
        monster for monster in file_read(monsters) if monster["type"] == search_type
    ]

    if filtered_monsters:
        print(f"{search_type} Monsters")
        for monster in filtered_monsters:
            print(f"{monster['name']}: {monster['hp']} HP")
    else:
        print(f"No monsters of type '{search_type}' found.")


if __name__ == "__main__":
    main()
