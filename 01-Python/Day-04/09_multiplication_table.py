# PRACTICAL 09: Write Table of any number using for loop 
# Lesson 02: for loop
num = int(input('Enter a Number: '))
product = 1
for i in range (1,11):
    product = i * num
    print (f'{num} * {i} = {product}')
