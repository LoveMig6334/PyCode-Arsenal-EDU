import itertools


def theos_text_encoder(string: str) -> str:
    breakdown: list = ["".join(g) for k, g in itertools.groupby(string)]
    result = "".join(f"{len(s)}{s[0]}" for s in breakdown)

    return result


def main() -> None:
    text = input()
    print(theos_text_encoder(text))
    print()


if __name__ == "__main__":
    main()
