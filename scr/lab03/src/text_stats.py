from lib.text import B_count
from lib.text import B_top_n
from lib.text import B_uni_my

c = "мир Привет Привет, мир! Привет!!!"

print("\nВторое задание\n")
print(f"Всего слов: {B_count(c)}")
print(f"Уникальных слов: {B_uni_my(c)}")
print(f"Топ:\n{B_top_n(c)}")
