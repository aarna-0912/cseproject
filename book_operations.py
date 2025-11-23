# book_operations.py
# Contains functions for basic CRUD operations on the book data.

def get_book_index(library_data, book_id):
    """
    Helper function to find the index of a book by its ID.
    Returns the index if found, otherwise -1.
    """
    for i, book in enumerate(library_data):
        if book.get('id') == book_id:
            return i
    return -1


def add_book(library_data):
    """
    Functional Module 1a: Prompts the user for book details and adds a new book
    to the library data list.
    """
    print("\n--- ADD NEW BOOK ---")

    # Simple ID generation (uses current length + 1, sufficient for a basic project)
    new_id = len(library_data) + 1

    # Collect mandatory inputs
    while True:
        title = input("Enter Title: ").strip()
        if title:
            break
        print("Title cannot be empty. Please re-enter.")

    author = input("Enter Author: ").strip() or "Unknown"
    genre = input("Enter Genre: ").strip() or "General"

    # Input validation for publication year (Non-functional Requirement: Error Handling)
    year = input("Enter Publication Year (e.g., 2023): ").strip()
    if not year.isdigit() or len(year) != 4:
        year = "N/A"  # Default if invalid input

    new_book = {
        'id': new_id,
        'title': title,
        'author': author,
        'genre': genre,
        'year': year,
        'status': 'Available'  # Default status
    }

    library_data.append(new_book)
    print(f"\n[SUCCESS] Book '{title}' (ID: {new_id}) added to the library.")


def view_all_books(library_data):
    """
    Functional Module 1b: Displays all books in the library.
    """
    print("\n--- ALL LIBRARY BOOKS ---")
    if not library_data:
        print("The library is currently empty.")
        return

    # Non-functional Requirement: Performance - Simple in-memory list traversal
    for book in library_data:
        print(
            f"ID: {book['id']:<4} | Title: {book['title']:<30} | Author: {book['author']:<20} | Year: {book['year']:<5} | Status: {book['status']}")


def update_book(library_data):
    """
    Functional Module 1c: Allows updating the title, author, or status of an existing book.
    """
    print("\n--- UPDATE BOOK DETAILS ---")
    book_id_str = input("Enter the ID of the book to update: ").strip()
    if not book_id_str.isdigit():
        print("[ERROR] Invalid input. Please enter a numerical ID.")
        return

    book_id = int(book_id_str)
    index = get_book_index(library_data, book_id)

    if index != -1:
        book = library_data[index]
        print(
            f"Current details for ID {book_id}: Title='{book['title']}', Author='{book['author']}', Status='{book['status']}'")

        # Update fields (user can leave input blank to keep current value)
        new_title = input(f"Enter new Title (or press Enter to keep '{book['title']}'): ").strip()
        new_author = input(f"Enter new Author (or press Enter to keep '{book['author']}'): ").strip()
        new_status = input(f"Enter new Status (e.g., Available, Loaned, Lost): ").strip()

        if new_title:
            book['title'] = new_title
        if new_author:
            book['author'] = new_author
        if new_status:
            book['status'] = new_status

        print(f"[SUCCESS] Book ID {book_id} updated.")
    else:
        print(f"[ERROR] Book with ID {book_id} not found.")


def delete_book(library_data):
    """
    Functional Module 1d: Removes a book from the library by its ID.
    """
    print("\n--- DELETE BOOK ---")
    book_id_str = input("Enter the ID of the book to delete: ").strip()
    if not book_id_str.isdigit():
        print("[ERROR] Invalid input. Please enter a numerical ID.")
        return

    book_id = int(book_id_str)
    index = get_book_index(library_data, book_id)

    if index != -1:
        deleted_book = library_data.pop(index)
        print(f"[SUCCESS] Book '{deleted_book['title']}' (ID: {book_id}) has been permanently deleted.")
    else:
        print(f"[ERROR] Book with ID {book_id} not found.")