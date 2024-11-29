# This program calculates the future value of an investment using compound interest

# Create a function that checks if the input contents are numeric, non-zero (except Goal) or positive values
def validateData(prompt, allowZero=False):
    while True:
        try:
            value = float(input(prompt))
            if (allowZero and value >= 0) or (not allowZero and value > 0):
                return value
            else:
                print("Input must be a positive numeric value." if not allowZero else "Input must be 0 or a positive numeric value.")
        except ValueError:
            print("Input must be a numeric value.")

# Create a function that gets the new account balance after applying monthly interest
def getNewAccountBalance(nOldAccountBalance, nMonthlyInterestRate):
    return nOldAccountBalance + (nMonthlyInterestRate * nOldAccountBalance)

# Ask the user for the necessary information
nDeposit = validateData("What is the original deposit (positive value)? ")
nInterestRate = validateData("What is the interest rate (positive value)? ")
nMonthlyInterestRate = (nInterestRate/100)/12
nNumberOfMonths = int(validateData("What is the number of months (positive value)? "))
nGoal = validateData("What is the goal amount (can enter 0 but not negative)? ", allowZero=True)

# Loop to determine the account balance for each month
nAccountBalance = nDeposit
for nMonth in range(1, nNumberOfMonths + 1): 
    nAccountBalance = getNewAccountBalance(nAccountBalance, nMonthlyInterestRate)

    # Display the current month and account balance
    print(f"Month: {nMonth:>2}  Account Balance: $ {nAccountBalance:,.2f}")

# Loop to determine how many months it will take of compounding to reach the Goal amount
if nGoal > 0:
    nMonth = 0
    nAccountBalance = nDeposit    
    while nAccountBalance < nGoal:
        nAccountBalance = getNewAccountBalance(nAccountBalance, nMonthlyInterestRate)
        nMonth += 1
    print(f"It will take: {nMonth} months to reach the goal of $ {nGoal:,.2f}")