outstandingBalance = float(raw_input('Enter the outstanding balance on your credit card: '))
annualInterestRate = float(raw_input('Enter the annual credit card interest rate as a decimal: '))
minMonthlyPaymentRate = float(raw_input('Enter the minimum monthly payment rate as a decimal: '))

totalAmountPaid = 0
for months in range(1,13):
    print 'Month: ', months

    minMonthlyPayment = minMonthlyPaymentRate * outstandingBalance
    interestPaid = (annualInterestRate/12) * outstandingBalance
    principlePaid = minMonthlyPayment - interestPaid

    outstandingBalance = outstandingBalance - principlePaid   
    
    totalAmountPaid += minMonthlyPayment
    print 'Minimum monthly payment: ','$' ,round(minMonthlyPayment, 2)
    print 'Principle paid: ','$', round(principlePaid, 2)
    print 'Remaining balance: ','$',round(outstandingBalance,2)
        

print 'RESULT'
print 'Total Amount Paid: ','$', round(totalAmountPaid, 2)
print 'Remaining Balance: ','$', round(outstandingBalance, 2)
