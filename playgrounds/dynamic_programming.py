"""
Dynamic Programming (DP) — ทบทวนตั้งแต่พื้นฐานถึงโจทย์คลาสสิก
แนวคิดหลัก: ถ้าปัญหาใหญ่แบ่งเป็นปัญหาย่อยซ้ำๆ ได้ → เก็บคำตอบไว้ ไม่ต้องคิดซ้ำ

DP ใช้ได้เมื่อปัญหามี 2 คุณสมบัติ:
  1. Overlapping Subproblems — ปัญหาย่อยซ้ำกัน (เช่น fib(3) ถูกเรียกหลายครั้ง)
  2. Optimal Substructure — คำตอบที่ดีที่สุดของปัญหาใหญ่ สร้างจากคำตอบที่ดีที่สุดของปัญหาย่อย
"""

import time

# ============================================================
# 1. FIBONACCI — เข้าใจ DP ผ่านตัวอย่างง่ายที่สุด
# ============================================================
print("=" * 55)
print("1. FIBONACCI — ทำไมต้อง DP?")
print("=" * 55)


# --- วิธีที่ 1: Recursion ธรรมดา (ช้ามาก!) ---
def fib_recursive(n: int) -> int:
    if n <= 1:
        return n
    return fib_recursive(n - 1) + fib_recursive(n - 2)


# ลองวาด call tree ของ fib(5) ดู:
#                fib(5)
#              /        \
#          fib(4)       fib(3)      ← fib(3) ถูกคิดซ้ำ!
#         /    \        /    \
#      fib(3) fib(2) fib(2) fib(1)  ← fib(2) ถูกคิดซ้ำอีก!
#     /   \
#  fib(2) fib(1)
# Time: O(2^n) — ช้ามากกกก

start = time.perf_counter()
print(f"fib_recursive(30) = {fib_recursive(30)}")
print(f"  เวลา: {time.perf_counter() - start:.4f} วินาที (ช้า!)\n")


# --- วิธีที่ 2: Top-Down DP (Memoization) ---
# คิดจากบนลงล่าง: fib(n) → fib(n-1) → ... → fib(0)
# ใช้ dict เก็บคำตอบที่เคยคิดแล้ว ไม่ต้องคิดซ้ำ
def fib_memo(n: int, memo: dict[int, int] = {}) -> int:
    if n <= 1:
        return n
    if n in memo:       # เคยคิดแล้ว? ส่งคำตอบเดิมกลับเลย
        return memo[n]
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]
# Time: O(n), Space: O(n)


start = time.perf_counter()
print(f"fib_memo(30)      = {fib_memo(30)}")
print(f"  เวลา: {time.perf_counter() - start:.6f} วินาที (เร็วมาก!)\n")


# --- วิธีที่ 3: Bottom-Up DP (Tabulation) ---
# คิดจากล่างขึ้นบน: fib(0) → fib(1) → ... → fib(n)
# สร้างตาราง (array) เก็บคำตอบทีละขั้น
def fib_tab(n: int) -> int:
    if n <= 1:
        return n
    dp = [0] * (n + 1)   # สร้างตาราง
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]  # ใช้คำตอบก่อนหน้า
    return dp[n]
# Time: O(n), Space: O(n)


# --- วิธีที่ 4: Space Optimized ---
# สังเกตว่า fib(i) ใช้แค่ 2 ค่าก่อนหน้า → ไม่ต้องเก็บทั้ง array
def fib_optimized(n: int) -> int:
    if n <= 1:
        return n
    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1
    return prev1
# Time: O(n), Space: O(1) — ดีที่สุด!


start = time.perf_counter()
print(f"fib_tab(30)       = {fib_tab(30)}")
print(f"fib_optimized(30) = {fib_optimized(30)}")
print(f"  เวลา: {time.perf_counter() - start:.6f} วินาที")

print("""
สรุป Fibonacci:
  Recursion    → O(2^n)  ช้ามาก ซ้ำเยอะ
  Memoization  → O(n)    Top-Down + cache
  Tabulation   → O(n)    Bottom-Up + array
  Optimized    → O(n)    เก็บแค่ 2 ค่า
""")

# ============================================================
# 2. CLIMBING STAIRS — โจทย์ DP ง่ายๆ
# ============================================================
print("=" * 55)
print("2. CLIMBING STAIRS")
print("=" * 55)
print("""
โจทย์: มีบันได n ขั้น แต่ละก้าวขึ้นได้ 1 หรือ 2 ขั้น
       มีกี่วิธีที่จะขึ้นถึงขั้นบนสุด?

ตัวอย่าง n=4:
  1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 → 5 วิธี

วิธีคิด:
  ถ้าจะขึ้นถึงขั้นที่ i ได้ ต้องมาจาก:
    - ขั้นที่ i-1 (ก้าว 1 ขั้น) หรือ
    - ขั้นที่ i-2 (ก้าว 2 ขั้น)
  ดังนั้น: dp[i] = dp[i-1] + dp[i-2]  ← เหมือน Fibonacci!
""")


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 ขั้น → 1 วิธี
    dp[2] = 2  # 2 ขั้น → 2 วิธี (1+1 หรือ 2)
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


