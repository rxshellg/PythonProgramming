# This program allows for the numeric entry of 4 test scores, returning the test average and letter grade. Also allows o Drop the Lowest grade and average the other 3 test grades.

# Ask the user for the necessary information
sName = input("Name of the person that we are calculating the grades for: ")
nTest1 = int(input("Test 1: "))
nTest2 = int(input("Test 2: "))
nTest3 = int(input("Test 3: "))
nTest4 = int(input("Test 4: "))
sShouldDropGrade = input("Do you wish to drop the lowest grade Y or N? ").upper()

# Make sure each of the 4 test scores is not less than zero, if yes, end the program
if nTest1 < 0 or nTest2 < 0 or nTest3 < 0 or nTest4 < 0:
    print("Test scores must be greater than 0.")
    exit()

# Check if we have a yes or no, if not, end the program
if sShouldDropGrade not in ["Y", "N"]:
    print(" Enter Y or N to Drop the Lowest Grade.")
    exit()

if sShouldDropGrade == "Y":
    # Determine the lowest test score and average the other three
    if nTest1 <= nTest2 and nTest1 <= nTest3 and nTest1 <= nTest4:
        nAverage = (nTest2 + nTest3 + nTest4) / 3
    elif nTest2 <= nTest1 and nTest2 <= nTest3 and nTest2 <= nTest4:
        nAverage = (nTest1 + nTest3 + nTest4) / 3
    elif nTest3 <= nTest1 and nTest3 <= nTest2 and nTest3 <= nTest4:
        nAverage = (nTest1 + nTest2 + nTest4) / 3
    else:
        nAverage = (nTest1 + nTest2 + nTest3) / 3
else:
    nAverage = (nTest1 + nTest2 + nTest3 + nTest4)/4

# Determine letter grade based on average
if nAverage >= 97.0:
    sGrade = "A+"
elif nAverage >= 94.0:
    sGrade = "A"
elif nAverage >= 90.0:
    sGrade = "A-"
elif nAverage >= 87.0:
    sGrade = "B+"
elif nAverage >= 84.0:
    sGrade = "B"
elif nAverage >= 80.0:
    sGrade = "B-"
elif nAverage >= 77.0:
    sGrade = "C+"
elif nAverage >= 74.0:
    sGrade = "C"
elif nAverage >= 70.0:
    sGrade = "C-"
elif nAverage >= 67.0:
    sGrade = "D+"
elif nAverage >= 64.0:
    sGrade = "D"
elif nAverage >= 60.0:
    sGrade = "D-"
else:
    sGrade = "F"

#Display the results
print(f"{sName}'s test average is: {nAverage:.1f}")
print(f"Letter grade for the test is: {sGrade}")