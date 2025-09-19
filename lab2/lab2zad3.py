# 1. Словарь с именами студентов и их оценками, вычисление среднего балла
students = {
    "Иван": 85,
    "Мария": 92,
    "Алексей": 78,
    "Ольга": 95,
    "Сергей": 88
}
average_score = sum(students.values()) / len(students)
print("Оценки студентов:", students)
print(f"Средний балл: {average_score:.2f}")

# 2. Подсчет количества каждой буквы в строке
text = input("\nВведите строку: ")
letter_count = {}
for char in text:
    if char.isalpha():  # Учитываем только буквы
        letter_count[char] = letter_count.get(char, 0) + 1
print("Количество каждой буквы:", letter_count)

# 3. Словарь с числами от 1 до 10 и их квадратами
squares = {}
for i in range(1, 11):
    squares[i] = i ** 2
print("\nЧисла и их квадраты:", squares)

# 4. Словарь из двух списков
keys = ["имя", "возраст", "город"]
values = ["Артём", 20, "Кемерово"]
combined_dict = {}
for i in range(len(keys)):
    combined_dict[keys[i]] = values[i]
print("\nСловарь из двух списков:", combined_dict)