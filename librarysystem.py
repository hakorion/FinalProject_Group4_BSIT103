library_books = []
borrowed_books = {}

# Functions for Admin operations
def add_book():
    """Add a book to the library (Admin only)."""
    book_name = input("Enter the name of the book to add: ").strip()
    if book_name:
        library_books.append(book_name)
        print(f'Book "{book_name}" has been added to the library.')
    else:
        print("Invalid book name! Please try again.")

def remove_book():
    """Remove a book from the library (Admin only)."""
    book_name = input("Enter the name of the book to remove: ").strip()
    if book_name in library_books:
        library_books.remove(book_name)
        print(f'Book "{book_name}" has been removed from the library.')
    else:
        print(f'Book "{book_name}" not found in the library.')

# Common Functions
def display_books():
    """Display all books in the library."""
    if library_books:
        print("\nBooks currently available in the library:")
        for idx, book in enumerate(library_books, start=1):
            print(f"{idx}. {book}")
    else:
        print("\nNo books available in the library.")

def search_books():
    """Search for a book in the library."""
    search_query = input("Enter the name of the book to search: ").strip().lower()
    found_books = [book for book in library_books if search_query in book.lower()]
    
    if found_books:
        print("\nBooks matching your search query:")
        for idx, book in enumerate(found_books, start=1):
            print(f"{idx}. {book}")
    else:
        print("No matching books found in the library.")

# Functions for Borrowing and Returning
def borrow_book():
    """Borrow a book from the library."""
    user_name = input("Enter your name: ").strip()
    book_name = input("Enter the name of the book to borrow: ").strip()

    if book_name in library_books:
        if book_name not in borrowed_books:
            library_books.remove(book_name)
            borrowed_books[book_name] = user_name
            print(f'Book "{book_name}" has been borrowed by {user_name}.')
        else:
            print(f'Sorry, the book "{book_name}" is already borrowed by {borrowed_books[book_name]}.')
    else:
        print(f'Sorry, the book "{book_name}" is not available in the library.')

def return_book():
    """Return a borrowed book to the library."""
    user_name = input("Enter your name: ").strip()
    book_name = input("Enter the name of the book to return: ").strip()

    if book_name in borrowed_books and borrowed_books[book_name] == user_name:
        library_books.append(book_name)
        del borrowed_books[book_name]
        print(f'Book "{book_name}" has been returned by {user_name}.')
    else:
        print(f'The book "{book_name}" was not borrowed by {user_name} or does not exist in borrowed records.')

def display_borrowed_books():
    """Display all borrowed books."""
    if borrowed_books:
        print("\nList of borrowed books:")
        for book, user in borrowed_books.items():
            print(f'Book: "{book}" - Borrowed by: {user}')
    else:
        print("\nNo books are currently borrowed.")

# Menus
def admin_menu():
    """Administrator menu for managing library."""
    while True:
        print("\nAdministrator Menu")
        print("1. Add a Book")
        print("2. Remove a Book")
        print("3. Display Available Books")
        print("4. Display Borrowed Books")
        print("5. Search for a Book")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            display_books()
        elif choice == '4':
            display_borrowed_books()
        elif choice == '5':
            search_books()
        elif choice == '6':
            print("Exiting administrator menu. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

def student_menu():
    """Student menu for borrowing and returning books."""
    while True:
        print("\nStudent Menu")
        print("1. Display Available Books")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Search for a Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            display_books()
        elif choice == '2':
            borrow_book()
        elif choice == '3':
            return_book()
        elif choice == '4':
            search_books()
        elif choice == '5':
            print("Exiting student menu. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Main Program
def main():
    """Main function to run the program."""
    while True:
        print("\nLibrary Management System")
        print("1. Admin Menu")
        print("2. Student Menu")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            admin_menu()
        elif choice == '2':
            student_menu()
        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Start the program
if __name__ == "__main__":
    main()