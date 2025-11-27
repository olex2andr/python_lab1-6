import math

print("1) z(a) = sin(a)^2")
a = float(input("Введіть a: "))
result = math.sin(a) ** 2
print(f"z({a}) = {result}\n")

print("2) Розмноження амеб")
hours = int(input("Введіть кількість годин: "))
divisions_count = hours // 3
ameb_count = 1 * (2 ** divisions_count)
print(f"Через {hours} год. буде {ameb_count} амеб\n")

print("3) Робота з масивом")
size = int(input("Введіть кількість елементів: "))
numbers_array = [int(input(f"Елемент {i+1}: ")) for i in range(size)]

negative_numbers = [x for x in numbers_array if x < 0]
if negative_numbers:
    print(f"Максимальний від'ємний елемент: {max(negative_numbers)}")
else:
    print("Від'ємних елементів немає")

odd_numbers = [x for x in numbers_array if x % 2 != 0]
if odd_numbers:
    average_odd = sum(odd_numbers) / len(odd_numbers)
    print(f"Середнє арифметичне непарних елементів: {average_odd}")
else:
    print("Непарних елементів немає")

if negative_numbers:
    print("Від'ємні елементи масиву:", negative_numbers)
else:
    print("Від'ємних елементів немає")
