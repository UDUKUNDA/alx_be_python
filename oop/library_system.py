from typing import List


class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author


class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int) -> None:
        super().__init__(title, author)
        self.file_size = file_size


class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count: int) -> None:
        super().__init__(title, author)
        self.page_count = page_count


class Library:
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Only Book, EBook, or PrintBook instances can be added")
        self.books.append(book)

    def list_books(self) -> None:
        for book in self.books:
            if isinstance(book, EBook):
                print(f"'{book.title}' by {book.author} [EBook, file size: {book.file_size}MB]")
            elif isinstance(book, PrintBook):
                print(f"'{book.title}' by {book.author} [PrintBook, pages: {book.page_count}]")
            else:
                print(f"'{book.title}' by {book.author} [Book]")