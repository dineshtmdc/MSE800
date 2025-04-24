import numpy as np

# Temperature data in Celsius for a week
temperatures = np.array([18.5, 19, 20, 25.0, 2, 30, 13.9])


# Print the average temperature
average_temp = np.mean(temperatures)
print(f"Average Temperature {average_temp:.2f}°C")

# Find the highest and lowest temperature
max_temp = np.max(temperatures)
min_temp = np.min(temperatures)
print(f"Highest Temperature : {max_temp}°C")
print(f"Lowest Temperature : {min_temp}°C")

# Convert all temperatures to Fahrenheit
fahrenheit = temperatures * 9/5 + 32
print(f"Temperatures in Fahrenheit:", fahrenheit)

# Identify the days (by index) where the temperature was above 20°C
above_20_indices = np.where(temperatures > 20)
print("Days with temperature above 20°C (by index):", above_20_indices)
