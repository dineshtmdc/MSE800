
class FactorialCalculator :

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


# Example usage:
num = int(input("Enter a number: "))
calculator = FactorialCalculator(num) 
print(f"The factorial of {num} is: {calculator.compute_factorial()}")
