name1, name2 = input(), input()


while len(name1) < len(name2):
    name1 += name1[: len(name2) - len(name1)]
while len(name2) < len(name1):
    name2 += name2[: len(name1) - len(name2)]


amulet = "".join(
    "w" if (c1.lower() in "love" or c2.lower() in "love") else "$"
    for c1, c2 in zip(name1, name2)
)


w_total = 0
run = 0
runs = []

for ch in amulet:
    if ch == "w":
        w_total += 1
        run += 1
    else:
        if run:
            runs.append(run)
            run = 0
if run:
    runs.append(run)


if w_total % 2 == 1:
    amulet += str(max(runs, default=0))
else:
    if max(runs, default=0) < 2:
        amulet += "#"

print(amulet)
