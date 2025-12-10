import csv
from pathlib import Path
from scr.lab08.models import Student



class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")
        else:
            with open(self.path, "r", encoding="utf-8") as f:
                first = f.readline().strip()
            if first != "fio,birthdate,group,gpa":
                self.path.write_text("fio,birthdate,group,gpa\n", encoding="utf-8")

    def list(self) -> list[Student]:
        result = []
        with open(self.path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue

            parts = line.split(",")
            if len(parts) != 4:
                continue

            fio, birthdate, group, gpa = parts

            try:
                gpa = float(gpa)
            except:
                continue

            try:
                student = Student(
                    fio=fio,
                    birthdate=birthdate,
                    group=group,
                    gpa=gpa
                )
            except:
                continue

            result.append(student)

        return result

    def add(self, student: Student):
        with open(self.path, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=",")
            w.writerow([student.fio, student.birthdate, student.group, student.gpa])

    def find(self, substr: str) -> list:
        substr = substr.lower()
        result = []
        for student in self.list():
            if substr in student.fio.lower():
                result.append(student)
        return result

    def remove(self, fio: str):
        rows = []
        with open(self.path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for line in lines:
            if line.startswith("fio,"):
                rows.append(line)
                continue
            if line.strip() and not line.startswith(fio + ","):
                rows.append(line)

        with open(self.path, "w", encoding="utf-8") as f:
            f.writelines(rows)

    def update(self, fio: str, **fields):
        students = self.list()
        for s in students:
            if s.fio == fio:
                for k, v in fields.items():
                    setattr(s, k, v)
                break

        with open(self.path, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter=",")
            w.writerow(["fio", "birthdate", "group", "gpa"])
            for s in students:
                w.writerow([s.fio, s.birthdate, s.group, s.gpa])

if __name__ == "__main__":
    g = Group(r"C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab09\students.csv")

g.add(Student("Иванов Иван", "2003/10/10", "БИВТ-21-1", 4.3))
g.add(Student("Петров Пётр", "2004/05/01", "БИВТ-21-2", 3.9))
g.add(Student("Сидоров Семён", "2002/12/12", "БИВТ-21-1", 4.7))


for s in g.list():
    print(s.fio, s.birthdate, s.group, s.gpa)

for s in g.find("Иван"):
    print(s.fio, s.group)

g.update("Иванов Иван", gpa=4.9)

g.remove("Петров Пётр")

