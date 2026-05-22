n = int(input())
items = [input() for _ in range(n)]


def permute(current: list, remaining: list):
    if not remaining:
        print(" ".join(current))
        return
    for i in range(len(remaining)):
        permute(current + [remaining[i]], remaining[:i] + remaining[i + 1 :])


permute([], items)

fact = 1
for x in range(1, n + 1):
    fact *= x
print(fact)
