import math

class NumberCheck :

    def __init__(self, number):
      self.number = number      
 
    def compute_factorial(self):

        # Check if the input number is negative
        if self.number < 0:
            return ("Factorial is not defined for negative numbers")
        # Base case: factorial of 0 is 1
        elif self.number == 0:
            return 1
        # Recursive case: n! = n * (n-1)!
        else:
            result = 1
            # Loop from 1 to n (inclusive)
            for i in range(1, self.number + 1):
                result = result * i # Multiply result by the current number
            return result

    # Function to check if the number is a prime number
    def is_prime(self):
        if self.number <= 1:
            return False  # 0 and 1 are not prime
        
    # Check divisibility from 2 up to square root of the number
        for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False  # Found a divisor, so not prime
            return True  # No divisors found, it's a prime number

    def display(self):  
              
        print(f"The factorial of {self.number} is: {self.compute_factorial()}")
        
        if self.is_prime():
            print(f"{self.number} is a Prime Number.")
        else:
            print(f"{self.number} is NOT a Prime Number.")




# Example usage
num = int(input("Enter a number: "))
checker = NumberCheck(num)
checker.display()