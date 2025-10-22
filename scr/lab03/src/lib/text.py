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

