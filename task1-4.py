import math
import re

# Завдання 1
def term(k, x, a):
    """Обчислює k-й член ряду."""
    return ((-1) ** k) * (x ** (3 * k)) / (a ** 5 + math.factorial(k))


def series_sum(x, a, eps=1e-8, n_max=10000):
    """Обчислення суми ряду з перевіркою умови точності."""
    s_prev = 0.0
    s_curr = 0.0

    for k in range(1, n_max + 1):
        s_curr = s_prev + term(k, x, a)
        if abs(s_curr - s_prev) < eps:
            print(f"Досягнуто точності при k = {k}")
            break
        s_prev = s_curr

    return s_curr


print("\nЗавдання 1:")
x = float(input("Введіть значення x: "))
a = float(input("Введіть значення a: "))
eps = 1e-8

result = series_sum(x, a, eps)
print(f"Сума ряду для x = {x}, a = {a}, eps = {eps}")
print(f"Результат: {result}\n")


# Завдання 2
def sequence_a(x, n_max=1000, eps=1e-8):
    a_prev = x
    a_curr = a_prev

    for n in range(1, n_max + 1):
        if abs(a_prev) < 1e-15:
            print(f"Помилка: a_{n - 1} ≈ 0, ділення на нуль!")
            return None

        a_curr = (2 / 7) * a_prev + x / (3 * (a_prev ** 5))

        if abs(a_curr - a_prev) < eps:
            print(f"Послідовність збіглася при n = {n}")
            break

        a_prev = a_curr

    return a_curr


print("\nЗавдання 2:")
x2 = float(input("Введіть значення x для послідовності: "))
eps2 = 1e-8

print(f"Границя послідовності a_n для x = {x2}: {sequence_a(x2, eps=eps2)}")


# Завдання 3
def clean_text(text):
    return re.findall(r'\b\w+\b', text.lower())

def remove_words(text1, text2):
    words1 = set(clean_text(text1))
    words2 = text2.split()

    result_words = [word for word in words2 if re.sub(r'\W', '', word.lower()) not in words1]
    return ' '.join(result_words)

print("\nЗавдання 3:")
text1 = input("Введіть перший текст: ")
text2 = input("Введіть другий текст: ")

result = remove_words(text1, text2)
print("\nРезультат: ")
print(result)


# Завдання 4
def is_palindrome(str):
    str = ''.join(str.split()).upper()

    if len(str) <= 1:
        return True

    if str[0] != str[-1]:
        return False

    return is_palindrome(str[1:-1])


print("\nЗавдання 4")
text = input("Введіть рядок: ")

print("YES" if is_palindrome(text) else "NO")
