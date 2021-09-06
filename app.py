from utils import database


user_choice = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your Input: '''


def prompt_add_book():
    name_book = input("Enter book name:")
    author_book = input("Who wrote the book: ")
    read = input("Have you read thos book? (Yes/No)")

    database.add_book(name_book, author_book, read)

def prompt_show_books():
    database.show_books()

def prompt_mark_read():
    book_read = input("Enter the name of the book: ")
    database.mark_read(book_read)


def prompt_delete_book():
    book_delete = input("Enter name of the book you want to delete: ")
    database.delete_book(book_delete)
        

user_options = {
    "a": prompt_add_book,
    "l": prompt_show_books,
    "r": prompt_mark_read,
    "d": prompt_delete_book
}


def menu():
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input in user_options:
            chosen_function = user_options[user_input]
            chosen_function()
        elif user_input == "q":
            database.quit()
        else:
            print(f'{user_input} is not a valid input.')
        
        user_input = input(user_choice)

    

menu()