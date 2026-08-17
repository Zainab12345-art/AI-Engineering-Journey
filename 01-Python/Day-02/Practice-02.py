# Day 02: Practice Of Day 01
name = input('What is your name?')
age = int(input('What is your age?'))
city = input('Where do you live?')
goal = input('What is your career goal?')

print('=========================================')
print('               AI Journey                ')
print('=========================================')
print (f'My name is {name}.')
print (f'I am {age} years old.')
print (f'I live in {city}.')
print (f'My career goal is to become {goal}.')
print('=========================================')

# Day 02: Lesson 01: Learn about DataTypes [int, float, string, boolean]
name = 'Zainab'
print(type(name))

# Practical 01: Check DataType (String)
name = 'Ali'
university = 'Quaid-i-Azam university'
career = 'AI Engineer'

print(name)
print(type(name))

print(university)
print(type(university))

print(career)
print(type(career))

# Practical 02: Check DataType (int)
age = 20
semester= 8
marks = 100

print(age)
print(type(age))

print(semester)
print(type(semester))

print(marks)
print(type(marks))

# Practical 03: Check DataType (float)
cgpa = 3.5
height= 5.4
price = 99.9

print(cgpa)
print(type(cgpa))

print(height)
print(type(height))

print(price)
print(type(price))

# Compare values as int, float, string
a = 20
b = 20.5
c = '20'

print (a)
print (type(a))
print (b)
print (type(b))
print (c)
print (type(c))

# Practical 04: Check DataType (Boolean)
is_student = False
is_ai_engineer = True

print (is_student)
print (type(is_student))

print (is_ai_engineer)
print (type (is_ai_engineer))

# Practical 05: Type Conversion (from one type to another)
number = '100'
print(number)
print(type(number))
number = int(number)
print(number)
print(type(number))
number = float(number)
print(number)
print(type(number))

# Lessson 02: OPERATORS
# PRACTICAL 06:  Arithmetic Playground
a = 20
b = 6
addition = a + b
subtract = a - b
multiply = a * b
division = a / b
floor_division = a // b
remainder = a % b
power1 = a ** 2
power2 = b ** 3

print('========================================')
print('        ARITHMETIC PLAYGROUND           ')
print('========================================')
print(f'Number1: {a}')
print(f'Number2: {b}')
print(f'Addition: {addition}')
print(f'Subtraction: {subtract}')
print(f'Multiplication: {multiply}')
print(f'Division: {division}')
print(f'Floor Division: {floor_division}')
print(f'Remainder: {remainder}')
print(f'Power of a: {power1}')
print(f'Power of b: {power2}')
print('========================================')

# Lessson 03: Comparison OPERATORS
# PRACTICAL 07: Comparison Playground
age = 20
print ('==================================')
print ('      COMPARISON PLAYGROUND       ')
print ('==================================')
print (f'Age: {age}')
print (f'Age > 18: {age > 18}')
print (f'Age < 18: {age < 18}')
print (f'Age >= 20: {age >= 20}')
print (f'Age <= 20: {age <= 20}')
print (f'Age == 20: {age == 20}')
print (f'Age != 20: {age != 20}')
print ('==================================')

# Lessson 04: Logical OPERATORS
# PRACTICAL 08: Logical Playground
age = 20
is_student = True

print ('==================================')
print ('        LOGICAL PLAYGROUND        ')
print ('==================================')
print (f'Age: {age}')
print  (f'Is Student: {is_student}')
print (f'Age > 18 and Age < 25: {age > 18 and age < 25}')
print (f'Age > 25 and Is Student: {age > 25 and is_student}')
print (f'Age < 18 or Age > 18: {age < 18 or age > 18}')
print (f'Age < 18 or Age > 25: {age < 18 or age > 25}')
print (f'Not Is Student: {not is_student}')
print ('==================================')
