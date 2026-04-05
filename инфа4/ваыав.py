# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:

    ...  # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, encoding="utf-8") as f: # Открываю INPUT_FILENAME с кодировкой utf-8 и присваиваю ему временное имя f
        reader = csv.DictReader(f) # Превращаю каждую строку таблицы в словарь, используя заголовки колонок в качестве ключей
        data = [row for row in reader] # Сохраняю все строки в один словарь

    ...  # TODO Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME,"w", encoding="utf-8") as f: # Открываю OUTPUT_FILENAME для записи с кодировкой utf-8 и присваиваю ему временное имя f
        json.dump(data, f, indent=4) #Записываю список словарей в отдельный файл, параметр indent=4 добавляет отступы


if __name__ == '__main__':
    # Нужно для проверки
    task() # Вызаваю функцию

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
