def main() -> None:
    number = int(input())
    times = int(input())

    total = number * times

    if total == 0:
        print("No teaching")
    elif total < 60:
        print(f"{total} minutes")
    elif total % 60 == 0:
        print(f"{total // 60} hours")
    else:
        print(f"{total // 60} hours {total % 60} minutes")


if __name__ == "__main__":
    main()
