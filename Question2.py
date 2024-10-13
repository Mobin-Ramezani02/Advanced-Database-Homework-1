import math

"""
2 - Write a program to compute the following expression for 500 sentences:
(3! / 2+9) − (5! / 3+7) + (7! / 4+5) − (9! / 5+3) + (11! / 6+1) − (13! 7−1) …
"""


def compute_expression(n):
    change_sign = True
    sign = 1
    fact_start = 3
    first_num = 2
    second_num = 9
    result = 0
    for _ in range(n):
        fact = math.factorial(fact_start)
        result += sign * (fact / (first_num + second_num))
        fact_start += 2
        first_num += 1
        second_num -= 2
        if change_sign:
            sign = -1
            change_sign = False
        else:
            sign = 1
            change_sign = True

    return result


print(compute_expression(500))  # 12 is error
