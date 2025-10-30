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
