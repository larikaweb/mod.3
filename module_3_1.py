# Глобальная переменная для подсчета вызовов
calls = 0

def count_calls():
    global calls  # Используем глобальную переменную
    calls += 1  # Увеличиваем счетчик на 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    # Возвращаем кортеж: длина строки, строка в верхнем регистре, строка в нижнем регистре
    return len(string), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()  # Приводим строку к нижнему регистру
    for item in list_to_search:
        if string_lower == item.lower():  # Сравниваем строку с каждым элементом списка
            return True  # Если совпадение найдено, возвращаем True
    return False  # Если совпадения нет, возвращаем False

# Примеры вызовов функций
print(string_info('Capybara'))  # (8, 'CAPYBARA', 'capybara')
print(string_info('Armageddon'))  # (10, 'ARMAGEDDON', 'armageddon')
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # True
print(is_contains('cycle', ['recycling', 'cyclic']))  # False

# Выводим количество вызовов
print(calls)