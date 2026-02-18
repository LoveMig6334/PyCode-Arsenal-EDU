MENU = [
    ["ข้าวมันไก่ต้ม", 50, 1.2, 0.8, 0],
    ["ข้าวมันไก่ทอด", 50, 1.2, 0, 0.8],
    ["ข้าวมันไก่ผสม", 70, 1.2, 0.6, 0.6],
    ["ไก่ต้มสับ", 120, 0, 1.8, 0],
    ["ไก่ทอดสับ", 120, 0, 0, 1.8],
    ["ไก่ผสมสับ", 150, 0, 1, 1],
    ["ข้าวเปล่า", 10, 1.5, 0, 0],
]
RES_NAME = ["ข้าว", "ไก่ต้ม", "ไก่ทอด"]
RES_COST = [3, 5, 6]

res = [0.0, 0.0, 0.0]
sales = [0] * 7
money = 0.0


def show_menu():
    print("\n──── เมนู ────")
    for i, m in enumerate(MENU, 1):
        avail = "v" if can_make(i - 1, 1) else "x"
        print(f"  {i}. {m[0]} ({m[1]}฿) [{avail}]")
    print("  77=ซื้อวัตถุดิบ  88=ดูทรัพยากร  99=ปิดร้าน")


def show_res():
    print("\n── ทรัพยากร ──")
    for i in range(3):
        print(f"  {RES_NAME[i]}: {res[i]:.1f}")
    print(f"  เงิน: {money:.0f} บาท")


def buy():
    global money
    print("\n── ซื้อวัตถุดิบ ──")
    for i in range(3):
        print(f"  {i + 1}. {RES_NAME[i]} (หน่วยละ {RES_COST[i]}฿)")
    try:
        s = int(input("เลือก (0=กลับ): "))
        if not 1 <= s <= 3:
            return
        q = int(input("จำนวน: "))
        if q <= 0:
            return
    except ValueError:
        print("ใส่ตัวเลข")
        return
    cost = RES_COST[s - 1] * q
    res[s - 1] += q
    money -= cost
    print(f"  ซื้อ {RES_NAME[s - 1]} {q} หน่วย จ่าย {cost}฿")


def can_make(idx, qty):
    return all(MENU[idx][2 + j] * qty <= res[j] for j in range(3))


def order(idx, qty):
    global money
    for j in range(3):
        res[j] -= MENU[idx][2 + j] * qty
    sales[idx] += qty
    total = MENU[idx][1] * qty
    money += total
    print(f"  {MENU[idx][0]} x{qty} = {total}฿")


def close_day():
    print("\n════ สรุปยอดขาย ════")
    grand = 0
    for i in range(7):
        rev = MENU[i][1] * sales[i]
        if sales[i]:
            print(f"  {MENU[i][0]}: {sales[i]} จาน = {rev}฿")
        grand += rev
    print(f"  รวมรายได้: {grand}฿")
    print(f"  เงินคงเหลือ: {money:.0f}฿")
    show_res()


def buy_loop(label):
    print(f"\n== {label} ==")
    while True:
        show_res()
        buy()
        if input("ซื้อเพิ่ม? (y/n): ").strip().lower() != "y":
            break


def main():
    global money, sales, res
    # เริ่มต้นวัตถุดิบวันแรก
    res = [100.0, 50.0, 50.0]
    money = -(100 * 3 + 50 * 5 + 50 * 6)  # -850
    day = 1

    while True:
        print(f"\n{'=' * 30}\n  วันที่ {day} | เงิน: {money:.0f}฿\n{'=' * 30}")
        sales = [0] * 7

        # ซื้อวัตถุดิบเพิ่ม (ถ้าต้องการ)
        if input("ซื้อวัตถุดิบเพิ่ม? (y/n): ").strip().lower() == "y":
            buy_loop("ซื้อวัตถุดิบเพิ่ม")

        # เปิดขาย
        while True:
            show_menu()
            try:
                s = int(input("สั่งเมนู: "))
            except ValueError:
                print("ใส่ตัวเลข")
                continue

            if s == 99:
                close_day()
                break
            elif s == 88:
                show_res()
            elif s == 77:
                buy()
            elif 1 <= s <= 7:
                try:
                    q = int(input("จำนวน: "))
                except ValueError:
                    print("ใส่ตัวเลข")
                    continue
                if q <= 0:
                    continue
                if not can_make(s - 1, q):
                    print("  ทรัพยากรไม่พอ!")
                    for j in range(3):
                        need = MENU[s - 1][2 + j] * q
                        if need > res[j]:
                            print(
                                f"    {RES_NAME[j]}: ต้องการ {need:.1f} มี {res[j]:.1f}"
                            )
                else:
                    order(s - 1, q)
            else:
                print("ไม่มีเมนูนี้")

        # จบวัน - ซื้อวัตถุดิบวันถัดไป
        if input("\nเปิดวันถัดไป? (y/n): ").strip().lower() != "y":
            print("ขอบคุณครับ!")
            break
        buy_loop("ซื้อวัตถุดิบสำหรับวันถัดไป")
        day += 1


if __name__ == "__main__":
    main()
