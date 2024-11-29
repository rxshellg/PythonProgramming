## This program displays a person's weight on the different planets within our solar system.

## Ask the user for the necessary information
sName = input("Welcome to the interplanetary weight calculator.\nWhat's your name? ")
nWeight = float(input("How much do you weigh? "))

## Declare constants with each planets Surface Gravity Factor
MERCURY_SGF = 0.38
VENUS_SGF = 0.91
MOON_SGF = 0.165
MARS_SGF = 0.38
JUPITER_SGF = 2.34
SATURN_SGF = 0.93
URANUS_SGF = 0.92
NEPTUNE_SGF = 1.12
PLUTO_SGF = 0.066

##Display the results
print(f'{sName} here are your weights in our Solar System\'s planets:\n'
      f'Weight on Mercury:    {(nWeight * MERCURY_SGF):10.2f}\n'
      f'Weight on Venus:      {(nWeight * VENUS_SGF):10.2f}\n'
      f'Weight on our Moon:   {(nWeight * MOON_SGF):10.2f}\n'
      f'Weight on Mars:       {(nWeight * MARS_SGF):10.2f}\n'
      f'Weight on Jupiter:    {(nWeight * JUPITER_SGF):10.2f}\n'
      f'Weight on Saturn:     {(nWeight * SATURN_SGF):10.2f}\n'
      f'Weight on Uranus:     {(nWeight * URANUS_SGF):10.2f}\n'
      f'Weight on Neptune:    {(nWeight * NEPTUNE_SGF):10.2f}\n'
      f'Weight on Pluto:      {(nWeight * PLUTO_SGF):10.2f}\n')