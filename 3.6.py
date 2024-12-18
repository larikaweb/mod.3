def calculate_structure_sum(data):
    total_sum = 0

    if isinstance(data, (list, tuple, set)):  # Если это список, кортеж или множество
        for item in data:
            total_sum += calculate_structure_sum(item)
    elif isinstance(data, dict):  # Если это словарь
        for key, value in data.items():
            total_sum += calculate_structure_sum(key)  # Обрабатываем ключ
            total_sum += calculate_structure_sum(value)  # Обрабатываем значение
    elif isinstance(data, (int, float)):  # Если это число
        total_sum += data
    elif isinstance(data, str):  # Если это строка
        total_sum += len(data)

    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)