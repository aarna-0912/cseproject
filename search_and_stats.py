# search_and_stats.py
# Contains functions for searching the library and generating reports.

def search_books(library_data):
    """
    Functional Module 2a: Searches books by title, author, or genre using case-insensitive matching.
    """
    print("\n--- SEARCH BOOKS ---")
    if not library_data:
        print("Library is empty. Nothing to search.")
        return

    search_term = input("Enter search term (Title, Author, or Genre): ").strip().lower()
    if not search_term:
        print("[INFO] Search term cannot be empty.")
        return

    results = []
    # Functional Requirement: Logical workflow (Iterate and match)
    for book in library_data:
        # Check title, author, and genre fields (Non-functional Requirement: Usability/Flexibility)
        if (search_term in book.get('title', '').lower() or
                search_term in book.get('author', '').lower() or
                search_term in book.get('genre', '').lower()):
            results.append(book)

    print(f"\nFound {len(results)} match(es) for '{search_term}':")
    if results:
        for book in results:
            print(
                f"ID: {book['id']:<4} | Title: {book['title']:<30} | Author: {book['author']:<20} | Genre: {book['genre']:<15} | Status: {book['status']}")
    else:
        print("No matching books found.")


def generate_stats(library_data):
    """
    Functional Module 2b: Generates a simple report on the library composition.
    """
    print("\n--- LIBRARY STATISTICS REPORT ---")

    total_books = len(library_data)
    if total_books == 0:
        print("The library is empty. No statistics to display.")
        return

    # Count by Status (Data Processing)
    status_counts = {}
    # Count by Genre (Analytics/Reporting)
    genre_counts = {}

    for book in library_data:
        # Tally status
        status = book.get('status', 'Unknown')
        status_counts[status] = status_counts.get(status, 0) + 1

        # Tally genre
        genre = book.get('genre', 'Unknown')
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    print(f"Total Books in Library: {total_books}\n")

    print("--- Distribution by Book Status ---")
    for status, count in status_counts.items():
        percentage = (count / total_books) * 100
        print(f"- {status:<10}: {count} books ({percentage:.1f}%)")

    print("\n--- Distribution by Genre ---")
    # Non-functional Requirement: Maintainability (Sorting the output for better readability)
    sorted_genres = sorted(genre_counts.items(), key=lambda item: item[1], reverse=True)
    for genre, count in sorted_genres:
        percentage = (count / total_books) * 100
        print(f"- {genre:<15}: {count} books ({percentage:.1f}%)")

    print("\n[REPORT END]")