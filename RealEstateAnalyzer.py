# This program calculates statistics for property sales at BDJ Real Estate of Springfield.

def main():
    # Initialize necessary variables
    listSalesValues=[]
    sAnotherValue = "Y"
    nTotal = 0

    # Get property values and add to the listSalesValues
    while sAnotherValue.upper() == "Y":
        nSaleValue= getFloatInput("Enter property sales value: ")
        listSalesValues.append(nSaleValue)
        sAnotherValue = getYesOrNoInput("Enter another value Y or N: ")

    # Sort the list from smallest value to largest
    listSalesValues.sort()
    
    # Calculate the total property sales value
    for value in listSalesValues:
        nTotal+= value
    
    # Display the information
    for index in range(len(listSalesValues)):
        print(f"Property {index + 1}  $ {listSalesValues[index]:15,.2f}")
    print(f"{"Minimum:":11} $ {listSalesValues[0]:15,.2f}\n"
          f"{"Maximum:":11} $ {listSalesValues[-1]:15,.2f}\n"
          f"{"Total:":11} $ {nTotal:15,.2f}\n"
          f"{"Average:":11} $ {(nTotal/len(listSalesValues)):15,.2f}\n"
          f"{"Median:":11} $ {getMedian(listSalesValues):15,.2f}\n"
          f"{"Commission:":11} $ {(nTotal*0.03):15,.2f}")

# Create a function that checks if the input contents are positive numeric values
def getFloatInput(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
        except ValueError:
            print("Input a number that is greater than 0.\n")

# Create a function that checks if the input is "Y" for yes or "N" for no
def getYesOrNoInput(prompt):
    while True:
        value = input(prompt).upper()
        if value == "Y" or value == "N":
            return value
        

# Create a function that returns the median of a list of numbers
def getMedian(list):
    nMedianIndex= int(len(list)/2)

    if len(list) % 2 == 0:
        return (list[nMedianIndex] + list[nMedianIndex -1])/2
    else:
        return list[nMedianIndex]

# Call the main function
if __name__ == '__main__':
    main()