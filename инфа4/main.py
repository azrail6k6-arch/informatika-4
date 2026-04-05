# TODO решите задачу
import json # Подключаю модуль, чтобы Python понимал формат JSON
def task() -> float: # Задаю функцию
    filename = 'input.json'

    with open(filename, encoding='utf-8') as f: # Открываю filename с кодировкой utf-8 и присваиваю ему временное имя f
        data = json.load(f) # Выгружаю всё содержимое файла в переменную data

    total_sum = sum(item["score"] * item["weight"] for item in data) # Вычисляею сумму произведений "score" на "weight" для каждого словаря
    return round(total_sum, 3)  # Возвращаю результат, округленный до 3 знаков после запятой

print(task())


