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
