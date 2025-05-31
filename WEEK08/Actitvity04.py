# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("The dog barks.")

# Creating an instance of Dog
my_dog = Dog()

# Calling method from parent class
my_dog.speak()

# Calling method from child class
my_dog.bark()
