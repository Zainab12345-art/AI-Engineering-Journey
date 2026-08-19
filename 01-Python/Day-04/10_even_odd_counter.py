# PRACTICAL 10: Even-Odd counter using for loop 
# Lesson 02: for loop
even_count = 0
odd_count = 0
for i in range(1,11):
    num = int(input('Enter Numbers: '))
    if num % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1
print(f'Total Even Numbers are: {even_count}')
print(f'Total Odd Numbers are: {odd_count}')