b = int(input())
a = [int(s) for s in input().split()]
k = len(a)
if ((b/2) and ((len(a) % 2) == 1)):
    print ("NO")
else:
    for i in range (len(a)):
        if (b == a[i]):
            print ("YES")
        else:
            k = k - 1
            if (k == 0):
                print ("NO")
