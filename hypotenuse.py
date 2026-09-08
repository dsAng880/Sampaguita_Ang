# DOMINIQUE JILLIAN S. ANG
# 8 - SAMPAGUITA
# ILA 4 - FINDING THE HYPOTENUSE OF A RIGHT TRIANGLE

import math # TO BE ABLE TO USE FUNCTIONS

sideA = input(float("Enter side A:"))
sideB = input(float("Enter side B:"))

sqA = math.pow(sideA,2)
sqB = math.pow(sideB,2)

hypotenuse = math.sqrt(sqA + sqB) # for the program to calculate hypotenuse

print ("The hypotenuse is ", hypotenuse)