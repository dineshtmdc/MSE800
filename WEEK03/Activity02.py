# Initialize counter
count = 0

# Get stop value from user input with validation
while True:
    try:
        stop_value_str = input("Enter the stop value for the range (must be a non-negative integer): ")
        stop_value = int(stop_value_str)
        if stop_value < 0:
             print("Input cannot be negative. Please enter a non-negative integer.")
             continue # Ask again if negative
        break # Exit loop if input is a valid non-negative integer
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Define the range using user input
loop_range = range(stop_value) 

# Loop through the range and count iterations
for i in loop_range:
    count += 14
    print(f"Iteration {i}, Count: {count}")

# Print the final count after the loop
print(f"The for loop executed {count} times.")