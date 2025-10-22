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




## Лабораторная работа 2

### Задание 1
```python
import sys
def min_max(nums: list[float | int]): 
    return float(min(nums)) if float(min(nums)) % 1 != 0 else int(min(nums)) ,float(max(nums)) if float(max(nums)) % 1 != 0 else int(max(nums))

def unique_sorted(nums: list[float | int]):
    return sorted(set(nums))

def flatten(mat: list[list | tuple]):
    result = []
    for item in mat:
        result.extend(item)
    return result

buk = "abcdefghijklmnopqrstuvwxyz"
cif = "0123456789"

print("What function you are going to use?")
print("min_max - 1, unique_sorted - 2, flatten - 3")
c = int(input())
if c == 1 or c == 2:
    print("Write your numbers in one line with spaces")
    m = []
    d = input().replace(",", " ").split()
    for i in range(len(d)):
        m.append(int(d[i]) if d[i].count(".") == 0 else float(d[i]))

s = []
if c == 3:
    print("how many lists you want, write number")
    z = input()
    if str(z) not in cif:
        print("ValueError")
        sys.exit() 
    z = int(z)
    print(f"write numbers in one line {z} times")
    for j in range(z):
        l = []
        y = input().replace(","," ").split()
        for v in range(len(y)):
            if str(y[v]) in buk:
                print("TypeError")
                sys.exit() 
            if y[v].count("0") == 0 and y[v].count("1") == 0 and y[v].count("2") == 0 and y[v].count("3") == 0 and y[v].count("4") == 0 and y[v].count("5") == 0 and y[v].count("6") == 0 and y[v].count("7") == 0 and y[v].count("8") == 0 and y[v].count("9") == 0:
                break
            l.append(int(y[v]) if y[v].count(".") == 0 else float(y[v]))
        s.append(l)




if c == 1:
    print(min_max(m) if len(m) > 0 else "ErrorValue")
elif c == 2:
        print(unique_sorted(m) if len(m) > 0 else [])
else:
    print(flatten(s))
```
<img width="868" height="526" alt="image" src="https://github.com/user-attachments/assets/519006f6-f58c-41fd-8709-99cd5dd4ae84" />



### Задание 2
```python
def transpose(mat: list[list[float | int]]):
    result = []
    if mat == []:
        return []
    first = len(mat[0])
    for row in mat:
        if first != len(row):
            return "ValueError"
    for i in range(len(mat[0])):
        new_mat = []
        for j in range(len(mat)):
            new_mat.append(mat[j][i])
        result.append(new_mat)
    return result

def row_sums(mat: list[list[float | int]]):
    result = []
    first = len(mat[0])
    for row in mat:
        if first != len(row):
            return "ErrorValue"
    if mat == []:
        return []
    for i in range(len(mat)):
        s = sum(mat[i])
        result.append(s)
    return result 

def col_sums(mat: list[list[float | int]]):
    result = []
    first = len(mat[0])
    for row in mat:
        if first != len(row):
            return "ValueError"
    for i in range(len(mat[0])):
        new_mat = 0
        for j in range(len(mat)):
            new_mat += mat[j][i]
        result.append(new_mat)
    return result 

print(transpose([[1, 2], [3, 4]]))
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[1, 2, 3], [4, 5, 6]]))
```
<img width="870" height="277" alt="image" src="https://github.com/user-attachments/assets/a875eab8-1d5a-41de-835f-a7511967e687" />


