import pytest
from lab05.json_csv import json_to_csv, csv_to_json
from pathlib import Path
import csv
import json
import os


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]
    src.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    try:
        json.loads(Path(src).read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        raise ValueError

    with dst.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    assert len(rows) == 2
    assert {"name", "age"} <= set(rows[0].keys())


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    data = "name,age\nAlice,22\nBob,25\n"

    src.write_text(data, encoding="utf-8")
    csv_to_json(str(src), str(dst))
    if not src.exists():
        raise FileNotFoundError
    if not dst.exists():
        raise FileNotFoundError
    if os.path.getsize(src) == 0:
        raise ValueError
    with src.open(encoding="utf-8") as ff:
        reader = csv.DictReader(ff)
        if reader.fieldnames is None:
            raise ValueError

    result = json.loads(dst.read_text("utf-8"))

    assert result == [
        {"name": "Alice", "age": "22"},
        {"name": "Bob", "age": "25"},
    ]


# py -m pytest -q
