import numpy as np

first_10_numbers = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# 1. Print the array
print(f'First Ten Numbers: {first_10_numbers}')

# 2. Print the shape and data type of the array
print(f"Data type of the Array: {first_10_numbers.dtype}")
print(f"The Shape of the Array: {first_10_numbers.shape}")

# 3. Multiply each element by 2 and print the result
multiplied_array = first_10_numbers * 2
print(f'Multify By Two: {multiplied_array}')
