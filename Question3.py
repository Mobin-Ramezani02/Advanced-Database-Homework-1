"""
3 - Write a program to print all 4 digits numbers (between 1000 and 9999) that the sum of the first
and second digits is equal with the product of the third and forth digits.
3466: 6 + 6 = 3 × 4
Output: 1110, 1101, ..., 2999 , ... , 3466 , ...
"""

for num in range(1000, 10000):
    number = str(num)
    digit1 = int(number[0])
    digit2 = int(number[1])
    digit3 = int(number[2])
    digit4 = int(number[3])
    if digit1 + digit2 == digit3 * digit4:
        print(num)
