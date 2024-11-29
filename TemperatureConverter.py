# This program converts temperatures between Celsius and Fahrenheit.

# Welcome the user and ask for the necessary information
print("\nWelcome to Rashell's Temperature Converter\n")
nInitialTemperature = float(input("Enter a temperature: "))
sInitialUnit = input("Is the temp F for Fahrenheit or C for Celsius? ").upper()

# Check if a valid unit was inputted
if sInitialUnit == "F" or sInitialUnit == "C":
    # Determine the maximum temperature for Fahrenheit or Celsius
    nMaxTemperature = 212 if sInitialUnit == "F" else 100

    # Check if a valid temperature was inputted
    if nInitialTemperature > nMaxTemperature:
        print(f'Temp can not be > {nMaxTemperature}\n')
    # Display the results
    else:
        nResult = (5/9) * (nInitialTemperature - 32) if sInitialUnit == "F" else ((9/5) * nInitialTemperature) + 32
        sResultUnit = "Celsius" if sInitialUnit == "F" else "Fahrenheit"
        print(f'The {sResultUnit} equivalent is: {nResult:.1f}\n')
else:
    print("Enter a F or C\n")