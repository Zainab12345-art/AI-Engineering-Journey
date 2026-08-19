# PRACTICAL 11: Password Strength Checker
# Lesson 03: nested if Statements 
password = input('Enter Your Password: ')
print('The Password Length is: ' , len(password))
if len(password) < 6:
    print('Weak Password.')
elif len(password) >= 6 and len(password) <= 9:
    print('Medium Password.')
else:
    print('Strong Password.')