x: str = ""

some_lst = []


def test_func() -> None:
    print(x)

    if x:
        print("x is not zero")

    y = x + "something"
    print(y)

    some_lst = [y for _ in range(5)]
    print(some_lst)


if __name__ == "__main__":
    test_func()
    print("This is a test function.")
    print("some_lst:", some_lst)
