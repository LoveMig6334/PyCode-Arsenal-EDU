"""
Python Review — ทบทวน Python แบบรวมทุกหัวข้อสำคัญ
รันแล้วอ่านผลลัพธ์ไปทีละส่วน ลองแก้โค้ดเล่นได้เลย!
"""

# ============================================================
# 1. LIST COMPREHENSION — สร้าง list แบบย่อในบรรทัดเดียว
# ============================================================
print("=" * 50)
print("1. LIST COMPREHENSION")
print("=" * 50)

# แบบปกติ (for loop)
squares_loop = []
for i in range(1, 6):
    squares_loop.append(i ** 2)

# แบบ list comprehension — ทำสิ่งเดียวกันแต่สั้นกว่า
# โครงสร้าง: [expression for item in iterable]
squares = [i ** 2 for i in range(1, 6)]
print(f"ยกกำลังสอง: {squares}")  # [1, 4, 9, 16, 25]

# ใส่เงื่อนไข (filter) — เอาเฉพาะเลขคู่
# โครงสร้าง: [expression for item in iterable if condition]
evens = [i for i in range(1, 11) if i % 2 == 0]
print(f"เลขคู่ 1-10: {evens}")  # [2, 4, 6, 8, 10]

# ใส่ if-else (transform) — ระวัง! if-else อยู่ข้างหน้า for
labels = ["คู่" if i % 2 == 0 else "คี่" for i in range(1, 6)]
print(f"คู่/คี่: {labels}")  # ['คี่', 'คู่', 'คี่', 'คู่', 'คี่']

# Nested — แปลง 2D list ให้เป็น 1D (flatten)
matrix = [[1, 2], [3, 4], [5, 6]]
flat = [num for row in matrix for num in row]
print(f"Flatten: {flat}")  # [1, 2, 3, 4, 5, 6]

# Dict comprehension — ใช้หลักการเดียวกันแต่ใส่ {}
word = "hello"
char_index = {char: idx for idx, char in enumerate(word)}
print(f"Dict comprehension: {char_index}")

print()

# ============================================================
# 2. STRING OPERATIONS — จัดการ string
# ============================================================
print("=" * 50)
print("2. STRING OPERATIONS")
print("=" * 50)

s = "  Hello, Python World!  "

# ตัด whitespace
print(f"strip:  '{s.strip()}'")
print(f"lstrip: '{s.lstrip()}'")
print(f"rstrip: '{s.rstrip()}'")

# เปลี่ยน case
print(f"upper:  '{s.strip().upper()}'")
print(f"lower:  '{s.strip().lower()}'")
print(f"title:  '{'hello world'.title()}'")

# ค้นหาและแทนที่
msg = "I like cats and cats like me"
print(f"replace: '{msg.replace('cats', 'dogs')}'")
print(f"count:   {msg.count('cats')}")
print(f"find:    index={msg.find('cats')}")  # -1 ถ้าไม่เจอ

# split & join
csv = "apple,banana,cherry"
fruits = csv.split(",")
print(f"split:  {fruits}")
print(f"join:   '{' | '.join(fruits)}'")

# f-string — วิธีฝังตัวแปรใน string (แนะนำใช้แบบนี้)
name, score = "สมชาย", 95.678
print(f"f-string: {name} ได้ {score:.1f} คะแนน")  # .1f = ทศนิยม 1 ตำแหน่ง

# Slicing — ตัด string เหมือน list
text = "ABCDEFGH"
print(f"text[2:5]  = '{text[2:5]}'")   # CDE (index 2,3,4)
print(f"text[:3]   = '{text[:3]}'")     # ABC (ตั้งแต่ต้นถึง index 2)
print(f"text[-3:]  = '{text[-3:]}'")    # FGH (3 ตัวท้าย)
print(f"text[::2]  = '{text[::2]}'")    # ACEG (เว้นตัว)
print(f"text[::-1] = '{text[::-1]}'")   # กลับหลัง

# เช็คว่ามีคำอยู่ไหม
print(f"'CD' in text: {'CD' in text}")           # True
print(f"startswith:   {text.startswith('ABC')}")  # True

print()

# ============================================================
# 3. LAMBDA FUNCTION — ฟังก์ชันไม่มีชื่อ (anonymous function)
# ============================================================
print("=" * 50)
print("3. LAMBDA FUNCTION")
print("=" * 50)

# ฟังก์ชันปกติ
def add_normal(a, b):
    return a + b

# Lambda — เหมือนกันแต่เขียนบรรทัดเดียว
# โครงสร้าง: lambda parameters: expression
add = lambda a, b: a + b
print(f"lambda add: {add(3, 5)}")  # 8

# ใช้กับ sorted() — เรียงลำดับตามเงื่อนไข
students = [("แอน", 85), ("บี", 92), ("ซี", 78)]
by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"เรียงตามคะแนน: {by_score}")

# ใช้กับ map() — แปลงทุกตัวใน list
nums = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, nums))
print(f"map x2:  {doubled}")

# ใช้กับ filter() — กรองเอาเฉพาะที่ตรงเงื่อนไข
adults = list(filter(lambda x: x >= 18, [15, 22, 17, 30, 12]))
print(f"filter >=18: {adults}")

# เปรียบเทียบ: ใช้ list comprehension แทน map/filter ก็ได้ (อ่านง่ายกว่า)
doubled_lc = [x * 2 for x in nums]          # เหมือน map
adults_lc = [x for x in [15, 22, 17, 30, 12] if x >= 18]  # เหมือน filter
print(f"(comprehension ก็ได้ผลเหมือนกัน)")

print()

