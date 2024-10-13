import numpy as np

"""
6 - Write a program to get n and then n numbers from user and compute maximum, minimum, average and 
standard deviation. Test your program for 5 different inputs.
input:
Enter the n:5
Enter number 1:12
Enter number 2:15
Enter number 3:9
Enter number 4:11
Enter number 5:84

output:
Maximum is: 84
Minimum is: 9
Average is: 26.2
Standard Deviation is: 28.96

"""

numbers = []
n = int(input("Enter the n:"))
for i in range(n):
    number = int(input(f"Enter number {i+1}:"))
    numbers.append(number)

numbers = np.array(numbers)
maximum = np.max(numbers)
minimum = np.min(numbers)
average = np.mean(numbers)
std = np.std(numbers)  # standard deviation

print("Maximum is:", maximum)
print("Minimum is:", minimum)
print("Average is:", average)
print(f"Standard Deviation is: {std:.2f}")