### Задание 3
```python
buk = "abcdefghijklmnopqrstuvwxyz"
def format_record(rec: tuple[str, str, float]):
    result = []
    FIO = rec[0].split()
    FIO_LEN = len(FIO)
    if FIO_LEN == 0:
        return "ValueError"
    elif FIO_LEN == 3:
        c = rec[0].split()
        second = c[1][0] + "."
        third = c[2][0] + "."
        NEW_FIO = c[0][0].upper() + c[0][1:].lower() + " " + second.upper() + third.upper()
    elif FIO_LEN == 2:
        c = rec[0].split()
        second = c[1][0] + "."
        NEW_FIO = c[0][0].upper() + c[0][1:].lower() + " " + second.upper()
    result.append(NEW_FIO)
    if rec[1] == "":
        return "ValueError"
    else:
        NEW_GROUP = "гр." + " " + rec[1]
    result.append(NEW_GROUP)
    GPU_STR = str(rec[2])
    for j in GPU_STR:
        if GPU_STR.count(".") == 1:
            if j not in buk:
                NEW_GPU = f"GPU {round(float(rec[2]), 2):.2f}"
        else:
            return "ErrorValue"
    result.append(NEW_GPU)
    return result[0] +"," + " " + result[1]+ "," + " " +result[2]


print(format_record(("ИВАНОВ ИВАН ИВАНОВИЧ", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
<img width="1120" height="1013" alt="image" src="https://github.com/user-attachments/assets/06c24a8c-67cc-4f69-9156-ea275cf099e8" />


## Лабораторная работа 3

### Задание 1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold == True:
        text = text.casefold() 
    if yo2e == True:
        text = text.replace("ё","е").replace("Ё","Е")
    text = text.replace("\n"," ").replace("\r"," ").replace("\t"," ")
    a = text.split()
    text1 = ""
    for i in a:
        if len(text1) == 0:
            text1 += i
        else:
            text1 += " " + i
    return text1

buk_eng = "abcdefghijklmnopqrstuvwxyz"
buk_rus = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
cif = "0123456789"
def tokenize(text: str):
    res = []
    l = ""
    for i in text:
        if i in buk_eng or i in buk_rus or i in cif or i in "_-/\:":
            l += i 
        elif len(l) != 0:
            res.append(l)
            l = ""
    if l:
        res.append(l)
    return res 

def count_freq(tokens: list[str]) -> dict[str, int]:
    set_tokens = list(set(tokens))
    turpleeesss = {}
    for word in tokens:
        turpleeesss[word] = turpleeesss.get(word,0) + 1
    return turpleeesss
            
    

def top_n(freq: dict[str, int], ds: int = 2) -> list[tuple[str, int]]:
    sorted_list = sorted(freq.items(),key = lambda x: x[1] ,reverse=1)
    result = []
    sets = []
    for y in range (len(sorted_list)):
        sum = 0
        sum2 = 0
        if sorted_list[y] == sorted_list[-1]:
            break
        for x in sorted_list[y][0]:
            sum += ord(x)
        for x in sorted_list[y+1][0]:
            sum2 += ord(x)
        if sorted_list[y][1] == sorted_list[y+1][1] and sum > sum2:
            a = sorted_list[y]
            b = sorted_list[y+1]
            sorted_list[y] = b
            sorted_list[y+1] = a
    return sorted_list[:ds]

def B_count(a):
    k = 0
    for x in a.split():
        k += 1
    return k 

def B_uni_my(a):
    result = []
    k = 0
    l = ""
    for x in a.split():
        for y in x:
            if y.isalpha():
                l += y
            if x[-1] == y:
                l += " "
    result = l.split()
    turp = {}
    for x in result:
        turp[x] = turp.get(x,0) + 1
    for x in turp:
        k += 1
    return k 

def B_top_n(a:str):
    result_final = ""
    result = []
    sort = []
    l = ""
    for x in a.split():
        for y in x:
            if y.isalpha():
                l += y
            if x[-1] == y:
                l += " "
    result = l.split()
    turp = {}
    for x in result:
        turp[x] = turp.get(x,0) + 1
    sort = sorted(turp.items(), key = lambda x: x[1],reverse=1)
    for x in sort:
        if len(result_final) == 0:
            result_final += str(x[0]) + " " + str(x[1])
        else:
            result_final += "\n" + str(x[0]) + " " + str(x[1])
    return result_final





print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка",yo2e=True,))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
a=count_freq(["bb","aa","bb","aa","cc"])
print(a)
print(top_n(a))
```
<img width="1143" height="318" alt="image" src="https://github.com/user-attachments/assets/e80c76e0-c70b-4cd2-bbc1-47f850e90a70" />


### Задание 2
```python
from lib.text import B_count
from lib.text import B_top_n
from lib.text import B_uni_my
c = "мир Привет Привет, мир! Привет!!!"

print("\nВторое задание\n")
print(f"Всего слов: {B_count(c)}")
print(f"Уникальных слов: {B_uni_my(c)}")
print(f"Топ:\n{B_top_n(c)}")
```
<img width="1159" height="320" alt="image" src="https://github.com/user-attachments/assets/489b4650-0731-4336-b0da-b0ca00295e32" />











