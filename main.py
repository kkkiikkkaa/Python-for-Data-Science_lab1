import random

matrix = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]

print("Початковий масив:")
for row in matrix:
    print(row)

total_sum = sum(sum(row) for row in matrix)
print("\nСума всіх елементів:", total_sum)

max_value = matrix[0][0]
min_value = matrix[0][0]
max_index = (0, 0)
min_index = (0, 0)

for i in range(3):
    for j in range(3):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = (i, j)
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = (i, j)

print("Максимальне значення:", max_value, "Індекс:", max_index)
print("Мінімальне значення:", min_value, "Індекс:", min_index)

for row in matrix:
    row.sort()

print("\nВідсортований масив по кожному рядку:")
for row in matrix:
    print(row)
