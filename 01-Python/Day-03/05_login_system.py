# PRACTICAL 05: Login System
# Lesson 02: if+elif+else Statements 
name = 'admin'
passkey = '12345'
username = input('Enter username: ')
password = input('Enter your password: ')

if username == name and password == passkey:
    print('Login Successfully.')
else:
    print('Invalid username or password.')
