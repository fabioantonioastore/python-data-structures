from typing import Sequence, Union


def min(*numbers: Union[int, float] | Sequence[int | float]) -> int | float:
    numbers_len = len(numbers)
    if numbers_len == 1 and isinstance(numbers[0], Sequence):
        numbers = numbers[0]
        numbers_len = len(numbers)
    a = numbers[0]
    for i in range(1, numbers_len):
        b = numbers[i]
        a = (a + b - abs(a - b)) / 2
    return a
