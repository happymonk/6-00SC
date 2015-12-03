# Problem Set 1
# Name: 
# Collaborators:
# Time Spent: 

bal = input('Enter Credit Card Balance: ')
APR = input('Enter Annual Interest Rate as decimal: ')
minRate = input('Enter minimum balance due as a decimal: ')

def MinMonthlyPayment(bal,minRate):
    return round(bal * minRate,2)

def MonthlyInterestPaid(bal, APR):
    return APR / 12 * bal

def MinMonthlyPrincipalPaid(bal, APR, minRate):
    return round(MinMonthlyPayment(bal, minRate) -
                 MonthlyInterestPaid(bal, APR),2)

def RemainingBalance():
    global bal
    bal -= round(MinMonthlyPrincipalPaid(bal, APR, minRate),2)
    return bal

def report():
    rpt = "\n"
    paid = 0
    for month in range(1,13):
        paid += MinMonthlyPayment(bal, minRate)
        rpt += ('Month: ' + str(month) + '\n' +
                'Minimum Monthly Payment: $' +
                str(MinMonthlyPayment(bal, minRate)) + '\n' +            
                'Principal Paid: $' +
                str(MinMonthlyPrincipalPaid(bal, APR, minRate)) + '\n' +
                'Remaining Balance: $' +
                str(RemainingBalance()) + '\n\n')

    result = 'Total Paid: $' + str(paid) + '\nRemaining Balance: $' + str(bal)
    print (rpt + result)

report()
        
