from random import randint


def random():
    lst = [randint(1, 10) for i in range(5)]
    print(lst)
    return lst
def var4():
    lst = random()
    s_lst = set(lst)
    for i in s_lst:
        if lst.count(i) > 1:
            print(f"{i} YES")
        else:
            print(f"{i} NO")

var4()
