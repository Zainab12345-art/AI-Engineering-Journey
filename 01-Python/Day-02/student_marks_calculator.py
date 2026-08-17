# Day-02: Mini Project
# Student Marks Calculator
name = input('What is your name?')
python = float(input('Enter Python marks: '))
database = float(input('Enter Database marks: '))
networking = float(input('Enter Networking marks: '))

total_marks = python + database + networking
average_marks = total_marks/3

print('=======================================================')
print('                 STUDENT MARKS REPORT                  ')
print('=======================================================')
print(f'Student Name: {name}')
print(f'Python Marks: {python}')
print(f'Database Marks: {database}')
print(f'Networking Marks: {networking}')

print(f'Total Marks: {total_marks}')
print(f'Average Marks: {average_marks}')
print('=======================================================')