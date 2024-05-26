def water_state(temperature):
    if temperature <= 0:
        return "Solid"

    if temperature > 0:
        if temperature < 100:
            return "Liquid"

    if temperature >= 100:
        return "Gas"


temp = float(input("Enter the temperature "))
state = water_state(temp)
print(state)
