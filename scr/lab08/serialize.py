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