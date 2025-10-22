s = input().strip()


max_u = 0
n = len(s)

for i, ch in enumerate(s):
    if ch.lower() == "b":
        j = i + 1
        cur = 0
        while j < n and s[j].lower() == "u":
            cur += 1
            j += 1
        max_u = max(max_u, cur)


if max_u >= 2:
    print(f"Yes {max_u}")
else:
    idx_b = next((i for i, ch in enumerate(s) if ch.lower() == "b"), -1)

    if idx_b != -1:
        result = s[: idx_b + 1] + "U" * (n - idx_b - 1)
        print(result)
    else:
        result = ("BUU" * ((n + 2) // 3))[:n]
        print(result)
