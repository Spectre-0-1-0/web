# quadratic_weather_model_file_multiple.py

def predict_temperature(a, b, c, t):
    return a * t**2 + b * t + c

with open("weather_inputs_multiple.txt", "r") as file:
    for line in file:
        a, b, c, t = map(float, line.strip().split())
        T = predict_temperature(a, b, c, t)
        print(f"For input a={a}, b={b}, c={c}, t={t} → T = {T:.2f}°C")