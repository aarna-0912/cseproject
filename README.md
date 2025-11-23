# Project Title
Digital Library Management System (DLMS)
# Overview of the Project
The DLMS is a console-based application built using Python to manage a personal collection of books. It provides fundamental data management capabilities (CRUD - Create, Read, Update, Delete) and simple reporting/analytics, fulfilling the requirements for a first-year programming project.
The system is designed to be highly modular, allowing a beginner to easily understand and maintain the code. It uses a JSON file (library_data.json) for data persistence.
# Features
1. Book Management (CRUD): Add new books with ID, Title, Author, Genre, and Year. Update book details (Title, Author, Status). Delete books.
2. Book Viewing: Display a formatted list of all books in the library.
3. Search Functionality: Find books by searching for keywords in the Title, Author, or Genre fields.
4. Reporting: Generate a basic statistics report showing the total number of books and distribution by Status and Genre.
5. Data Persistence: Automatically saves and loads data using a JSON file to ensure the library state is maintained between sessions.

# Technologies/Tools Used
1. Language: Python 3.x (Basic features, no external libraries required beyond standard modules like json and os).
2. Data Storage: Local JSON file (library_data.json) for persistence.
3. Version Control: Git (Assumed to be used for repository management).

# Steps to Install & Run the Project
1. Clone the Repository (Required for Git/GitHub usage):
   
   git clone [YOUR-REPOSITORY-URL]
   
   cd DLMS-Project-Name
2. Ensure Python is Installed:
   Verify you have Python 3.x installed by running:
   python --version
   or 
   python3 --version
3. Run the Application:
4. Execute the main script from the terminal:
   
   python main.py
5. The application will start, load any existing data, and present the main menu.

# Instructions for Testing
1. Adding Books (Test 1): Select option 1. Add at least 3-4 books with different titles, authors, and genres (e.g., Fiction, Science, History).
2. Viewing Books (Test 2): Select option 2. Verify that all the books you added in Test 1 are displayed correctly.
3. Searching (Test 3): Select option 3.
4. Search by a full word (e.g., 'Python'). Verify the correct book(s) appear.
5. Search by a partial keyword (e.g., 'Histor'). Verify matching books appear.
6. Updating (Test 4): Select option 4. Enter the ID of a book. Update its title and status. Select option 2 again to verify the changes took effect.
7. Reporting (Test 5): Select option 6. Verify that the total book count is accurate and the percentages by Genre and Status sum up correctly.
8. Persistence (Test 6 - Reliability/Non-functional):
9. Add a new book (Test 1).
10. Exit the application (option 7).
11. Re-run the application (python main.py).
12. Select option 2. The newly added book should still be present, confirming data was saved and loaded correctly.
