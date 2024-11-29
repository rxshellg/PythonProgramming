# This program calculates the total cost of a painting job.

import math

def main():
    # Ask the user for the necessary information
    nWallSquareFeet = getFloatInput("Enter wall space in square feet: ")
    nPaintPrice = getFloatInput("Enter paint price per gallon: ")
    nFeetPerGallon = getFloatInput("Enter feet per gallon: ")
    nLaborHoursPerGallon = getFloatInput("How many labor hours per gallon: ")
    nPaintingChargePerHour = getFloatInput("Labor charge per hour: ")
    sJobState = input("State job is in: ").upper()
    sCustomerLastName = input("Customer last name: ")
    
    # Make the necessary calculations by calling the appropriate functions
    nTotalGallons = getGallonsOfPaint(nWallSquareFeet, nFeetPerGallon)
    nLaborHours = getLaborHours(nLaborHoursPerGallon, nTotalGallons)
    nTotalLaborCost = getLaborCost(nLaborHours, nPaintingChargePerHour)
    nTotalPaintCost = getPaintCost(nTotalGallons, nPaintPrice)
    nSalesTax = getSalesTax(sJobState)

    # Display the results and generate a file with it
    showCostEstimate(nTotalGallons, nLaborHours, nTotalPaintCost, nTotalLaborCost, nSalesTax, sCustomerLastName)

# Create a function that checks if the input contents are positive numeric values
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Input must be a positive numeric value.")
        except ValueError:
            print("Input must be a numeric value.")

# Create a function that returns how many gallons are needed for the job rounded up to the next highest gallon
def getGallonsOfPaint(nWallSquareFeet, nFeetPerGallon):
    nTotalGallons = math.ceil(nWallSquareFeet/nFeetPerGallon)
    return nTotalGallons

# Create a function that returns the Labor Hours to paint the wall
def getLaborHours(nLaborHoursPerGallon, nTotalGallons):
    nLaborHours = nLaborHoursPerGallon * nTotalGallons
    return nLaborHours

# Create a function that returns the Labor Cost to paint the wall
def getLaborCost(nLaborHours, nPaintingChargePerHour):
    nTotalLaborCost = nLaborHours * nPaintingChargePerHour
    return nTotalLaborCost

# Create a function that returns the Paint Cost to paint the wall
def getPaintCost(nTotalGallons, nPaintPrice):
    nTotalPaintCost = nTotalGallons * nPaintPrice
    return nTotalPaintCost

# Create a function that returns the tax rate for the passed in state
def getSalesTax(sJobState):
    if sJobState == "CT" or sJobState == "VT":
        return 0.06
    elif sJobState == "MA":
        return 0.0625
    elif sJobState == "ME":
        return 0.085
    elif sJobState =="RI":
        return 0.07
    else:
        return 0

# Create a function that takes in all the calculated values and outputs them while also creating a file with the same information
def showCostEstimate(nTotalGallons, nLaborHours, nTotalPaintCost, nTotalLaborCost, nSalesTax, sCustomerLastName):

    nSalesTax *= (nTotalPaintCost + nTotalLaborCost)
    nTotalCost = nTotalPaintCost + nTotalLaborCost + nSalesTax

    sOutput= (f"Gallons of paint: {nTotalGallons}\n"
          f"Hours of labor: {nLaborHours} \n"
          f"Paint charges: ${nTotalPaintCost} \n"
          f"Labor charges: ${nTotalLaborCost:.2f} \n"
          f"Tax: ${nSalesTax:.2f} \n"
          f"Total cost: ${nTotalCost:.2f} \n")
    
    print(sOutput)
    sFileName = f"{sCustomerLastName}_PaintJobOutput.txt"
    with open(sFileName, "w") as file:
        file.write(sOutput)
    print(f"File: {sFileName} was created.")

# Call the main function
if __name__ == '__main__':
    main()