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