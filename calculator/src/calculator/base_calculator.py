from .calc_exceptions import InvalidCalculation

def addn(*num):
    sum = 0
    for n in num:
        sum = sum + n
    return sum

def subt(*num):
    if len(num) > 1:
        diff = num[0]
        for n in num[1:]:
            diff = diff - n
    else:
        return num
    return diff

def mult(*num):
    res = 1
    for n in num:
        res = res * n
    return res

def dvd(*num):
    if len(num) > 1:
        res = num[0]
        for n in num[1:]:
            if n != 0:
                res = res/n
            else:
                return InvalidCalculation
    return res