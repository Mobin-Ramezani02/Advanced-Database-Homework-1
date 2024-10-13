from statistics import mean
import math

"""
7 - Write 4 functions for question 6. Get 5 numbers from user in main. 
Send numbers for Max1, Min1, Ave1 and STD1 functions. Max1 gives n numbers and return maximum. 
Min1 gives n number and return minimum. Ave1 and STD1 give n number and print average and 
standard deviation in their own body and do not return any value. Test your program for 5 different inputs.
"""


def Max1(numbers):
    maximum = numbers[0]
    for num in numbers:
        if num > maximum:
            maximum = num
    print("The Maximum is: ", maximum)


def Min1(numbers):
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    print("The Minimum is: ", minimum)


def Ave1(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    print("The Average is: ", average)


def STD1(numbers):
    ave = mean(numbers)
    total = 0
    for num in numbers:
        total += ((num - ave) ** 2)

    std = math.sqrt(total / len(numbers))
    print(f"The Standard Deviation is: {std:.2f}")


nums = []
n = int(input("Enter the n:"))
for i in range(n):
    number = int(input(f"Enter number {i + 1}:"))
    nums.append(number)

Max1(nums)
Min1(nums)
Ave1(nums)
STD1(nums)
