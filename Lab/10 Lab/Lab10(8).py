b = int(input())
a = [int(s) for s in input().split()]
if (len(a)/2 == (len(a)%2 == 0)):
    print ("NO")
else:
    for i in range (len(a)):
        if (b == a[i]):
            print ("YES")
