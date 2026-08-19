# PRACTICAL 08: Student Result Analyzer
# Lesson 03: nested if Statements 
name = input('Enter Student name: ')
marks = float(input('Enter marks: '))
if marks < 0 or marks > 100:
    print('Invalid Marks.')
else:
    if marks >= 90:
        print('Your grade is A.')
    elif marks >= 80:
        print('Your grade is B.')
    elif marks >= 70:
        print('Your grade is C.')
    elif marks >= 60:
        print('Your grade is D.')
    else:
        print('Your grade is F.')
    if marks >=60:
            print('Result: Pass.')
    else:
            print('Result: Fail.')  
