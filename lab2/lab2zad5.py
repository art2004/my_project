import random

# 1. Список из 20 случайных чисел и вывод уникальных значений
numbers = [random.randint(1, 50) for _ in range(20)]
unique_numbers = list(set(numbers))
print("Исходный список чисел:", numbers, len(numbers))
print("Уникальные значения:", unique_numbers, len(unique_numbers))

# 2. Словарь с элементами списка и количеством их повторений
number_counts = {}
for num in numbers:
    number_counts[num] = number_counts.get(num, 0) + 1
print("\nСловарь с количеством повторений:", number_counts)

# 3. Множество слов длиннее 5 символов
words = ["кошка", "собака", "питон", "Артём", "спать", "хочется", "всегда"]
long_words = {word for word in words if len(word) > 5}
print("\nСписок слов:", words)
print("Множество слов длиннее 5 символов:", long_words)

# 4. Количество вхождений каждого слова в предложении
sentence = input("\nВведите предложение: ")
words = sentence.split()
word_counts = {}
for word in words:
    word_counts[word] = word_counts.get(word, 0) + 1
print("Количество вхождений слов:", word_counts)

# 5. Список чисел в множество и обратно в список (без дубликатов)
numbers = [1, 2, 2, 3, 3, 4, 5, 5, 6]
number_set = set(numbers)
unique_list = list(number_set)
print("\nИсходный список:", numbers)
print("Множество:", number_set)
print("Список без дубликатов:", unique_list)

# 6. Самый дорогой товар в словаре
products = {"хлеб": 50, "молоко": 80, "яблоки": 120, "мясо": 350, "сыр": 200}
most_expensive = max(products.items(), key=lambda x: x[1])
print("\nСловарь товаров и цен:", products)
print(f"Самый дорогой товар: {most_expensive[0]} ({most_expensive[1]} руб.)")

# 7. Имена, встречающиеся более одного раза, и самое частое имя
names = ["Иван", "Мария", "Иван", "Алексей", "Мария", "Ольга", "Иван"]
name_counts = {}
for name in names:
    name_counts[name] = name_counts.get(name, 0) + 1
duplicates = {name: count for name, count in name_counts.items() if count > 1}
most_common = max(name_counts.items(), key=lambda x: x[1])
print("\nСписок имён:", names)
print("Имена, встречающиеся более одного раза:", duplicates)
print(f"Самое частое имя: {most_common[0]} ({most_common[1]} раз)")

# 8. Словарь: символ → индекс первого вхождения
text = input("\nВведите строку: ")
char_index = {}
for i, char in enumerate(text):
    if char not in char_index:
        char_index[char] = i
print("Словарь символов и индексов первого вхождения:", char_index)