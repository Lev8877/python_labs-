import argparse
from pathlib import Path
from ..lab05.json_csv import json_to_csv, csv_to_json
from ..lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертеры данных")
    sub = parser.add_subparsers(dest="cmd")

    p1 = sub.add_parser("json2csv",help="Конвертировать JSON в CSV")
    p1.add_argument("--in", dest="input", required=True,help="Входной JSON файл")
    p1.add_argument("--out", dest="output", required=True,help="Выходной CSV файл")

    p2 = sub.add_parser("csv2json",help="Конвертировать CSV в JSON")
    p2.add_argument("--in", dest="input", required=True,help="Входной CSV файл")
    p2.add_argument("--out", dest="output", required=True,help="Выходной JSON файл")

    p3 = sub.add_parser("csv2xlsx",help="Конвертировать CSV в XLSX")
    p3.add_argument("--in", dest="input", required=True,help="Входной CSV файл")
    p3.add_argument("--out", dest="output", required=True,help="Выходной XLSX файл")

    args = parser.parse_args()

    if args.cmd == "json2csv":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл") 
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        json_to_csv(args.input,args.output)

    if args.cmd == "csv2json":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл") 
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        csv_to_json(args.input,args.output)

    if args.cmd == "csv2xlsx":
        pp = Path(args.output)
        if not pp.exists():
            parser.error("Файл не существует")
        if not pp.is_file():
            parser.error("Это не файл")  
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")  
        csv_to_xlsx(args.input,args.output)

if __name__ == "__main__":
    main()

#py -m scr.lab06.cli_convert json2csv --in "C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab06\people.json" --out "C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab06\cli_convert_json2csv.csv"