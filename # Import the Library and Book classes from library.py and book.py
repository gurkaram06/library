# Import the Library and Book classes from library.py and book.py
from library import Library
from book import Book

# Create a library
library = Library()

# Create some book objects and add them to the library
book1 = Book("The Catcher in the Rye", "J.D. Salinger")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
library.add_book(book1)
library.add_book(book2)

# Borrow a book from the library
borrow_result = library.borrow_book("The Catcher in the Rye")
print(borrow_result)

# Try to borrow the same book again
borrow_result = library.borrow_book("The Catcher in the Rye")
print(borrow_result)

# Return a book to the library
return_result = library.return_book("The Catcher in the Rye")
print(return_result)

# Try to return the same book again
return_result = library.return_book("The Catcher in the Rye")
print(return_result)
