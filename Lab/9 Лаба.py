n = int(input())
a = [[0] * n for i in range (n)]
for i in range(n):
    for j in range(n-1,-1,-1):
        if (j==n-i-1):
            a[i][j] = 1
    for j in range(n-1,-1,-1):
        if (j>n-i-1):
            a[i][j]=2
for row in a:
    print(' '.join([str(elem) for elem in row]))
