m = input()
m = int(m)
h = m // 60
c = m % 60
mn = h * 60 
mnn = m - mn 
if c <= 9:
    total = total = str(h) + ":" + "0" + str(mnn)
else:
    total = str(h) + ":" + str(mnn)
print("Минуты:",m)
print(total)
