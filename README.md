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



## Лабораторная работа 4

### Задание 1
```python
from pathlib import Path
import csv
from pathlib import Path
from typing import Iterable, Sequence
def read_text(path: str | Path, encoding: str = "UTF-8") -> str: #Можно выбрать либо ISO-8859-5 либо UTF-8 либо cp1251
    path_1 = Path(path)
    if not(path_1.is_file()):
        raise FileNotFoundError
    if encoding != "ISO-8859-5" and  encoding != "UTF-8" and  encoding != "cp1251": 
        raise ValueError(f"Unsupported encoding: {encoding}")
    a = path_1.read_text(encoding=encoding)
    a = a.replace(" ","")
    return a 

def write_csv(rows: Iterable[Sequence], path: str | Path,
              header: tuple[str, ...] | None = None) -> None:
    p = Path(path)
    rows = list(rows)
    with p.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f,delimiter=",")
        if header is not None:
            w.writerow(header)
        if len(rows) != 0:
            row0 = rows[0]
        for r in rows:
            if len(row0) != len(r):
                raise ValueError
            w.writerow(r)

txt = read_text(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs-\data\lab04\input.txt")
print(txt)
write_csv([("word","count"),("test",3)], "data/lab04/check.csv",["sigma","sigma"])
```
![photo_2025-10-30_11-58-38](https://github.com/user-attachments/assets/c390f514-58ec-46c2-a255-b9a0e464ec58)


### Задание 2
```python
from pathlib import Path
import csv
import os
import sys
if __package__ is None or __package__ == "":
    print("Перезапускаю корректно: py -m scr.lab04.text_report ...\n")
    os.system("py -m scr.lab04.text_report")
    sys.exit()
from scr.lab03.src.lib.text import normalize, tokenize, top_n, count_freq
p = Path(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs-\data\lab04\input.txt")

with p.open("r", newline="", encoding="utf-8") as f:
    text = f.read()
a = normalize(text)
b = tokenize(a)
c = count_freq(b)
d = top_n(c)
def csv_writter(rows, path):
    p = Path(path)
    rows1 = list(rows)
    with p.open("w",newline="",encoding="utf-8") as ff:
        w = csv.writer(ff,delimiter=",")
        w.writerow(["word","count"])
        for x in rows1:
            w.writerow(x)

csv_writter(d, "data/lab04/check.csv")
```
![photo_2025-10-30_11-58-43](https://github.com/user-attachments/assets/7c421324-731a-4dfd-8fed-f3dfc91ebdfd)

## Лабораторная работа 5

### Задание 1
```python
from pathlib import Path
import json 
import csv
def json_to_csv(json_path: str) -> None:
    p = Path(json_path)
    with p.open("r",encoding="utf-8") as f:
        try:
            a = json.load(f) 
        except json.JSONDecodeError:
            raise ValueError
    if not a:
        raise ValueError
    for x in a:
        if type(x) != dict:
            raise ValueError
    dict1 = {}
    with open("data/lab05/ex1.csv","w",encoding="utf-8") as ff:
        headers = []
        for x in a:
            for k,_ in x.items():
                headers.append(k)
            break
        w = csv.writer(ff,delimiter=",")
        w.writerow(headers)
        for x in a:
            values = []
            for _,v in x.items():
                values.append(v)
            w.writerow(values)
#json_to_csv(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs-\data\lab05\samples\people.json")

def csv_to_json(csv_path: str) -> None:
    p = Path(csv_path)
    with open(p,"r",encoding="utf-8") as f:
        headers = [] 
        reader = csv.DictReader(f)
        data = list(reader)
        for x in data:
            for k,_ in x.items():
                headers.append(k)
            break
    a = json.dumps(data,ensure_ascii=False,indent=2)
    b = json.loads(a)
    with open("data/lab05/ex1.csv","w",encoding="utf-8") as ff:
        ff.write(a)
        
csv_to_json(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs-\data\lab05\samples\peoples.csv")
```
![ex1 1](https://github.com/user-attachments/assets/b1f23bb7-b091-429d-a362-f09fd110d8bd)
![ex1 2](https://github.com/user-attachments/assets/56b323f8-aa51-48a8-893c-16e9637358a9)

### Задание 2
```python
from openpyxl import Workbook
import csv
from pathlib import Path

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    p = Path(csv_path)
    if not p.exists():
        raise FileNotFoundError
    if p.suffix.lower() != '.csv':
        raise ValueError
    
    wb = Workbook()
    ws = wb.active
    ws.title = "Sheet1"

    with open(p, encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)
        if not rows:
            raise ValueError
        for row in rows:
            ws.append(row)

    for col in ws.columns:
        max_len = 8
        for cell in col:
            if cell.value:
                length = len(str(cell.value))
                if length > max_len:
                    max_len = length
        col_letter = col[0].column_letter
        ws.column_dimensions[col_letter].width = max_len

    wb.save(xlsx_path)

csv_to_xlsx(
    "data/lab05/ex1.csv",
    "data/lab05/samples/ex1.xlsx"
)
```
![ex2](https://github.com/user-attachments/assets/282d10f5-30bd-436b-9b7d-35216ea39af0)


## Лабораторная работа 6

### Задание 1
```python
import argparse 
from pathlib import Path 
from ..lab03.src.lib.text import my_top_n

def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument("--input", required=True,help="Просто путь, если абсюоютный то в ' ' ")
    stats_parser.add_argument("--top", type=int, default=5,help="Сколько значений вывести, по умолчанию 5")

    args = parser.parse_args()

    if args.command == "cat":
        result = [] 
        k = 0
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")   
        with open(p, encoding="utf-8") as ff:
            for line in ff:
                if args.n:
                    k += 1
                    result.append(str(k) + "." + " " + line.strip())
                else:
                    result.append(line.strip())
        for i in result:
            print(i)
    elif args.command == "stats":
        freq = {}
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл") 
        with open(p,encoding="utf-8") as f:
            for line in f:
                for slovo in line.split():
                    freq[slovo] = freq.get(slovo, 0) + 1
        top_n1 = my_top_n(freq, args.top)
        for word, count in top_n1:
            print(f"{word}: {count}")

            
if __name__ == "__main__":
    main()
```
<img width="1919" height="1079" alt="ex1" src="https://github.com/user-attachments/assets/a078003a-db47-4ca5-9088-68091fa0eaa7" />

### Задание 2
```python
import argparse
from pathlib import Path
from ..lab05.json_csv import json_to_csv, csv_to_json
from ..lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv",help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True,help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True,help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json",help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True,help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True,help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx",help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True,help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True,help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл") 
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        json_to_csv(args.input,args.output)

    if args.cmd == "csv2json":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл") 
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        csv_to_json(args.input,args.output)

    if args.cmd == "csv2xlsx":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл")  
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        csv_to_xlsx(args.input,args.output)

if __name__ == "__main__":
    main()
```
<img width="1919" height="1079" alt="ex2" src="https://github.com/user-attachments/assets/25847ba0-0e53-4741-8fe0-77c0e6a6b592" />

## Лабораторная работа 7

### Задание 1
```python
import pytest
from lab03.src.lib.text import normalize, tokenize, count_freq, my_top_n


def test_normalize_basic():
    assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
    assert normalize("") == ""


def test_tokenize_basic():
    assert tokenize("привет мир") == ["привет", "мир"]
    assert tokenize("") == []


def test_count_freq_and_top_n():
    assert my_top_n(count_freq(["bb", "aa", "bb", "aa", "cc"])) == [
        ("aa", 2),
        ("bb", 2),
    ]


def test_top_n_tie_breaker():
    assert my_top_n({"aa": 2, "bb": 2, "cc": 1}, ds=1) == [("aa", 2)]
    assert my_top_n({"b": 1, "a": 1}, ds=2) == [("a", 1), ("b", 1)]


# py -m pytest -q
```

### Задание 2
```python
import pytest
from lab05.json_csv import json_to_csv, csv_to_json
from pathlib import Path
import csv
import json
import os


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    try:
        json.loads(Path(src).read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    data = "name,age\nAlice,22\nBob,25\n"

    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))
    if not src.exists():
        raise FileNotFoundError
    if not dst.exists():
        raise FileNotFoundError
    if os.path.getsize(src) == 0:
        raise ValueError
    with src.open(encoding="utf-8") as ff:
        reader = csv.DictReader(ff)
        if reader.fieldnames is None:
            raise ValueError

    result = json.loads(dst.read_text("utf-8"))

    assert result == [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]


# py -m pytest -q
```

## Лабораторная работа 8

### Задание 1
```python
from dataclasses import dataclass
from datetime import date, datetime
@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float


    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Неправильный формат даты")
        
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 10")

    def age(self) -> int:
        parts = self.birthdate.replace("/", " ").replace("-", " ").split()
        return int(date.today().year) - int(parts[0])

    def to_dict(self) -> dict:
        if None in (self.fio, self.birthdate, self.group, self.gpa):
            raise ValueError("Не все поля заполнены")
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(**d)

    def __str__(self):
        return f"{self.fio}, {self.group}, {self.gpa}, {self.birthdate}"
    
s = Student("Иванов Иван", "2000/05/12", "A-01", 4)

data = {
    "fio": "Иванов Иван",
    "birthdate": "2000/05/12",
    "group": "A-01",
    "gpa": 4,
}
if __name__ == "__main__":
    print(s.birthdate)   
    print(s.fio)  
    print(s.group)  
    print(s.gpa)  

    print("----------------")

    print(s.age())
    print(s.to_dict())
    print(Student.from_dict(data))
    print(s.__str__())
```
<img width="1919" height="1018" alt="ex1" src="https://github.com/user-attachments/assets/8f14cb12-8f00-4259-b309-8fcbca6ec062" />

### Задание 2
```python
import json 
from pathlib import Path
from models import Student

stupids = [
    Student("Иванов Иван", "2000/05/12", "A-01", 4),
    Student("Петров Петр", "2001/03/10", "B-02", 4.5),
]

def students_to_json(students, path):
    p = Path(path)
    data = [s.to_dict() for s in students]
    a = json.dumps(data, ensure_ascii=False, indent=2)
    with open(p, "w", encoding="utf-8") as ff:
        ff.write(a)

def students_from_json(path):
    p = Path(path)
    with open(p, "r", encoding="utf-8") as ff:
        data = json.load(ff)
    return [Student.from_dict(d) for d in data]
        

if __name__ == "__main__":
    #students_to_json(stupids, r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab08\students_input.json")
    print(students_from_json(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab08\students_output.json"))
```
<img width="1919" height="1021" alt="ex2" src="https://github.com/user-attachments/assets/95e7bf7e-0c16-441e-ae82-4937c32016ba" />

