from database import create_table
from user_manager import add_user, advance_search_user, view_users, search_user, delete_user, add_course,view_course

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
    print("6. Advanced Search Based on ID and Name")
    print("7. Add Course")
    print("8. View All Course")
    print("9. Enroll Course")

def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        elif choice == '6':
            user_id = input("Enter user ID to advance search: ")
            name = input("Enter name to advance search:")
            users = advance_search_user(user_id, name)
            for user in users:
                print(user)
        elif choice == '7':
            name = input("Enter Course name: ")
            units = input("Enter Course units: ")
            add_course(name, units)
        elif choice == '8':
            course = view_course()
            for course in course:
                print(course)
        elif choice == '9':
            course = view_course()
            for course in course:
                print(course)
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
