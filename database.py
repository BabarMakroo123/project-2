import json

with open(r"C:\Users\Owais Mohammad\PythonProjects\Milestone Project 2\utils\data.json", "r") as f:
    books = json.load(f)


def add_to_file(data):
    with open(r"C:\Users\Owais Mohammad\PythonProjects\Milestone Project 2\utils\data.json", "w") as f1:
        json.dump(data, f1, indent = 2)


def add_book(name, author, read):
    global read_book
    if read == "Yes":
        read_book = True
    elif read == "No":
        read_book = False
    else:
        print(f"{read} is not a valid input. Please Startover.")

    books.append(
        {
            "name": name, "author": author, "read": read_book
        }
    )
    
    add_to_file(books)


def show_books():
    for book in books:
        print(f"{book['name']}")


def mark_read(book_read):
    if book_read in [book["name"] for book in books]:
        for book in books:
            if book["name"] == book_read:
                book["read"] = True
            elif book_read != book:
                continue
    else:
        print(f"{book_read} is not in your library.")
    

    add_to_file(books)
    

def delete_book(book_delete):
    global books

    if book_delete in [book["name"] for book in books]:
        books = [book for book in books if book["name"] != book_delete]
    else:
        print(f"{book_delete} is not in your library.")


    add_to_file(books)

def quit():
    exit()