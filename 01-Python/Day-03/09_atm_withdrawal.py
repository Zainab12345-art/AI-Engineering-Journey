# PRACTICAL 09: ATM Withdrawal 
# Lesson 03: nested if Statements 
balance = float(input('Enter your Account Balance: '))
withdrawal = float(input('Enter Withdrawal amount: '))

if withdrawal <=0:
    print('Invalid Withdrawal amount.')
else:
    if withdrawal > balance:
        print('Insufficient Balance.')
    else:
        remaining_balance = balance-withdrawal
        print('Withdrawal Successful.')
        print(f'Remaining balance: {remaining_balance}')
