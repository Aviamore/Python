c = list(map(int, input().split()))
B = set('')
for i in range(len(c)):
    y = len(c)
    B.add(c[i])

    if y == len(B):
        print("YES")
    else:
        print("NO")