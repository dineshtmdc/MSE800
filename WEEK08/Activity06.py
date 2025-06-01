
class Person:
    def __init__(self, name, age):     
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, {self.age} years old.")

class Student(Person):
    # Call the constructor of the parent class to set name and age
    def __init__(self, name, age, student_id):        
        super().__init__(name, age)
        self.student_id = student_id

    # Override the parent class method to include student ID
    def introduce(self):        
        print(f"Hi, I'm {self.name}, {self.age} years old, and my student ID is {self.student_id}")


student = Student("Jone", 20, 1234)
student.introduce()
