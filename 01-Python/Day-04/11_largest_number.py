# PRACTICAL 11: Find largest number using for loop 
# Lesson 02: for loop
largest = 0
for i in range (5):
    num = int(input('Enter Numbers: '))
    if num > largest:
        largest = num
print(f'Largest Number is: {largest}')