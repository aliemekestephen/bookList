"""
Concerned with storing and retrieving books from a CSV file
Format of CSV file:

name,author,read\n
"""

books_file = 'books.txt'


def create_book_table():
    with open(books_file, 'a') as file:
        pass  # just to make sure the file is there


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f'{name},{author},0\n')  # using 0 for false


def get_all_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]   # gives [[name, author, read],[[name, author, read]]

    # [[name, author, read], [[name, author, read]]
    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


# changes the read status to true
def mark_book_as_read(name, author):
    books = get_all_books()
    for book in books:
        if book['name'] == name and book['author'] == author:
            book['read'] = '1'
            _save_all_books(books)
            print(f'Book changed to read')


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]   # using list comprehension
    _save_all_books(books)
