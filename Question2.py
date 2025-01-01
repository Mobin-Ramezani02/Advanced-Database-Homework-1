"""
2 - Write a program to compute the following expression for 500 sentences:
(3! / 2+9) − (5! / 3+7) + (7! / 4+5) − (9! / 5+3) + (11! / 6+1) − (13! / 7−1) …
"""

import math
from decimal import Decimal, getcontext

getcontext().prec = 200

def compute_expression(n):
    result = Decimal(0)
    sign = -1
    for i in range(n):
        sign *= -1
        numerator = (2 * i) + 3
        denominator = Decimal(i + 2) + Decimal(9 - (2 * i))

        if denominator == 0:
            print(f"division by zero in n = {i+1} and continue.")
            continue

        term_value = Decimal(math.factorial(numerator) / denominator)
        result += Decimal(sign) * term_value

    return result

n = int(input("Enter n:"))
result = compute_expression(n)
print("result:", result)
