from calculator import addn, subt, mult, dvd, exp, root

x = addn(1,1)
print(f"1 + 1 = {x}")

s = subt(2,1)
print(f"2 - 1 = {s}")

s = subt(2,3,1,4)
print(f"2 - 3 - 1 - 4 = {s}")
m = mult(2,2)
print(f"2 x 2 = {m}")

d = dvd(2,2)
print("2 / 2 = {}".format(float(d)))

e = exp(2,2)
print(f"2^2 = {e}")

q=root(16)
print(f"The square root of 16 = {q}")

r=root(16,4)
print(f"The fourth root of 16 = {r}")

s=root(64,6,5)
print(f"64 ^ (5/6) = {s}")