def is_ultimate_attack_ready(chakra: int) -> bool:
    if chakra >= 100:
        return True
    else:
        return False


def main() -> None:
    ninja = {
        f"Character {i}": float(input(f"Character {i}'s chakra levels: "))
        for i in range(1, 4)
    }
    print()

    for character in ninja:
        if is_ultimate_attack_ready(ninja[character]):
            print(f"{character} can perform the ultimate attack")


if __name__ == "__main__":
    main()
