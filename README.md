# Lev8877

## Лабораторная работа 1

### Задание 1
```python
name = input("Введите ваше имя:")
age = input("Введите ваш возраст:")
age = int(age) + 1
age = str(age)
print("Привет,", name + "! Через год тебе будет", str(int(age)) + ".")
```
<img width="1116" height="352" alt="image" src="https://github.com/user-attachments/assets/547caeea-c2a5-4983-95b0-6af81fcebe36" />


### Задание 2
```python
a = input()
b = input()
if a.count(",") > 0:
    a = a.replace(",",".")
if b.count(",") > 0:
    b = b.replace(",",".")
a = float(a)
b = float(b)
sum = a + b 
rz = (a + b) / 2

print("sum=" + str(round(sum,2))+";","avg=" + str(round(rz,2)))
```
<img width="1138" height="399" alt="image" src="https://github.com/user-attachments/assets/e16e56e1-235d-4646-aee5-59c027ce77d7" />


### Задание 3
```python
price=int(input())
discount=int(input())
vat=int(input())
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print(f"База после скидки:   {base:.2f} ₽")
print(f"НДС:                 {vat_amount:.2f} ₽")
print(f"Итого к оплате:      {total:.2f} ₽")
```
<img width="1095" height="351" alt="image" src="https://github.com/user-attachments/assets/479292bd-bc2d-451c-b6fd-6d6bf86979ad" />


### Задание 4
```python
m = int(input())
k = m // 60
ost = m - k * 60 
if ost <= 9:
    total = total = str(k) + ":" + "0" + str(ost)
else:
    total = str(k) + ":" + str(ost)
print("Минуты:",m)
print(total)
```
<img width="1107" height="361" alt="image" src="https://github.com/user-attachments/assets/d65cdbdf-9d33-43e5-9972-3d82e0100696" />


### Задание 5
```python
I = input()
m = []
m = I.split()
space = len(m) - 1
print("ФИО:",I)
print("Инициалы:",m[0][0]+m[1][0]+m[2][0])
print("Длина (символов):",len(m[0])+len(m[1])+len(m[2]) + space)
```
<img width="1103" height="355" alt="image" src="https://github.com/user-attachments/assets/ef74a8e3-fcd8-4cf7-b4d0-556052342408" />


### Задание 6

```python
N = int(input())
m = []
for i in range(N):
    m.append(input())
k1 = 0
k2 = 0
for i in range(len(m)):
    if m[i].count("True") > 0:
        k1 += 1
    elif m[i].count("False") > 0:
        k2 += 1
print(k1,k2)
```
<img width="1096" height="366" alt="image" src="https://github.com/user-attachments/assets/925356b2-5445-45b8-80e4-54ea5fa4ed09" />


### Задание 7

``` python
cif = "0123456789"
buk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec = "."
shifr = str(input())
shifr = list(shifr)
fin = ""
k = 0
s = True
first = 0 
second = 0 
stop = False

for i in range (len(shifr)):
    ind = i 
    if shifr[ind] in buk:
        fin += shifr[ind]
        first = i
    if shifr[i] in cif and s == True:
        fin += shifr[i+1]
        s = False 
        second = i + 1
    shag = second - first  
    ostalos = len(shifr[:second])
    if shag > 0 and ostalos != len(shifr):
        for j in range(ostalos+shag,len(shifr),shag):
            fin += shifr[j]
            if shifr[j] == ".":
                stop = True
    if stop == True:
        break
print(fin)
```
<img width="1123" height="340" alt="image" src="https://github.com/user-attachments/assets/7034b8e4-f857-4b70-9319-1ab4b5ea1587" />










