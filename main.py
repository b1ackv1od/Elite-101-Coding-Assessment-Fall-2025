from library_books import library_books
from datetime import datetime, timedelta

#1) need basic outline/idea on what to code
#2)start with all the funtions with certain parts with diffrent fucnitons of with diffrent code
#3)put in more detail for the codes that need more work that others, and debugging will be a must!
#4) polish the code that it can function normally

#problem(1)= everything is normal aside from the fact that a bracket is a bug that i some how have no clue what to do
#problem (2)=never mind, iv mustive add something and now i have 8 errors i need to fix



# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

#self explanitory all books that are in the said shelfs sooo yipieeee (im so going to crash out ITS NOT A COCONUT)

def veiw_all(book):
    print(f"{'ID':<5}{'Title'}{'Author'}")
    print("-"*50)
for book in library_books: any
if book['quantity']>0:
    print(f"{book[id]:<5}{book['title']:<30}{book['author']}")



# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

#this part of the code is a case -insensitive reader and checker of said author and genre

def look_book(query, search_type="author"):
    if search_type.lower() not in ("author", "genra"):
        raise ValueError("search_type must be 'author' or 'genra'.")
    if not isinstance(query,str) or not query.strip():
        raise ValueError("Query must be a non-empty string.")
    
    query_lower=query.lower()
    
matches= [
    book for book in library_books
    if query_lower in book[search_type.lower()].lower()
    
    ]
return matches

# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

#the code is kinda buggy, cant really figure out whats going on with it but will fix later

def checkout(library_books ):
    if book not in library_books:
        return f"Book with ID {library_books} not found."
    book = library_books[id]

    if not book.get('available',false):
        return f{"book.get('title','unknown')}

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
