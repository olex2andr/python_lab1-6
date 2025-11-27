# variant 5, 2

from collections import deque
import inspect
from typing import get_origin, get_args

# 5
def validate_types(func):
    signature = inspect.signature(func)
    annotations = func.__annotations__

    def check_type(value, expected_type):
        origin = get_origin(expected_type)

        if origin is not None:
            return any(isinstance(value, t) for t in get_args(expected_type))

        return isinstance(value, expected_type)

    def wrapper(*args, **kwargs):
        bound = signature.bind(*args, **kwargs)
        bound.apply_defaults()

        for name, value in bound.arguments.items():
            if name in annotations:
                expected_type = annotations[name]
                if not check_type(value, expected_type):
                    raise TypeError(
                        f"Аргумент {name} має тип {type(value).__name__}, "
                        f"коли очікується {expected_type}"
                    )

        return func(*args, **kwargs)

    return wrapper


@validate_types
def calculate_price(name: str, price: int | float, quantity: int) -> float:
    return price * quantity

print(calculate_price("Laptop", 25000, 2))
print(calculate_price("Book", 500.50, 3))
# print(calculate_price("Phone", "20000", 1)) # TypeError

# 2
print()

def sliding_window(data, n):
    window = deque(maxlen=n)

    for value in data:
        window.append(value)
        if len(window) == n:
            yield tuple(window)

data = [1, 2, 3, 4, 5, 6]
windows = sliding_window(data, 3)
print(list(windows))
