menu = [
    ["ข้าวมันไก่ต้ม", 50, 0.9, 1.2, 0],
    ["ข้าวมันไก่ทอด", 50, 0.9, 0, 1.2],
    ["ข้าวมันไก่ผสม", 70, 1.1, 0.7, 0.7],
    ["ไก่ต้มสับ", 120, 0, 2.7, 0],
    ["ไก่ทอดสับ", 120, 0, 0, 2.7],
    ["ไก่ผสมสับ", 150, 0, 1.8, 1.8],
    ["ข้าวเปล่า", 10, 1.2, 0, 0],
]
sum = [0, 0, 0, 0, 0, 0, 0]
res = [["ข้าวมัน", 100], ["ไก่ต้ม", 50], ["ไก่ทอด", 50]]


def main() -> None:
    while True:
        select = int(input("กรุณาเลือกเมนู :"))

        if select == 99:
            total = 0
            print("ร้านปิดเเล้ว วันนี้คุณขายได้...")
            for i in range(len(menu)):
                print(f"{menu[i][0]}= {sum[i]} เป็นเงิน {menu[i][1] * sum[i]}บาท")
                total = total + menu[i][1] * sum[i]

            print(f"รวมยอดรายรับ {total}")

            print("""-เมื่อสิ้นวันให้แสดงจำนวนขายแต่ละเมนูและยอดขายรวมในเมนูนั้นๆ
             -เมื่อสิ้นวันให้สรุปยอดขายรวมได้""")
            break

        elif select == 88:
            print("ทรัพยากรที่เหลือ")
            for i in res:
                print(i[0], i[1])

        elif select >= 1 and select <= len(menu):
            unit = int(input("รับกี่จานดี?"))
            err = 0

            # ตรวจสอบว่าทรัพยากรที่ต้องใช้ (คูณจำนวน unit) มากกว่าที่มีหรือไม่
            rice_needed = menu[select - 1][2] * unit
            boiled_chicken_needed = menu[select - 1][3] * unit
            fried_chicken_needed = menu[select - 1][4] * unit

            if rice_needed > res[0][1]:
                print("ข้าวหมด")
                err = 1
            if boiled_chicken_needed > res[1][1]:
                print("ไก่ต้มหมด")
                err = 2
            if fried_chicken_needed > res[2][1]:
                print("ไก่ทอดหมด")
                err = 3

            if err != 0:
                print("ทรัพยากรไม่พอ กรุณากินอย่างอื่น")
            else:
                # หักทรัพยากรที่ใช้ไป
                res[0][1] -= rice_needed
                res[1][1] -= boiled_chicken_needed
                res[2][1] -= fried_chicken_needed

                print(
                    f"คุณสั่ง {menu[select - 1][0]} จำนวน {unit} หน่วย รวมยอดจ่าย {menu[select - 1][1] * unit}บาท"
                )

                sum[select - 1] = sum[select - 1] + unit
                print(sum)

        else:
            print("ผิดพลาด ไม่มีเมนู")


if __name__ == "__main__":
    main()
