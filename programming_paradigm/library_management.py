class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False
        
    def check_book_out(self):
        # Returns True if successful, False if already checked out.
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False
        
    def return_book(self):
        # Returns True if successful, False if it was not checked out.
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False
        
class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book: Book):
        self._books.append(book)
        
    def check_out_book(self, title):
        # Returns True if checkout succeeds, False otherwise.
        for book in self._books:
            if book.title == title:
                return book.check_book_out()
        return False
        
    def return_book(self, title):
        # Returns True if return succeeds, False otherwise.
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False
        
    def list_available_books(self):
        for book in self._books:
            # Check if this book is not checked out
            if not book._is_checked_out:
                print (f"{book.title} by {book.author}")
