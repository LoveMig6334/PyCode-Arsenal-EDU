# นาย ธรรศ บุนนาค เลขที่ 5 ชั้น 3/3

salary = float(input("กรอกเงินเดือน: "))
name = input("กรอกชื่อผู้รับเงินเดือน: ")


if salary > 40_000:
    print("\nคุณไม่ได้เงินเดือนเพิ่ม")
    print("ผู้รับเงินเดือน: ", name)
    print("เงินเดือนเดิม: ", salary)

    new = salary * (0 / 100)
    print("เงินที่ได้เพิ่มขึ้น", new)
    print("เงินเดือนใหม่ที่ปรับแล้ว", salary + new)

elif salary >= 10_000:
    print("\nคุณได้เงินเดือนเพิ่ม 2% ")
    print("ผู้รับเงินเดือน: ", name)
    print("เงินเดือนเดิม: ", salary)

    new = salary * (2 / 100)
    print("เงินที่ได้เพิ่มขึ้น", new)
    print("เงินเดือนใหม่ที่ปรับแล้ว", salary + new)
else:
    print("\nคุณได้เงินเดือนเพิ่ม 5%")
    print("ผู้รับเงินเดือน: ", name)
    print("เงินเดือนเดิม: ", salary)

    new = salary * (5 / 100)
    print("เงินที่ได้เพิ่มขึ้น", new)
    print("เงินเดือนใหม่ที่ปรับแล้ว", salary + new)
