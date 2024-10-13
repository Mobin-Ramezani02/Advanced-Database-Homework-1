"""
1 - Write a program to get a number and print all its even digits separated by *.
Input: 822145635
Output: 6*4*2*2*8
"""


def evenDigits(number):
    even_digits = [digit for digit in str(number) if int(digit) % 2 == 0]
    return '*'.join(even_digits)


num = 822145635
print(evenDigits(num))
