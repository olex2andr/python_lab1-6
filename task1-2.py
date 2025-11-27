# -------------------------------
# Завдання 1
# Задано матрицю X(n, n), n ≤ 15. Перетворити матрицю так, щоб добутки
# елементів рядків утворювали неспадну послідовність.

def row_product(row):
    product = 1
    for el in row:
        product *= el
    return product


def sort_by_row_products(matrix):
    return sorted(matrix, key=row_product)

print("\nЗавдання 1:")
n = int(input("Введіть розмір матриці n (≤ 15): "))
matrix = []

for i in range(n):
    row = list(map(int, input(f"Введіть {n} елементів {i+1}-го рядка: ").split()))
    matrix.append(row)

sorted_matrix = sort_by_row_products(matrix)

print("\nПеретворена матриця:")
for row in sorted_matrix:
    print(*row)


# -----------------------------
# Завдання 2
# Є n=10 команд з різною кількістю очок. Потрібно визначити:
# (a) чемпіона,
# (b) команди на 2 і 3 місці,
# (c) команди, що зайняли 1 і 2 місце, використовуючи два проходи по масиву.

print("\nЗавдання 2:")

n = int(input("Введіть кількість команд: "))
teams = []
points = []

for i in range(n):
    name = input(f"Назва команди {i+1}: ")
    pts = int(input(f"Кількість очок для {name}: "))
    teams.append(name)
    points.append(pts)

max_points = max(points)
champion = teams[points.index(max_points)]
print(f"\n(a) Чемпіон: {champion}")

sorted_indices = sorted(range(n), key=lambda i: points[i], reverse=True)
second = teams[sorted_indices[1]]
third = teams[sorted_indices[2]]
print(f"(b) 2 місце: {second}, 3 місце: {third}")

first_max = max(points)
first_index = points.index(first_max)

second_max = -1
second_index = -1
for i in range(n):
    if i != first_index and points[i] > second_max:
        second_max = points[i]
        second_index = i

print(f"(c) 1 місце: {teams[first_index]}, 2 місце: {teams[second_index]}")


# ----------------------------
# Завдання 3
# Є словник з пар слів-синонімів. Для заданого слова знайти його синонім.
# Кожне слово має лише один синонім, і всі слова різні.

print("\nЗавдання 3:")

pairs = [
    ("Hello", "Hi"),
    ("Bye", "Goodbye"),
    ("List", "Array")
]
word = "Goodbye"

synonyms = {}
for w1, w2 in pairs:
    synonyms[w1] = w2
    synonyms[w2] = w1

if word in synonyms:
    print("Синонім:", synonyms[word])
else:
    print("Слова немає у словнику")
