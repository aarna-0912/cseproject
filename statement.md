# Problem Statement
In an academic setting, first-year students often begin accumulating numerous books, research papers, and digital resources. It can be challenging to keep track of this growing collection, especially regarding who owns which book, which books are loaned out, or the overall composition of their personal library. There is a need for a simple, accessible, and digital tool to manage this inventory efficiently.
# Scope of the Project
This project provides a simple, console-based library management system for individual users.
In Scope:
1. Book data management (Add, View, Update basic details, Delete).
2. Search and basic statistical reporting.
3. Local file-based data persistence (JSON).
4. Modular design using Python functions and simple data structures (lists of dictionaries).

Out of Scope (Future Enhancements):
1. Graphical User Interface (GUI).
2. Integration with a proper database (like SQLite or Firestore).
3. User login/multi-user functionality (Focus is on single-user application).
4. Handling of external file types (e.g., PDFs, ePubs).

# Target Users
1. First-Year Students: The primary users who need a tool to track their personal academic and leisure reading collections.
2. Hobbyist Book Collectors: Individuals with small-to-medium collections who require a simple, fast way to catalogue their books without complex software.
3. High-Level Features

# The system is built around three major functional modules:
1. Book CRUD Module: Allows the user to create, update, and delete book records in the digital library.
2. Search & Analytics Module: Enables searching the library data by various fields and generating simple distribution reports.
3. Data Persistence Module: Manages the reliable loading and saving of the library's data to a local file, ensuring session continuity.

# Non-Functional Requirements (NF-R) Satisfied
1. NF-R
2. Description
3. Implementation Strategy in DLMS
4. Reliability
5. The system must prevent data loss between sessions.
6. Uses a dedicated data_storage.py module to save and load data from a JSON file upon application start and exit.

# Usability
1. The command-line interface must be clear, simple, and easy to navigate for a beginner user.
2. Simple numbered menus (main.py) and clear, descriptive prompts for all inputs.
3. Error Handling
4. The application should not crash on invalid input (e.g., non-numeric ID, corrupted data file).
5. Includes try-except blocks in main.py (data loading) and input validation checks (e.g., isdigit() in book_operations.py).

#Maintainability
1. The code must be easy to understand, modify, and extend.
2. The project is split into four distinct and focused Python files/modules, with clear function definitions and comments.
