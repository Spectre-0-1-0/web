# quadratic_weather_model_file_single.py

with open("weather_input.txt", "r") as file:
    lines = file.readlines()
    a = float(lines[0])
    b = float(lines[1])
    c = float(lines[2])
    t = float(lines[3])

T = a * t**2 + b * t + c
print(f"At time t = {t}, the predicted temperature is {T}°C")