# ============================================================
# 4. DICTIONARY & LOOP KEY-VALUE
# ============================================================
print("=" * 50)
print("4. DICTIONARY & LOOP KEY-VALUE")
print("=" * 50)

# สร้าง dict
student = {
    "name": "สมหญิง",
    "age": 16,
    "grade": "M4",
    "scores": [88, 92, 76],
}

# เข้าถึงค่า
print(f"ชื่อ: {student['name']}")
print(f"get: {student.get('email', 'ไม่มี')}")  # get ปลอดภัยกว่า ไม่ error ถ้าไม่มี key

# เพิ่ม / แก้ไข
student["email"] = "som@example.com"
student["age"] = 17
print(f"เพิ่ม/แก้: {student}")

# ลบ
removed = student.pop("email")
print(f"ลบ email: {removed}")

# --- Loop แบบต่างๆ ---
print("\nLoop keys:")
for key in student:
    print(f"  {key}")

print("\nLoop values:")
for value in student.values():
    print(f"  {value}")

print("\nLoop key-value (สำคัญมาก!):")
for key, value in student.items():
    print(f"  {key}: {value}")

# นับความถี่ — ใช้ dict เก็บ
sentence = "apple banana apple cherry banana apple"
freq = {}
for word in sentence.split():
    freq[word] = freq.get(word, 0) + 1
print(f"\nนับคำ: {freq}")

# Dict comprehension — กรอง dict
high_freq = {k: v for k, v in freq.items() if v >= 2}
print(f"คำที่ซ้ำ >= 2: {high_freq}")

# Nested dict
school = {
    "M4/1": {"students": 35, "avg_score": 82.5},
    "M4/2": {"students": 33, "avg_score": 78.0},
}
for room, info in school.items():
    print(f"  {room} -> {info['students']} คน, เฉลี่ย {info['avg_score']}")

print()

# ============================================================
# 5. CLASS & OOP — สร้าง object ของตัวเอง
# ============================================================
print("=" * 50)
print("5. CLASS & OOP")
print("=" * 50)


class Animal:
    """คลาสพื้นฐาน — สัตว์ทั่วไป"""

    # class variable — ใช้ร่วมกันทุก object
    count = 0

    def __init__(self, name: str, sound: str):
        """สร้าง object ใหม่ — __init__ จะถูกเรียกอัตโนมัติ"""
        self.name = name      # instance variable — แต่ละตัวมีค่าของตัวเอง
        self.sound = sound
        self.energy = 100
        Animal.count += 1

    def speak(self):
        return f"{self.name} says {self.sound}!"

    def eat(self, food: str):
        self.energy += 10
        return f"{self.name} eats {food} (energy: {self.energy})"

    def __str__(self):
        """กำหนดว่า print(object) จะแสดงอะไร"""
        return f"Animal({self.name}, energy={self.energy})"


# Inheritance — สืบทอดจากคลาสแม่
class Dog(Animal):
    def __init__(self, name: str, breed: str):
        super().__init__(name, "Woof")  # เรียก __init__ ของ Animal
        self.breed = breed

    def fetch(self, item: str):
        self.energy -= 20
        return f"{self.name} fetches the {item}!"

    # Override — เขียนทับ method ของคลาสแม่
    def speak(self):
        return f"{self.name} ({self.breed}) says Woof Woof!"


# สร้าง objects
cat = Animal("มีมี่", "Meow")
dog = Dog("โกลเด้น", "Golden Retriever")

print(cat.speak())
print(dog.speak())         # ใช้ method ที่ override
print(dog.eat("bone"))     # ใช้ method จาก Animal (สืบทอดมา)
print(dog.fetch("ball"))
print(f"สัตว์ทั้งหมด: {Animal.count} ตัว")
print(f"dog เป็น Animal ไหม? {isinstance(dog, Animal)}")  # True
print(f"print object: {cat}")  # ใช้ __str__

print()

# ============================================================
# 6. BONUS — รวมทุกอย่างเข้าด้วยกัน
# ============================================================
print("=" * 50)
print("6. BONUS — รวมทุกอย่าง")
print("=" * 50)


class Classroom:
    def __init__(self, room: str):
        self.room = room
        self.students: dict[str, list[int]] = {}  # name -> [scores]

    def add_student(self, name: str, scores: list[int]):
        self.students[name] = scores

    def averages(self) -> dict[str, float]:
        """ใช้ dict comprehension + lambda ผสมกัน"""
        return {
            name: sum(scores) / len(scores)
            for name, scores in self.students.items()
        }

    def top_students(self, min_avg: float = 80) -> list[str]:
        """ใช้ list comprehension + dict.items()"""
        avgs = self.averages()
        return [name for name, avg in avgs.items() if avg >= min_avg]

    def summary(self) -> str:
        """ใช้ f-string + join + sorted + lambda"""
        avgs = self.averages()
        ranked = sorted(avgs.items(), key=lambda x: x[1], reverse=True)
        lines = [f"  {i+1}. {name}: {avg:.1f}" for i, (name, avg) in enumerate(ranked)]
        return f"ห้อง {self.room}\n" + "\n".join(lines)


room = Classroom("M4/1")
room.add_student("อลิซ", [95, 88, 92])
room.add_student("บ๊อบ", [72, 68, 75])
room.add_student("ชาลี", [85, 90, 88])
room.add_student("เดวิด", [60, 55, 70])

print(room.summary())
print(f"\nคะแนนเฉลี่ย >= 80: {room.top_students(80)}")

print("\n✅ ทบทวนครบแล้ว! ลองแก้โค้ดด้านบนเล่นดูนะครับ")
