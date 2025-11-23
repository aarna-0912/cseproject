import book_operations as bo
import search_and_stats as ss
from data_storage import load_data, save_data

 # Global variable to hold the main application data (list of book dictionaries)
LIBRARY_DATA = []


def display_menu():
     """Displays the main menu options to the user."""
     print("\n" + "=" * 50)
     print(" DIGITAL LIBRARY MANAGEMENT SYSTEM (DLMS) ".center(50))
     print("=" * 50)
     print("1. Add New Book")
     print("2. View All Books")
     print("3. Search Books (by Title, Author, or Genre)")
     print("4. Update Book Details")
     print("5. Delete Book")
     print("6. Generate Statistics Report")
     print("7. Exit Application")
     print("-" * 50)


def main():
     """Main function to run the application loop."""
     global LIBRARY_DATA

     # Load data from the file system when the application starts
     # This is part of the error handling and reliability non-functional requirement
     try:
         LIBRARY_DATA = load_data()
         print(f"Successfully loaded {len(LIBRARY_DATA)} books from data file.")
     except FileNotFoundError:
         print("Data file not found. Starting with an empty library.")
     except Exception as e:
         # Generic error handling for loading
         print(f"An error occurred during data loading: {e}. Starting with an empty library.")
         LIBRARY_DATA = []

     while True:
         display_menu()

         # Non-functional Requirement: Usability - Clear input/output structure
         choice = input("Enter your choice (1-7): ").strip()

         # Functional Module 1: Book Operations (CRUD)
         if choice == '1':
             bo.add_book(LIBRARY_DATA)
         elif choice == '2':
             bo.view_all_books(LIBRARY_DATA)
         elif choice == '4':
             bo.update_book(LIBRARY_DATA)
         elif choice == '5':
             bo.delete_book(LIBRARY_DATA)

         # Functional Module 2: Search and Reporting
         elif choice == '3':
             ss.search_books(LIBRARY_DATA)
         elif choice == '6':
             ss.generate_stats(LIBRARY_DATA)

         elif choice == '7':
             print("Saving data before exit...")
             # Non-functional Requirement: Reliability - Ensure data persistence on exit
             save_data(LIBRARY_DATA)
             print("Data saved. Thank you for using DLMS. Goodbye!")
             break

         else:
             # Non-functional Requirement: Error Handling Strategy
             print("\nError: Invalid choice. Please enter a number from 1 to 7.")

         # Optional: Save data after every major operation for increased reliability
         if choice in ['1', '4', '5']:
             save_data(LIBRARY_DATA)


if __name__ == "__main__":
     main()