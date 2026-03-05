# Temperaure in celcius and convert in fahrenheit
# Add the option to to choose

convertInto = input("Do You want to convert to Celcius or Fahrenheit?[C/F]")

if (convertInto == "C" or convertInto == "c"):
   tempInF = int(input("Enter temperature in Fahrenheit:"))
   tempInC = (tempInF - 32) * 5 / 9 
elif (convertInto == "F" or convertInto == "f"):
    tempInC = int(input("Enter temperatur in Celcius:"))
    tempInF = (tempInC * 9 / 5) + 32  
else:
    print("Invalid Input please try again!")

print(f"Temperature in celcius : {tempInC}")
print(f"Temperature in fahrenhait : {tempInF}")