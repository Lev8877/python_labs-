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
