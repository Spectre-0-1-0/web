# quadratic_weather_model_hardcoded.py

# Sample model: T(t) = at^2 + bt + c, where T is temperature, t is time.
a = -0.5
b = 4
c = 20

# Let's say we want to find temperature at time t = 3
t = 3
T = a * t**2 + b * t + c

print(f"At time t = {t}, the predicted temperature is {T}°C")