for n in range(1, 8):
    print(f"  {n} ขั้น → {climb_stairs(n)} วิธี")

print()

# ============================================================
# 3. COIN CHANGE — หาจำนวนเหรียญน้อยที่สุด
# ============================================================
print("=" * 55)
print("3. COIN CHANGE — จำนวนเหรียญน้อยที่สุด")
print("=" * 55)
print("""
โจทย์: มีเหรียญหลายชนิด ต้องทอนเงิน amount บาท
       ใช้เหรียญน้อยที่สุดกี่เหรียญ?

ตัวอย่าง: เหรียญ [1, 5, 10] ทอน 13 บาท
  → 10+1+1+1 = 4 เหรียญ? ไม่ใช่!
  → 5+5+1+1+1 = 5 เหรียญ? แย่กว่า
  → จริงๆ 10+1+1+1 = 4 เหรียญ ถูกแล้ว

วิธีคิด:
  dp[amount] = จำนวนเหรียญน้อยที่สุดที่ทอนได้ amount บาท
  สำหรับแต่ละ coin:
    dp[a] = min(dp[a], dp[a - coin] + 1)
  แปลว่า: "ถ้าใช้เหรียญนี้ 1 เหรียญ ส่วนที่เหลือต้องใช้กี่เหรียญ?"
""")


def coin_change(coins: list[int], amount: int) -> int:
    # dp[i] = จำนวนเหรียญน้อยที่สุดสำหรับ i บาท
    INF = amount + 1  # ค่าที่เป็นไปไม่ได้ (มากกว่าจำนวนเหรียญสูงสุด)
    dp = [INF] * (amount + 1)
    dp[0] = 0  # ทอน 0 บาท ใช้ 0 เหรียญ

    for a in range(1, amount + 1):
        for coin in coins:
            if coin <= a and dp[a - coin] + 1 < dp[a]:
                dp[a] = dp[a - coin] + 1

    return dp[amount] if dp[amount] != INF else -1


coins = [1, 5, 10]
for amount in [0, 3, 7, 11, 13, 15, 26]:
    result = coin_change(coins, amount)
    print(f"  เหรียญ {coins}, ทอน {amount:2d} บาท → {result} เหรียญ")

print()

# ============================================================
# 4. 0/1 KNAPSACK — ปัญหากระเป๋าเป้ (คลาสสิกมาก!)
# ============================================================
print("=" * 55)
print("4. 0/1 KNAPSACK — ปัญหากระเป๋าเป้")
print("=" * 55)
print("""
โจทย์: มีของ n ชิ้น แต่ละชิ้นมีน้ำหนักและมูลค่า
       กระเป๋ารับน้ำหนักได้ W กก.
       เลือกของใส่กระเป๋าให้มูลค่ารวมมากที่สุด (แต่ละชิ้นเอาหรือไม่เอา)

ตัวอย่าง: กระเป๋ารับได้ 7 กก.
  ของ: [(น้ำหนัก, มูลค่า)] = [(1,1), (3,4), (4,5), (5,7)]

วิธีคิด:
  dp[i][w] = มูลค่ามากสุดที่ได้ เมื่อพิจารณาของ i ชิ้นแรก กระเป๋ารับได้ w กก.
  สำหรับของชิ้นที่ i:
    - ไม่เอา: dp[i][w] = dp[i-1][w]
    - เอา:   dp[i][w] = dp[i-1][w - weight[i]] + value[i]  (ถ้าใส่ได้)
  เลือกอันที่ดีกว่า: dp[i][w] = max(ไม่เอา, เอา)
""")


def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    # สร้างตาราง dp ขนาด (n+1) x (capacity+1)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]  # ไม่เอาของชิ้นนี้
            if w <= c:
                # เอาของชิ้นนี้ (ถ้าคุ้มกว่า)
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)

    return dp[n][capacity]


# แสดงตาราง dp ให้เห็นภาพ
def knapsack_visual(weights: list[int], values: list[int], capacity: int):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w = weights[i - 1]
        v = values[i - 1]
        for c in range(capacity + 1):
            dp[i][c] = dp[i - 1][c]
            if w <= c:
                dp[i][c] = max(dp[i][c], dp[i - 1][c - w] + v)

    # แสดงตาราง
    print(f"  {'':>12} | ", end="")
    for c in range(capacity + 1):
        print(f"{c:>3}", end=" ")
    print(f"  ← น้ำหนักกระเป๋า")
    print(f"  {'':>12}-+-{'----' * (capacity + 1)}")
    for i in range(n + 1):
        label = "ไม่มีของ" if i == 0 else f"ของ{i}(w={weights[i-1]},v={values[i-1]})"
        print(f"  {label:>12} | ", end="")
        for c in range(capacity + 1):
            print(f"{dp[i][c]:>3}", end=" ")
        print()

    return dp[n][capacity]


weights = [1, 3, 4, 5]
values = [1, 4, 5, 7]
cap = 7

