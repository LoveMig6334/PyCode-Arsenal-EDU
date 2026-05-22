from collections import deque

q = int(input())
normal = deque()
emergency = deque()

for _ in range(q):
    cmd = input().split()
    if cmd[0] == "ARRIVE":
        if cmd[2] == "emergency":
            emergency.append(cmd[1])
        else:
            normal.append(cmd[1])
    elif cmd[0] == "TREAT":
        if emergency:
            emergency.popleft()
        elif normal:
            normal.popleft()
    else:
        if not emergency and not normal:
            print("EMPTY")
        else:
            print(*emergency, *normal)
