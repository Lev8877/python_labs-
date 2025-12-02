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