syms = ["#", "/", "+", "*"]
nums = input().split()
out = ""

for s in nums:
    n = int(s)
    if n == 0:
        out += "-"
    else:
        d = [(n // 1000) % 10, (n // 100) % 10, (n // 10) % 10, n % 10]
        for i in range(4):
            if d[i] > 0:
                out += syms[i]

print(out)
