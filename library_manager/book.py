class Book:
    def __init__(self, title, author, isbn, status="available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status

    def issue_book(self):
        if self.status == "available":
            self.status = "issued"
            return True
        return False

    def return_book(self):
        if self.status == "issued":
            self.status = "available"
            return True
        return False

    def __str__(self):
        return f"{self.title} | {self.author} | {self.isbn} | {self.status}"
    #json mathods
    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "status": self.status
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            data.get("title", ""),
            data.get("author", ""),
            data.get("isbn",""),
            data.get("status","available")
        )