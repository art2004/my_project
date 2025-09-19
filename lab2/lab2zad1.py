# 1. Таблица умножения от 1 до 9
print("Таблица умножения:")
for i in range(1, 10):
    for j in range(1, 10):
        print(f"{i * j:2}", end="\t")
    print()

# 2. Сумма нечётных чисел от 1 до 100
sum_odd = 0
for i in range(1, 101, 2):
    sum_odd += i
print(f"\nСумма нечётных чисел от 1 до 100: {sum_odd}")

# 3. Делители числа
n = int(input("\nВведите число для поиска делителей: "))
print(f"Делители числа {n}:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=" ")
print()

# 4. Факториал числа
n = int(input("\nВведите число для вычисления факториала: "))
factorial = 1
if n > 0:
    for i in range(1, n + 1):
        factorial *= i
    print(f"Факториал числа {n}: {factorial}")
else:
    print('Факториал не может быть отрицательным!')

# 5. Последовательность Фибоначчи
n = int(input("\nВведите длину последовательности Фибоначчи: "))
fib = [0, 1]
if n > 0:
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    print("Последовательность Фибоначчи:", end=" ")
    for i in range(n):
        print(fib[i], end=" ")
else:
    print('Последовательность не может быть отрицательной!')