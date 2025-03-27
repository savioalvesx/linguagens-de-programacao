class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_checked_out = False

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def check_out_book(self, book):
        if book in self.books and not book.is_checked_out:
            book.is_checked_out = True
            return f"You have checked out '{book.title}'"
        return f"'{book.title}' is not available"

    def return_book(self, book):
        if book in self.books and book.is_checked_out:
            book.is_checked_out = False
            return f"You have returned '{book.title}'"
        return f"'{book.title}' was not checked out"

    def list_books(self):
        return [str(book) for book in self.books]

# Example usage
if __name__ == "__main__":
    library = Library()
    book1 = Book("1984", "George Orwell", 1949)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960)

    library.add_book(book1)
    library.add_book(book2)

    print("Books in library:")
    print(library.list_books())

    print(library.check_out_book(book1))
    print("Books in library after checkout:")
    print(library.list_books())

    print(library.return_book(book1))
    print("Books in library after return:")
    print(library.list_books())