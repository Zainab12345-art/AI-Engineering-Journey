# PRACTICAL 06: Age + Student Eligibility
# Lesson 02: if+elif+else Statements 
age = int(input('Enter your age: '))
is_student = input('Are you a student? (Yes/No) ')
if age >= 18 and is_student == 'yes':
    print('You are Eligible.')
else:
    print('You are not Eligible.')