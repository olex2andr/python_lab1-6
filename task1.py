import numpy as np
import pandas as pd

import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

# PART 1

np.random.seed(42)
n = 250

delivery_time_minutes = np.random.randint(5, 120, size=n)
distance_km = np.random.uniform(0.5, 20.0, size=n)
order_type = np.random.choice(['Food', 'Documents', 'Package'], size=n)
courier_id = np.random.choice([1, 2, 3, 4, 5], size=n)

df = pd.DataFrame({
    'delivery_time_minutes': delivery_time_minutes,
    'distance_km': distance_km,
    'order_type': order_type,
    'courier_id': courier_id
})

df.to_csv("variant_20.csv", index=False)
print("Файл variant_20.csv збережено.\n")

# PART 2

df = pd.read_csv("variant_20.csv")

df["minutes_per_km"] = df["delivery_time_minutes"] / df["distance_km"]

avg_time_by_type = df.groupby("order_type")["delivery_time_minutes"].mean()
avg_minutes_per_courier = df.groupby("courier_id")["minutes_per_km"].mean()

max_courier = avg_minutes_per_courier.idxmax()
max_courier_value = avg_minutes_per_courier.max()

mean_distance = df["distance_km"].mean()
long_trips = df[df["distance_km"] > mean_distance]
avg_long_per_courier = long_trips.groupby("courier_id")["minutes_per_km"].mean()
overall_avg_long = long_trips["minutes_per_km"].mean()

print("Середній час доставки за типами замовлень:")
print(avg_time_by_type, "\n")

print(f"Кур'єр з найбільшою середньою minutes_per_km: {max_courier}")
print(f"Значення: {max_courier_value:.2f}\n")

print("Середній minutes_per_km для довгих поїздок:")
print(avg_long_per_courier, "\n")

print(f"Загальна середня minutes_per_km (довгі поїздки): {overall_avg_long:.2f}\n")

# PART 3

plt.figure(figsize=(9, 5))
plt.hist(df["delivery_time_minutes"], bins=20)
plt.title("Розподіл часу доставки (delivery_time_minutes)")
plt.xlabel("Час доставки (хв)")
plt.ylabel("Кількість доставок")
plt.grid(True)
plt.show()

avg_time_by_courier = df.groupby("courier_id")["delivery_time_minutes"].mean()

plt.figure(figsize=(9, 5))
plt.bar(avg_time_by_courier.index, avg_time_by_courier.values)
plt.title("Середній час доставки для кожного кур'єра")
plt.xlabel("Courier ID")
plt.ylabel("Середній час доставки (хв)")
plt.grid(True)
plt.show()
