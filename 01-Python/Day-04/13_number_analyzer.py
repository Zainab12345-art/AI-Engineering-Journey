# Day-04: Mini Project
# PRACTICAL 13: Number Analyzer using for loop
# Lesson 02: for loop

sum = 0
average = 0
largest = 0
smallest = 0
even_count = 0
odd_count = 0
for i in range (5):
    num = int(input('Enter numbers: '))
    sum = sum + num
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
    if i == 0:            # Checks if this is the first number
        largest = num     # Sets the first number as the largest
        smallest = num    # Sets the first number as the smallest
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
average = sum/5
print (f'Sum of Numbers: {sum}.')
print (f'Average of Numbers is: {average}.')
print (f'Total Even Numbers are: {even_count}.')
print (f'Total Odd Numbers are: {odd_count}.')
print (f'Largest Number is: {largest}.')
print (f'Smallest Number is: {smallest}.')

    