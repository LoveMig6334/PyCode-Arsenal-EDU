def check_rabbit_word(s: str):
    n = len(s)
    S = s.upper()

    if n > 0 and all(c in ("I", "T") for c in S):
        print("unknown", n)
        return

    allowed = set("RABIT")

    for i, c in enumerate(S):
        if c not in allowed:
            print("no", i)
            return

        if c == "A":
            if i == 0 or S[i - 1] not in ("R", "A"):
                print("no", i)
                return

        if c == "R":
            if i + 1 >= n:
                print("no", i)
                return
            if S[i + 1] != "A":
                print("no", i + 1)
                return

        if c == "B":
            if i + 1 >= n:
                print("no", i)
                return
            if S[i + 1] not in ("I", "T"):
                print("no", i + 1)
                return

    max_A = 0
    cur = 0
    for c in S:
        if c == "A":
            cur += 1
            max_A = max(max_A, cur)
        else:
            cur = 0

    print("yes", max_A)


def main() -> None:
    s = input().strip()
    check_rabbit_word(s)


if __name__ == "__main__":
    main()
