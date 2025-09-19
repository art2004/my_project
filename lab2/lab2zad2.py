import random

# Подготовка списка из 10 случайных чисел
numbers = [random.randint(-5, 5) for _ in range(20)]
print("Исходный список:", numbers)

# 1. Вывод чётных элементов
print("\nЧётные элементы списка:")
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

# 2. Максимальное и минимальное число
max_num = numbers[0]
min_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print(f"\nМаксимальное число: {max_num}")
print(f"Минимальное число: {min_num}")

# 3. Ввод 5 чисел, сохранение в список, сортировка и вывод
user_numbers = []
print("\nВведите 5 чисел:")
for _ in range(5):
    num = int(input("Число: "))
    user_numbers.append(num)
user_numbers.sort()
print("Отсортированный список:", user_numbers)

# 4. Удаление дубликатов
unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
print("\nСписок без дубликатов:", unique_numbers)

# 5. Поменять местами первый и последний элемент
if len(numbers) > 1:
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
print("\nСписок после замены первого и последнего элементов:", numbers)