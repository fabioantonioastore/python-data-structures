def gcd(n1: int, n2: int) -> int:
    while n2 != 0:
        t = n2
        n2 = n1 % n2
        n1 = t
    return n1
