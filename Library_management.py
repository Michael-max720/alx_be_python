class Book:
    def __init__ (self,title,author):
        self.title = title
        self.author = author
        self._is_checked_out=False
    def check_out(self):
        if not self._is_checked_out:
             self._is_checked_out = True
             return f"{self.title}is not available"
        else:
            return f"{self.title} is available"
    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out =False
            return f"{self.title} has been returned"
        else:
            return f"{self.title} has not been returned"
    def is_available(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return f"{self.title} is availabe"
        else:
            return f"{self.title} is not available"
class library:
    def __init__ (self):
        self.book=[]
    def add_book(self,book):
        self.boook.append(book)
    def  check_out_book(self,title):
        for book in self.book:
            if book.title.lower()==title.book().lower():
                print(book.chech_out())
                return
        print(f"{title} is not found in the library"})
        def return_book(self,title):
            for book in self.book:
                if book.title.lower()==title.book().lower():
                    print(book.return_book())
                    return
            print(f"{title} is not found in the library")   
    def list_available_books(self):
        available_books=[book for book in self.book if not book._is_checked_out]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"- {book.title} by {book.author}")
        else:
            print("No books are currently available in the library.")

