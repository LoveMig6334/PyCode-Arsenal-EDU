def f_to_c(f: float) -> float:
    return (f - 32) * 5 / 9


def main() -> None:
    temp = float(input())
    unit: str = input().capitalize()

    if unit == "F":
        temp = f_to_c(temp)

    if temp <= 0:
        print("solid")
    elif temp > 100:
        print("gas")
    else:
        print("liquid")


if __name__ == "__main__":
    main()
