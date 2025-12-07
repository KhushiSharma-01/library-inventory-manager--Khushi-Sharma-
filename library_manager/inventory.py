import json
import logging
from .book import Book

logging.basicConfig(
    filename="library.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class LibraryInventory:
    def __init__(self, filename="books.json"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.books = [Book.from_dict(b) for b in data]
            logging.info("Loaded books from JSON.")
        except FileNotFoundError:
            logging.warning("books.json not found, creating new.")
            self.books = []
            self.save_books()
        except json.JSONDecodeError:
            logging.error("JSON corrupted! Creating fresh file.")
            self.books = []
            self.save_books()

    def save_books(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([b.to_dict() for b in self.books], f, indent=4)
            logging.info("Books saved to JSON.")
        except Exception as e:
            logging.error(f"Error saving books: {e}")

    def add_book(self, title, author, isbn):
        self.books.append(Book(title, author, isbn))
        self.save_books()
        logging.info(f"Book added: {title}")

    def search_book(self, keyword):
        return [b for b in self.books if keyword.lower() in b.title.lower() or keyword in b.isbn]

    def issue_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.issue_book():
                    self.save_books()
                    logging.info(f"Issued book: {isbn}")
                    return True
                return False
        logging.warning(f"Book not found: {isbn}")
        return None

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                if b.return_book():
                    self.save_books()
                    logging.info(f"Returned book: {isbn}")
                    return True
                return False
        logging.warning(f"Book not found: {isbn}")
        return None