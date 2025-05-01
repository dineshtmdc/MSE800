
class Library:
    def __init__(self):
        self.books = []

    # Method to add a book to the library
    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added to the library.")
    
    # Method to display all books in the library
    def show_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Books in the library:")
             # Print each book with its index number
            for idx, book in enumerate(self.books, 1):
                print(f"{idx}. {book}")

# Example usage
library = Library()

while True:

    # Display menu options
    print("\n Library Menu:")
    print("1. Add a Book")
    print("2. Show All Books")
    print("3. Exit")

    # Get the user's choice
    choice = input("Enter your choice (1-3): ")

    # Perform action based on user choice
    if choice == '1':        
        # Ask user for book name and add it to the library
        book_name = input("Enter book name: ")
        library.add_book(book_name)

    elif choice == '2':
        # Show all books in the library
        library.show_books()

    elif choice == '3':
         # Exit the program
        print("Exiting the program.")
        break

    else:
        # Handle invalid input
        print("Invalid choice. Please select 1, 2, or 3.")