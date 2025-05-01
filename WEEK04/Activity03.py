class NumberCheck :

    @staticmethod
    def compute_factorial(number):

        # Check if the input number is negative
        if number < 0:
            return ("Factorial is not defined for negative numbers")
        # Base case: factorial of 0 is 1
        elif number == 0:
            return 1
        # Recursive case: n! = n * (n-1)!
        else:
            result = 1
        # Loop from 1 to n (inclusive)
        for i in range(1, number + 1):
            result = result * i # Multiply result by the current number
        return result

    # Function to check if the number is a prime number
    @staticmethod
    def is_prime(number):
        if number <= 1:
            return False  # 0 and 1 are not prime
        
    # Check divisibility from 2 up to square root of the number
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False  # Found a divisor, so not prime
            return True  # No divisors found, it's a prime number


# Example usage
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {NumberCheck.compute_factorial(number)}")

if NumberCheck.is_prime(number):
    print(f"{number} is a Prime Number.")
else:
    print(f"{number} is NOT a Prime Number.")