# PRACTICAL 12: Find Factorial of a number using for loop
# Lesson 02: for loop
num = int(input('Enter a Number: '))
factorial = 1
for i in range(num, 0, -1):
    factorial = factorial * i
print(f'Factorial of {num} = {factorial}')

