"""
8 - Give a number with 5 digits in main. If the number is not a 5 digits number, ask repeatedly from user
to enter a valid number. Send the number for F1 function to find and return the maximum digit of the number.
In the next step, send the maximum digit and the input number for F2 function to delete the maximum digit from
number and return it. Finally, print the final output in main as shown in figure below.
"""


def F1(number):
    digits = []
    while number > 0:
        digit = number % 10
        digits.append(digit)
        number //= 10
    maxDigit = max(digits)
    return maxDigit


def F2(number, digit):
    number = str(number).replace(f"{digit}", "").strip()
    return number


num = input("Enter a 5 digits number:")

while True:
    if len(num) == 5 and num.isdigit():
        break
    else:
        print("It is not a 5 digits number.")
        num = input("Please enter a valid number:")

num = int(num)
max_digit = F1(num)
print("The Maximum digit is:", max_digit)
print(f"The Final Digit without {max_digit} is:", F2(num, max_digit))
