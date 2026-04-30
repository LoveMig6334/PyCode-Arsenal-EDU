r, x, y = map(int, input().split())


def is_inside_circle(r, x, y) -> str:
    if (x**2 + y**2) == r**2:
        return "ON"
    elif (x**2 + y**2) < r**2:
        return "IN"
    else:
        return "OUT"


def main() -> None:
    print(is_inside_circle(r, x, y))


if __name__ == "__main__":
    main()
