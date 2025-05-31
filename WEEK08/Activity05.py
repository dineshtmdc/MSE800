# Parent class
class Animal:
    def speak(self):
        print("The animal makes a sound.")

# Child class 1
class Dog(Animal):
    def bark(self):
        print("The dog barks.")

# Child class 2
class Cat(Animal):
    def meow(self):
        print("The cat meows.")

# Create an instance of Dog
my_dog = Dog()
print("Dog says:")
my_dog.speak()   # Inherited from Animal
my_dog.bark()    # Defined in Dog

print("\nCat says:")
# Create an instance of Cat
my_cat = Cat()
my_cat.speak()   # Inherited from Animal
my_cat.meow()    # Defined in Cat 
# my_cat.brak()   # we can't call brak methon through the cat instance
