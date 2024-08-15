from calculator import addn, subt, mult, dvd, exp, root, temp, conv_len

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

il = conv_len(12, 'in', 'ft')
print(f"There are {il} feet in 12 inches")

il = conv_len(36, 'in', 'yards')
print(f"There are {il} yards in 36 inches")

il = conv_len(1, 'km', 'm')
print(f"There are {il} meters in 1 km")

il = conv_len(1, 'in', 'cm')
print(f"There are {il} cm in 1 inches")

t = temp(32,'F','c')
print(f"32F in Celsius is {t}")

t = temp(0, 'Celsius', 'Fahrenheit')
print(f"0C in Fahrenheit is {t}")

t = temp(212, 'F', 'kelvin')
print(f"212 Fahrenheit in Kelvin is {t}")

t = temp(373.15, 'K', 'F')
print(f"373.15 Kelvin in Fahrenheit is {t}")

t = temp(100, "Centigrade", "F")
print(f"100 Centigrade in Fahrenheit is {t}")

try:
    g = temp(0, 'Celsius', 'Gradient')
except Exception as e:
    print(e)
    
il = conv_len(12, 'in', 'ft')
print(f"There are 12 inches in {il} ft")