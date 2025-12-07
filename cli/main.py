import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from library_manager.inventory import LibraryInventory

def menu():
    print("\n===== Library Menu (NEW VERSION) =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Show All Books")
    print("6. Exit")
    print("======================================")

def main():
    library = LibraryInventory("books.json")

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(title, author, isbn)
            print("Book added successfully!")

        elif choice == "2":
            keyword = input("Enter title or ISBN to search: ")
            results = library.search_book(keyword)
            if results:
                print("\n--- Search Results ---")
                for book in results:
                    print(book)
            else:
                print("No book found!")

        elif choice == "3":
            isbn = input("Enter ISBN to issue: ")
            result = library.issue_book(isbn)
            if result is True:
                print("Book issued successfully!")
            elif result is False:
                print("Book is already issued!")
            else:
                print("Book not found!")

        elif choice == "4":
            isbn = input("Enter ISBN to return: ")
            result = library.return_book(isbn)
            if result is True:
                print("Book returned successfully!")
            elif result is False:
                print("Book was not issued!")
            else:
                print("Book not found!")

        elif choice == "5":
            print("\n--- All Books ---")
            for book in library.books:
                print(book)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()