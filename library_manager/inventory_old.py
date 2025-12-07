from book import Book

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    title, author, isbn, status = line.strip().split(" | ")
                    self.books.append(Book(title, author, isbn, status))
        except FileNotFoundError:
            open(self.filename, "w").close()

    def save_books(self):
        with open(self.filename, "w") as file:
            for book in self.books:
                file.write(str(book) + "\n")

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()

    def search_book(self, keyword):
        return [book for book in self.books if keyword.lower() in book.title.lower() or keyword in book.isbn]

    def issue_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.issue_book():
                    self.save_books()
                    return True
                return False
        return None

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.return_book():
                    self.save_books()
                    return True
                return False
        return None