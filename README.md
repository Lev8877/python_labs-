# Lev8877

## Лабораторная работа 1

### Задание 1
```python
name = input("Введите ваше имя:")
age = input("Введите ваш возраст:")
print("Привет", name,"! Через год тебе будет", int(age) + 1,"!")
```
<img width="1077" height="323" alt="image" src="https://github.com/user-attachments/assets/f55fdea4-cc72-4206-9e1d-e5bdb415f687" />

### Задание 2
```python
a = 3.5
b = 4.25
a = float(a)
b = float(b)
sum = a + b 
rz = (a + b) / 2

print(round(sum,2),round(rz,2))
```
<img width="1092" height="349" alt="image" src="https://github.com/user-attachments/assets/69fc2b25-3916-4a2d-9e23-72c5e7f0f1f3" />

### Задание 3
```python
price=1000
discount=10
vat=20
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount
print("База после скидки:", round(base,2))
print("НДС:", round(vat_amount,2))
print("Итого к оплате:", round(total,2))
```
<img width="1096" height="354" alt="image" src="https://github.com/user-attachments/assets/0f0de4ed-256f-462d-a789-67325d7a3d7f" />

### Задание 4
```python
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
```
<img width="1107" height="354" alt="image" src="https://github.com/user-attachments/assets/8b1f229b-108a-4b61-bca3-f476b95b842e" />

### Задание 5
```python
I = input()
m = []
m = I.split()
print("ФИО:",I)
print("Инициалы:",m[0][0]+m[1][0]+m[2][0])
print("Длина (символов):",len(I))
```
<img width="1086" height="354" alt="image" src="https://github.com/user-attachments/assets/49b3e0cb-213b-4363-90c6-4bb3ce65c3ba" />

### Задание 6

```python
f = ["Максимов Максим 18 True","Геннадьев Геннадий 17 False","Алексеев Алексей 17 True"]
k1 = 0
k2 = 0
for i in f:
    if i.count("True") > 0:
        k1 += 1 
    else:
        k2 += 1 
print(k1,k2)
```
<img width="1091" height="339" alt="image" src="https://github.com/user-attachments/assets/d5b208de-e062-41f3-b765-51d2fa3be827" />

### Задание 7

``` python
cif = "0123456789"
buk = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spec = "."
shifr = "thisisabracadabraHt1eadljjl12ojh."
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


 
print(fin) #Дай бог вам в помощь с этим кодом...
```
<img width="1084" height="354" alt="image" src="https://github.com/user-attachments/assets/05caf981-a900-411e-8424-e562b8ace4c7" />









