def fahrenheit__(temp_in_F):
    temperature = temp_in_F
    # Convert Fahrenheit to Celsius
    celsius = (temperature - 32) * (5 / 9)
    if celsius < -273.15:
            # Invalid temperature, below absolute zero
        return "Invalid temperature"
    else:
        # Convert Celsius to Kelvin
        kelvin = celsius + 273.15
        if kelvin < 0:
                # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < -459.67:
                    # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return celsius, kelvin, fahrenheit

def celsius__(temp_in_celsius):
    temperature = temp_in_celsius
    # Convert Celsius to Fahrenheit
    fahrenheit = (temperature * (9 / 5)) + 32
    if fahrenheit < -459.67:
            # Invalid temperature, below absolute zero
        return "Invalid temperature"
    else:
        # Convert Celsius to Kelvin
        kelvin = temperature + 273.15
        if kelvin < 0:
                # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            return temperature, kelvin, fahrenheit

def kelvin__(temp_in_kelvin):
    temperature = temp_in_kelvin
    # Convert Kelvin to Celsius
    celsius = temperature - 273.15
    if celsius < -273.15:
        # Invalid temperature, below absolute zero
        return "Invalid temperature"
    else:
        # Convert Celsius to Fahrenheit
        fahrenheit = (celsius * (9 / 5)) + 32
        if fahrenheit < -459.67:
                # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            return celsius, temperature, fahrenheit
            

def convert_temperature(temperature, unit):
    if unit == "F":
        celsius, kelvin, fahrenheit = fahrenheit__(temperature)
        return celsius, kelvin, fahrenheit
    elif unit == "C":
        celsius, kelvin, fahrenheit = celsius__(temperature)
        return celsius, kelvin, fahrenheit
    elif unit == "K":
        celsius, kelvin, fahrenheit = kelvin__(temperature)
        return celsius, kelvin, fahrenheit
    else:
        return "Invalid unit"



if __name__ == "__main__":
    result=convert_temperature(14, 'F')
    print("Results for 14 F:\t",result)
    result=convert_temperature(-10, 'C')
    print("Results for -10 C:\t",result)
    result=convert_temperature(263.15, 'K')
    print("Results for 263.15 K:\t",result)