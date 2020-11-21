"""
Concerned with storing and retrieving books from a list
"""

books = []


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})


def get_all_books():
    return books

# changes the read status to true
def mark_book_as_read(name, author):
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = True
    else:
        print(f"{name} cannot be found.")


def delete_book(name):
    global books     # tells you that global 'books' is used locally in this function
    books = [book for book in books if book['name'] != name]   # using list comprehension

# def delete_book(name):
#    for book in books:
#        if book['name'] == name:
#            books.remove(book)
