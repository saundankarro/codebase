def exp(*num):
    if len(num) > 1:
        res = num[0]
        for n in num[1:]:
            res = res**n
    else:
        res = num
    return res

def root(n,m=2, o=1):
    return n**(o/m)