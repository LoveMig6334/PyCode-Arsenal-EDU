def str_encode(str_input: str) -> str:
    str_counter: dict = {}
    for i in range(len(str_input)):
        char = str_input[i]
        if char in str_counter:
            str_counter[char] += 1
        else:
            str_counter[char] = 1

    result = "".join(f"{v}{k}" for k, v in str_counter.items())
    return result


def main() -> None:
    str_input = input()
    print(str_encode(str_input))


if __name__ == "__main__":
    main()
