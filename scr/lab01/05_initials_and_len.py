I = input()
m = []
m = I.split()
space = len(m) - 1
print("ФИО:",I)
print("Инициалы:",m[0][0]+m[1][0]+m[2][0])
print("Длина (символов):",len(m[0])+len(m[1])+len(m[2]) + space)
