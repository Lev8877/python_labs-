a = input()
b = input()
if a.count(",") > 0:
    a = a.replace(",", ".")
if b.count(",") > 0:
    b = b.replace(",", ".")
a = float(a)
b = float(b)
sum = a + b
rz = (a + b) / 2

print("sum=" + str(round(sum, 2)) + ";", "avg=" + str(round(rz, 2)))
