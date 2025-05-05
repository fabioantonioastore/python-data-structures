from typing import Union, Sequence


def gcd(*numbers: Union[int, float] | Sequence[int | float]):
    numbers_len = len(numbers)
    if numbers_len == 1 and isinstance(numbers[0], Sequence):
        numbers = numbers[0]
        numbers_len = len(numbers)
    a = numbers[0]
    for i in range(1, numbers_len):
        b = numbers[i]
        while b != 0:
            c = b
            b = a % b
            a = c
        if a == 1:
            return a
    return a
