
class Student:
    def __init__(self, name):
        self.name = name
        # Dictionary to hold subject:grade pairs                   
        self.grades = {}                    

    # Method to add or update a grade for a subject
    def add_grade(self, subject, grade):
         # Add subject and grade to dictionary
        self.grades[subject] = grade       
        print(f"Grade '{grade}' added for subject '{subject}'.")

    # Method to display all results for the student
    def show_results(self):
        if not self.grades:
            print(f"{self.name} has no grades recorded.")
        else:
            print(f"Results for {self.name}:")
            # Print each subject and its grade
            for subject, grade in self.grades.items():
                print(f"  {subject}: {grade}")   


# Dictionary to store all students by name
students = {}

# Main loop for menu-driven program
while True:
    # Display menu options
    print("\nStudent Grading System Menu:")
    print("1. Create a New Student")
    print("2. Add Grade to Student")
    print("3. Show Student Results")
    print("4. Exit")
    
    # Take user input
    choice = input("Enter your choice (1-4): ")

    # Option 1: Create a new student
    if choice == '1':
        name = input("Enter student name: ")
        # Avoid duplicates
        if name in students:
            print(f"Student '{name}' already exists.")  
        else:
            # Create new student object
            students[name] = Student(name)              
            print(f"Student '{name}' created.")

    # Option 2: Add grade to an existing student
    elif choice == '2':
        name = input("Enter student name: ")
         # Check if student exists
        if name not in students:
            print(f"Student '{name}' not found.")      
        else:
            subject = input("Enter subject name: ")
            grade = input("Enter grade (e.g., A, B+, 75): ")
            # Add grade to student
            students[name].add_grade(subject, grade)    

    # Option 3: Show results for a student
    elif choice == '3':
        name = input("Enter student name to show results: ")
         # Validate student
        if name not in students:
            print(f"Student '{name}' not found.")      
        else:
             # Display results
            students[name].show_results()              

    # Option 4: Exit the program
    elif choice == '4':
        print("Exiting the program.")
        break

    # Invalid menu choice
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
