import argparse
from pathlib import Path
from ..lab03.src.lib.text import my_top_n


def main() -> None:
    parser = argparse.ArgumentParser(description="CLI‑утилиты лабораторной №6")
    subparsers = parser.add_subparsers(dest="command")

    # подкоманда cat
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True)
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")

    # подкоманда stats
    stats_parser = subparsers.add_parser("stats", help="Частоты слов")
    stats_parser.add_argument(
        "--input", required=True, help="Просто путь, если абсюоютный то в ' ' "
    )
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Сколько значений вывести, по умолчанию 5"
    )

    args = parser.parse_args()

    if args.command == "cat":
        result = []
        k = 0
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")
        with open(p, encoding="utf-8") as ff:
            for line in ff:
                if args.n:
                    k += 1
                    result.append(str(k) + "." + " " + line.strip())
                else:
                    result.append(line.strip())
        for i in result:
            print(i)
    elif args.command == "stats":
        freq = {}
        p = Path(args.input)
        if not p.exists():
            parser.error("Файл не существует")
        if not p.is_file():
            parser.error("Это не файл")
        with open(p, encoding="utf-8") as f:
            for line in f:
                for slovo in line.split():
                    freq[slovo] = freq.get(slovo, 0) + 1
        top_n1 = my_top_n(freq, args.top)
        for word, count in top_n1:
            print(f"{word}: {count}")


if __name__ == "__main__":
    main()

# Запускать из корнивища: C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs>
# ЧТО НУЖНО ПИСАТЬ В КОНСОЛЬ (для stats): py -m scr.lab06.cli_text stats --input "C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab06\text.txt" --top 5
# ИЛИ ДЛЯ cat: py -m scr.lab06.cli_text cat --input "C:\Users\kiri-\OneDrive\Documents\GitHub\python_labs\data\lab06\text.txt" -n
