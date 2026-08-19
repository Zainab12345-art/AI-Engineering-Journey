# PRACTICAL 07: University Admission Checker
# Lesson 02: nested if Statements 
# I wrote some code, and when the outer condition becomes false,
# it still asks for input for the inner condition. Ideally, this shouldn’t happen. 
# If the outer condition is false, it should skip the inner condition entirely 
# and execute the `else` part of the outer condition instead.
age = int(input('Enter your age: '))
marks = float(input('Enter your marks: '))
if age >= 18:
    if marks >= 60:
        print('You are eligible for Admission.')
    else: 
        print('Your marks are too low.')
else:
    print('You are too young for admission.')


# This is correct code:
age = int(input('Enter your age: '))

if age >= 18:
    marks = float(input('Enter your marks: '))
    if marks >= 60:
        print('You are eligible for Admission.')
    else: 
        print('Your marks are too low.')
else:
    print('You are too young for admission.')