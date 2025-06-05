FAHRENHEIT_TO_CELSIUS_FACTOR = (5/9)
CELSIUS_TO_FAHRENHEIT_FACTOR = (9/5)

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    
temperature = input("Enter the temperature to convert: ")
temperature_conversion = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

if temperature.isdigit() != True:
    print("Invalid temperature. Please enter a numeric value.")
else:
    match temperature_conversion:
        case "C":
            result = convert_to_fahrenheit(int(temperature))
            print(f"{temperature}°C is {result}°F")
        case "F":
            result = convert_to_celsius(int(temperature))
            print(f"{temperature}°F is {result}°C")
        case _:
            print("Invalid temperature unit. Please select a valid unit")