print(f"  ของ: น้ำหนัก={weights}, มูลค่า={values}")
print(f"  กระเป๋ารับได้: {cap} กก.\n")
knapsack_visual(weights, values, cap)
print(f"\n  มูลค่ามากสุด: {knapsack(weights, values, cap)}")

print()

# ============================================================
# 5. LONGEST COMMON SUBSEQUENCE (LCS) — ลำดับร่วมยาวสุด
# ============================================================
print("=" * 55)
print("5. LCS — Longest Common Subsequence")
print("=" * 55)
print("""
โจทย์: หา subsequence ร่วมที่ยาวที่สุดของ 2 string
       (subsequence = ตัวอักษรที่เลือกมาโดยยังเรียงตามลำดับเดิม ไม่ต้องติดกัน)

ตัวอย่าง: "ABCBDAB" กับ "BDCAB"
  → LCS = "BCAB" (ยาว 4)

วิธีคิด:
  dp[i][j] = LCS ของ s1[:i] กับ s2[:j]

  ถ้า s1[i-1] == s2[j-1]:  ตัวท้ายเหมือนกัน → เอามารวม
    dp[i][j] = dp[i-1][j-1] + 1
  ถ้าไม่เท่ากัน:  เลือกทิ้งตัวท้ายของ s1 หรือ s2
    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
""")


def lcs(s1: str, s2: str) -> tuple[int, str]:
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Backtrack หาว่า LCS คืออะไร
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s1[i - 1] == s2[j - 1]:
            result.append(s1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], "".join(reversed(result))


s1, s2 = "ABCBDAB", "BDCAB"
length, subseq = lcs(s1, s2)
print(f"  s1 = \"{s1}\"")
print(f"  s2 = \"{s2}\"")
print(f"  LCS = \"{subseq}\" (ยาว {length})")

print()

# ============================================================
# 6. LONGEST INCREASING SUBSEQUENCE (LIS)
# ============================================================
print("=" * 55)
print("6. LIS — Longest Increasing Subsequence")
print("=" * 55)
print("""
โจทย์: หา subsequence ที่เพิ่มขึ้นเรื่อยๆ ที่ยาวที่สุด

ตัวอย่าง: [10, 9, 2, 5, 3, 7, 101, 18]
  → LIS = [2, 3, 7, 18] หรือ [2, 5, 7, 101] (ยาว 4)

วิธีคิด:
  dp[i] = LIS ที่ยาวที่สุดที่จบที่ index i
  dp[i] = max(dp[j] + 1) สำหรับทุก j < i ที่ arr[j] < arr[i]
""")


def lis(arr: list[int]) -> int:
    n = len(arr)
    dp = [1] * n  # ทุกตัวเป็น LIS ยาว 1 ได้เสมอ (ตัวมันเอง)

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"  arr = {arr}")
    print(f"  dp  = {dp}")
    return max(dp)
# Time: O(n²) — มีวิธี O(n log n) ด้วย binary search แต่เข้าใจยากกว่า


nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"  LIS ยาว {lis(nums)}")

print()

# ============================================================
# 7. สรุปวิธีคิด DP
# ============================================================
print("=" * 55)
print("สรุป: วิธีคิด DP ทีละขั้น")
print("=" * 55)
print("""
  ขั้นที่ 1: นิยาม state
    → dp[i] หรือ dp[i][j] เก็บอะไร? (คำตอบของปัญหาย่อย)

  ขั้นที่ 2: หา recurrence (สูตรความสัมพันธ์)
    → dp[i] คิดจาก dp[ค่าก่อนหน้า] ยังไง?
    ตัวอย่าง:
      Fibonacci:  dp[i] = dp[i-1] + dp[i-2]
      Knapsack:   dp[i][w] = max(ไม่เอา, เอา)
      LCS:        dp[i][j] = dp[i-1][j-1]+1 หรือ max(dp[i-1][j], dp[i][j-1])

  ขั้นที่ 3: กำหนด base case
    → dp[0] = ?, dp[1] = ? (จุดเริ่มต้นที่ไม่ต้องคิดต่อ)

  ขั้นที่ 4: กำหนดทิศทางการคิด
    → Bottom-Up: วน loop จากเล็กไปใหญ่
    → Top-Down:  เขียน recursion + memo

  ขั้นที่ 5: หาคำตอบ
    → dp[n]? dp[n][m]? max(dp)? ขึ้นอยู่กับโจทย์

  Tips สำหรับแข่ง:
    - เริ่มจากวาดตารางมือก่อนเสมอ
    - ลอง brute force ก่อน แล้วหา pattern ที่ซ้ำ
    - ส่วนใหญ่ 1D dp → O(n) หรือ O(n²), 2D dp → O(n*m)
    - ถ้า space เยอะไป ดูว่าลดได้ไหม (เก็บแค่แถวก่อนหน้า)
""")

print("✅ จบแล้ว! ลองแก้ค่า input แต่ละข้อแล้วรันดูผลลัพธ์นะครับ")
