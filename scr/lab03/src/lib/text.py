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
    result = {}
    for word in tokens:
        result[word] = result.get(word,0) + 1
    return result

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    sorted_set = sorted(freq.items(), key = lambda item: item[1],reverse=1 )
    return sorted_set
        


print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка",yo2e=True,))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
a=count_freq(["a","b","a","c","b","a"])
print(a)
print(top_n(a))

