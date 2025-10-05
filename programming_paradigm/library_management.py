class Library:
    """Represents a library that can store and manage books."""

    def __init__(self):
        self._books = []  # private list to store all the Book objects

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title if it is available."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You checked out '{title}'.")
                    return
                else:
                    print(f"Sorry, '{title}' is already checked out.")
                    return
        print(f"Sorry, '{title}' not found in the library.")

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                book.return_book()
                print(f"Thank you for returning '{title}'.")
                return
        print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books are available right now.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")
