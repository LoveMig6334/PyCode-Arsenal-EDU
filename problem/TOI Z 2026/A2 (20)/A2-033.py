rates = {1: 25, 2: 50, 3: 80, 4: 110, 5: 145, 6: 180}


def to_minutes(t: float) -> int:
    h = int(t)
    mm_str = f"{t:.2f}".split(".")[1]
    mi = int(mm_str)
    if h < 0 or h > 23 or mi < 0 or mi > 59:
        return -1
    return h * 60 + mi


i = float(input())
o = float(input())
mi_in = to_minutes(i)
mi_out = to_minutes(o)

if mi_in < 0 or mi_out < 0 or mi_in >= mi_out:
    print("ERROR")
else:
    diff = mi_out - mi_in
    if diff < 15:
        print("FREE")
    else:
        hours = (diff + 59) // 60
        print(rates[hours] if hours <= 6 else 250)
