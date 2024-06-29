import csv

def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    houses = []
    with open(filename, "r", encoding="UTF-8") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            house = {
                "area_id": row["area_id"],
                "house_address": row["house_address"],
                "floor_count": int(row["floor_count"]),
                "heating_house_type": row["heating_house_type"],
                "heating_value": float(row["heating_value"]),
                "area_residential": float(row["area_residential"]),
                "population": int(row["population"]),
            }
            houses.append(house)
    return houses


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        raise TypeError("Количество этажей должно быть целочисленным значением.")
    if floor_count <= 0:
        raise ValueError("Количество этажей должно быть положительным числом.")
    a = []
    if floor_count <= 5:
        a.append("Малоэтажный")
    elif 6 <= floor_count <= 16:
        a.append("Среднеэтажный")
    else:
        a.append("Многоэтажный")
    return a


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    categories = []
    for house in houses:
        floor_count = house.get("floor_count")
        if floor_count is not None:
            category = classify_house(floor_count)
            categories.append(category)
    return categories


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """
    Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    count_dict = {}
    for category in categories:
        count_dict[category] = count_dict.get(category, 0) + 1
    return count_dict


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца.
    """
    min_area_per_resident = float("inf")
    min_address = ""

    for house in houses:
        area_residential = house.get("area_residential")
        population = house.get("population")
        if area_residential is not None and population is not None and population != 0:
            area_per_resident = area_residential / population
            if area_per_resident < min_area_per_resident:
                min_area_per_resident = area_per_resident
                min_address = house.get("house_address", "")

    return min_address


houses_data = read_file("housing_data.csv")

# Классифицирует дом на основе количества этажей
house = classify_house(int(input("Введите этажность дома: ")))

# Классификация домов на основе количества этажей
classified_houses = get_classify_houses(houses_data)

# Подсчет количества домов в каждой категории
count_categories = get_count_house_categories(classified_houses)

# Нахождение дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца
min_address = min_area_residential(houses_data)

# Печать результатов
print("Классификация дома на основе количества этажей:", house)
print("Классификация домов на основе количества этажей:")
for category, count in count_categories.items():
    print(f"{category[:-1]}х: {count} домов")

print()
print(f"Адрес дома с наименьшим средним количеством квадратных метров жилой площади на одного жильца: {min_address}")
