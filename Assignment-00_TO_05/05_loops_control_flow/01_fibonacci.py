MAX = 10000
cur = 0
next = 1

while cur <= MAX:
    print(cur, end=" " "💚 ")
    new = cur + next # 0 + 1
    cur = next       # 0 = 1
    next = new       # 1 = 0 + 1