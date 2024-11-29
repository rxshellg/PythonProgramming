## This program calculates the future value of an investment using compound interest

## Ask the user for the necessary information
nPrincipalInvestment = float(input("Enter the starting principal: "))
nInterestRate = float(input("Enter the annual interest rate: "))/100
nCompounding = int(input("How many times per year is the interest compounded? "))
nNumberOfPeriods = float(input("For how many years will the account earn interest? "))

## Calculate the result using the formula for compound interest
nResult = nPrincipalInvestment*(1 + nInterestRate / nCompounding)**(nCompounding * nNumberOfPeriods)

## Print the result for the user
print(f'At the end of {int(nNumberOfPeriods)} years you will have $ {nResult:,.2f}')