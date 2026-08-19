# PRACTICAL 10: Movie Ticket Booking 
# Lesson 03: nested if Statements 
age = int(input('Enter your age: '))
student = input('Are you a student? (Yes / No) ')
if age < 5:
    print('Ticket is free.')
elif age >= 5 and age <= 17:
    print('Ticket price: 500.')
else:
    if age >= 18:
        if student == 'Yes' or student == 'yes':
            print('Ticket price: 600.')
        else:
            print('Ticket price: 800.')