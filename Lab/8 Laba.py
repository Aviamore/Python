a = int(input())
n = int(input())
def power(a,n):
    if (n!=1):
        return a * power (a,n-1)
    else:
        return a
print (power(a,n))
