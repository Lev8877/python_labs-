m = int(input())
k = m // 60
ost = m - k * 60
if ost <= 9:
    total = total = str(k) + ":" + "0" + str(ost)
else:
    total = str(k) + ":" + str(ost)
print("Минуты:", m)
print(total)
