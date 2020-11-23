from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd to delete a book'
- 'q' to quit#

Your choice: """

# dictionary to store the user options first class function
# user_options = {
#    "a": prompt_add_book,
#    "l": list_book,
#    "r": prompt_read_book,
#    "d": delete_book
#}

def menu():  # function to select the active function to run
    database.create_book_table()
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input == 'a':  # from this point
            prompt_add_book()
        elif user_input == 'l':
            list_book()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            delete_book()  # to this point
        else:
            print("Unknown command. Please try again.")

# another way to implement the set of if statements using first class functions
        #if user_input in user_options:
            #active_function = user_options[user_input]
            #active_function()

        user_input = input(USER_CHOICE)


# def prompt_add_book()  ask for book name and author, then calls the add_book() in the database.py file
def prompt_add_book():
    name = input('Please enter name of book: ')
    author = input('Please enter the book author: ')

    database.add_book(name, author)


# def list_book()  show all the books in our list
def list_book():
    books = database.get_all_books()
    if not books:  # if the file is empty
        print(f'No books stored')
    else:
        for book in books:
            read = 'YES' if book['read'] == '1' else 'NO'
            print(f"{book['name']} by {book['author']}, read: {read}")


# def prompt_read_book()   ask for book name and change it to 'read' in our list
def prompt_read_book():
    name = input('Please enter name of book you just finished reading: ')
    author = input('Please enter author of book you just finished reading: ')

    database.mark_book_as_read(name, author)


# def prompt_delete_book()   ask for book name and remove book from list
def delete_book():
    name = input('Please enter name of book to delete: ')

    database.delete_book(name)


menu()
