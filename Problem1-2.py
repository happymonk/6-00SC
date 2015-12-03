# Problem Set 1
# Name: 
# Collaborators:
# Time Spent:

balance = input('Enter balance: ')
i = input('Enter Annual Interest: ')/12 # monthly interest
LBound = round( balance / 12, -1 )
UBound = ( balance * (1+i)**12 ) / 12
guess = round( ( LBound + UBound ) / 2 , -1 )

def calc12MonthBalance(pmt):
    payment = pmt
    bal = balance
    months = 0
    def report():
        print ('Monthly payment to pay off debt in 1 year: $' + str(pmt) +
            '\nNumber of months needed: ' + str(months) + '\nBalance: ' + str(round(bal,2)))

    for month in range(1,13):
        if bal < 0:
            report()
            break
        else:
            bal = bal * (1+i) - payment
            months = month
            
    if bal > 0:
        calc12MonthBalance(payment + 10)
    else:
        report()

calc12MonthBalance(guess)
