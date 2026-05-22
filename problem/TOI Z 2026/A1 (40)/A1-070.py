n = int(input())

types = ["Plastic", "Can", "Glass"]
for _ in range(n):
    vals = [float(x) for x in input().split()]
    total = sum(vals)
    parts = [f"{total:.1f}"]
    if total > 50:
        parts.append("Overloaded")
    for i in range(3):
        if vals[i] > 20:
            parts.append(f"Check Type {types[i]}")
    print(",".join(parts))
