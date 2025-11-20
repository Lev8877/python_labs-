from pathlib import Path
import json
import csv


def json_to_csv(json_path: str, csv_path: str) -> None:
    p = Path(json_path)
    with p.open("r", encoding="utf-8") as f:
        try:
            a = json.load(f)
        except json.JSONDecodeError:
            raise ValueError
    if not a:
        raise ValueError
    for x in a:
        if type(x) != dict:
            raise ValueError
    with open(csv_path, "w", encoding="utf-8", newline="") as ff:
        headers = []
        for x in a:
            for k, _ in x.items():
                headers.append(k)
            break
        w = csv.writer(ff, delimiter=",")
        w.writerow(headers)
        for x in a:
            values = []
            for _, v in x.items():
                values.append(v)
            w.writerow(values)


def csv_to_json(csv_path: str, json_path: str) -> None:
    p = Path(csv_path)
    with open(p, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        data = list(reader)
    a = json.dumps(data, ensure_ascii=False, indent=2)
    with open(json_path, "w", encoding="utf-8") as ff:
        ff.write(a)


json_to_csv(
    r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab05\samples\people.json",
    r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab05\ex1.csv",
)
