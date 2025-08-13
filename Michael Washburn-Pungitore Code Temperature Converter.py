# Display welcome message
print("Michael's Temp Converter:")

# Prompt for temperature input
fltTemp = float(input("\nEnter a temperature: "))

# Prompt for temperature unit
strScale = input("Is the temp F for Fahrenheit or C for Celsius? ").strip().upper()

# Check for valid scale input
if strScale == "F":
    if fltTemp > 212:
        print("Temp can not be > 212")
    else:
        # Convert Fahrenheit to Celsius
        fltCelsius = (5.0 / 9.0) * (fltTemp - 32)
        print(f"The Celsius equivalent is: {fltCelsius:.1f}")

elif strScale == "C":
    if fltTemp > 100:
        print("Temp can not be > 100")
    else:
        # Convert Celsius to Fahrenheit
        fltFahrenheit = ((9.0 / 5.0) * fltTemp) + 32
        print(f"The Fahrenheit equivalent is: {fltFahrenheit:.1f}")

else:
    print("You must enter a F or C")
