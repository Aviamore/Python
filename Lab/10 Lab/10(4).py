a = [int(s) for s in input().split()]
b = list(set(a))
for i in range (len(a)):
    if (a[i] == b[i]):
        print ("NO")
    else:
        print ("YES")
print (a)
print (b)
