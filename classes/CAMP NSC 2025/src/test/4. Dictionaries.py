characters_power = {
    "Goku": 9000,
    "Luffy": 5000,
    "Naruto": 7000,
}


def update_characters(characters: str, power: int) -> None:
    characters_power[characters] = power


def main() -> None:
    update_characters("Saitama", 6000)

    update_characters("Goku", 9000)
    update_characters("Luffy", 10000)
    update_characters("Naruto", 7000)

    print(characters_power)


if __name__ == "__main__":
    main()
