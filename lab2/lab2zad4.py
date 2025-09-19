# 1. Пересечение и объединение двух множеств
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
intersection = set1 & set2
union = set1 | set2
print("Множество 1:", set1)
print("Множество 2:", set2)
print("Пересечение:", intersection)
print("Объединение:", union)

# 2. Уникальные слова в тексте
text = input("\nВведите текст: ")
words = text.split()
unique_words = set(words)
print("Уникальные слова:", unique_words)

# 3. Общие элементы двух списков
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = set(list1) & set(list2)
print("\nСписок 1:", list1)
print("Список 2:", list2)
print("Общие элементы:", common_elements)

# 4. Проверка подмножества
set3 = {7, 8, 9}
set4 = {1, 2, 3, 4, 5}
is_subset = set3.issubset(set4)
print("\nМножество 3:", set3)
print("Множество 4:", set4)
print("Множество 3 является подмножеством множества 4:", is_subset)

# 5. Удаление элементов меньше заданного числа
number_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(f"исходное множество: {number_set}")
threshold = int(input("\nВведите число для удаления элементов меньше него: "))


print("Исходное множество:", number_set)
number_set = {num for num in number_set if num >= threshold}  # Фильтрация элементов
print(f"Множество после удаления элементов меньше {threshold}:", number_set)