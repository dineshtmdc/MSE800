# Factorial function definition
def factorial(n):

    # Check if the input number is negative
    if n < 0:
        return ("Factorial is not defined for negative numbers")
    # Base case: factorial of 0 is 1
    elif n == 0:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        result = 1
        # Loop from 1 to n (inclusive)
        for i in range(1, n + 1):
            result = result * i # Multiply result by the current number
        return result

## test for -3
print(f'factorial -3! :{factorial(-3)}')
## test for 0
print(f'factorial 0 :{factorial(0)}')
## test for 4
print(f'factorial 4! :{factorial(4)}')
