"""Ask the user to enter a temperature in Celsius. The program should 
print a message based on the temperature (Source: A Practical Introduction
 to Python Programming): 
 
 • If the temperature is less than −273.15, print that the temperature is 
 invalid because it is below absolute zero. 
 
 • If it is exactly −273.15, print that the temperature is absolute 0. 
 
 • If the temperature is between −273.15 and 0,
print that the temperature is below freezing. 

• If it is 0, print that the temperature is at the freezing point. 

• If it is between 0 and 100, print that the temperature is in the 
normal range. 

• If it is 100, print that the temperature is at the boiling point. 

• If it is above 100, print that the temperature is above the 
boiling point."""


#Get user input, convert to float. Using cutoffs in decimals
degCelsius = float(input("Please enter the temperature in Celsius:"))


#set intervals for print messages
if degCelsius > 100:
    print("The temperature is above boilpoint point.")
elif degCelsius == 100:
    print("The temperature is at boilpoint point.")

#using 100 > degCelsius > 0 works in python but could also just use and keyword
elif 100 > degCelsius > 0:
    print("The temperature is in the normal range.")

elif degCelsius == 0:
    print("The temperature is at freezing point.")

elif 0 > degCelsius > -273.15:
    print("The temperature is below freezing.")

elif degCelsius == -273.15:
    print("The temperature is absolute zero.")

#as long as all the above conditions are set correctly dont have to set a elif cutoff here it should always 
#execute for any number below -273.15
else:
    print("The temperature is invalid because it is below absolute zero.")




    
