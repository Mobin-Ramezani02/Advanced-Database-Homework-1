"""
4 - Write a program to print all 3 digits numbers (between a 100 and 999) that does not have odd digits.
Consider 0 as even digit.
Output: 200, 202,204, 206,208,220,222,…
"""

for num in range(100, 1000):
    number = str(num)
    digit1 = int(number[0])
    digit2 = int(number[1])
    digit3 = int(number[2])
    if digit1 % 2 == 0 and digit2 % 2 == 0 and digit3 % 2 == 0:
        print(num)

