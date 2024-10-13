"""
10-Study about Recursive Functions in python.
Explain in details that how does the following recursive function work?
"""


def factorial(x):
    if x == 1:  # This is the base case
        return 1
    else:  # This is the recursive case
        return x * factorial(x - 1)


print(factorial(4))
