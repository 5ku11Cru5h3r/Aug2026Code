import subprocess
catalog = [
    {
        "id": 1,
        "title": "Python Programming",
        "author": "John Zelle",
        "genre": "Technical",
        "price": 650.00,
        "copies": 15
    },
    {
        "id": 2,
        "title": "Clean Code",
        "author": "Robert Martin",
        "genre": "Technical",
        "price": 950.00,
        "copies": 8
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": "Fiction",
        "price": 350.00,
        "copies": 20
    },
    {
        "id": 4,
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": "Fiction",
        "price": 450.00,
        "copies": 12
    },
    {
        "id": 5,
        "title": "Atomic Habits",
        "author": "James Clear",
        "genre": "Self Help",
        "price": 550.00,
        "copies": 10
    }]
id_counter = 5
filepath = "books.txt"


def menu():
    menu_txt = '''
    1.Add Book
    2. View Catalog
    3.Search Book
    4.Update Details
    5.Delete Book
    6.Save To File
    7.Load From File
    8.Exit'''

    print("***********DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM**********")
    print(menu_txt)
    try:
        choice = int(input("Enter the choice you want: "))
        if choice < 0 or choice > 8:
            choice = -1
        return choice
    except:
        choice = -1
# --------------------------------------------------------------------------------------


# next_id is not in use
def add_book_entry(catalog: list[dict], next_id: int) -> int:
    global id_counter
    while True:
        id_counter += 1
        current_id = id_counter
        print("Enter the book details you want to add: ")
        title = input("Title:     ").strip()
        while title == "":
            print("title can't be empty")
            title = input("Title:     ").strip()

        author = input("Author:     ").strip()
        while author == "":
            print("author can't be empty")
            author = input("Author:     ").strip()

        genre = input("Genre:     ").strip()
        while genre == "":
            print("Genere can't be empty")
            genre = input("Genre:     ").strip()

        while True:
            try:
                price = float(input("Price:     "))

                if price <= 0:
                    print("Price must be greater than 0")
                    continue
                break
            except ValueError:
                print("Price must be an Integer")

        while True:
            try:
                copies = int(input("Copies:     "))
                if copies < 0:
                    print("Copies must be greater than 0")
                    continue
                break
            except ValueError:
                print("Copies must be an integer")

        book_data = dict(id=current_id, title=title, author=author,
                         genre=genre, price=price, copies=copies)

        catalog.append(book_data)
        print(f"\nBook added successfully! Book ID: {current_id}")
        choice = input(
            "Would you like to add another book? (y/n): ").strip().lower()
        if choice != 'y':
            return current_id


def print_one_book(catalog):
    id, title, author, genere, price, copies = catalog.values()
    print(f"ID:     :{id}")
    print(f"Book Title:     :{title}")
    print(f"Author:     :{author}")
    print(f"Genre:     :{genere}")
    print(f"Price:     :{price}")
    print(f"Copies:     :{copies}")


def print_many_book(catalog):
    print("-"*98)
    print(
        f"{'ID':<5}"
        f"{'Book Title':<25}"
        f"{'Author Name':<25}"
        f"{'Genre':<15}"
        f"{'Price':<12}"
        f"{'Copies':<10}"
    )
    print("-"*98)
    for book in catalog:
        id, title, author, genre, price, copies = book.values()
        print(
            f"{id:<5}"
            f"{title:<25}"
            f"{author:<25}"
            f"{genre:<15}"
            f"{price:<12.2f}"
            f"{copies:<10}"
        )

    print("-"*98)


def render_catalog(catalog: list[dict]) -> None:
    if len(catalog) == 0:
        print("No book found in the Catalog. Please add first")
    elif len(catalog) == 1:
        print_one_book(catalog[0])
    else:
        print_many_book(catalog)

# def search_by_Id(id_counter):
#     print("Searching By Id")

# def search_by_title(name: str):
#     print("Search By name")


def query_books(catalog: list[dict], search_term: str) -> list[dict]:
    result = []

    search_item = search_term.strip()

    if search_item.isdigit():

        book_id = int(search_item)

        for book in catalog:
            if book["id"] == book_id:
                result.append(book)
        return result

    else:
        search_item = search_term.strip().lower()

        for book in catalog:
            if search_item in book["title"].lower() or search_item in book["author"].lower():
                result.append(book)
        return result


def modify_book_details(catalog: list[dict], book_id: int) -> bool:
    try:
        edit_book = [b for b in catalog if b["id"] == book_id]

        if not edit_book:
            print(f"Book with this book Id not found in catalog")
            return False
    except IndexError:
        print("Enter 2 to see the list of book")

    edit_book = edit_book[0]
    while True:
        try:
            _price = float(input("Enter the Price: "))
            if _price <= 0:
                print("price must be an Integer")
                continue
            break
        except ValueError:
            print("Price must be an number")
    while True:
        try:
            _copies = int(input("Enter the Copies: "))
            if _copies < 0:
                print("Copies must be greater than 0")
                continue
            break
        except ValueError:
            print("Value must be an Integer")

    edit_book["price"] = _price
    edit_book["copies"] = _copies
    print("Value update dSuccessfully")
    return True


def delete(catalog):
    delete_Id = int(input("Enter the Id you want to delete: "))
    del_book = [b for b in catalog if b["id"] == delete_Id]

    if not del_book:
        print("Book Not Found")
        return

    del_book = del_book[0]

    ans = input("Are you sure you want to delete the product: [y/n]")

    if ans.strip().lower() == 'y':
        catalog.remove(del_book)
        print("DELETED Successfully")
    else:
        print("Delete Cancelled")


def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
    with open(filepath, 'w') as file:
        for book in catalog:
            file.write(
                f"{book['id']}|"
                f"{book['title']}|"
                f"{book['author']}|"
                f"{book['genre']}|"
                f"{book['price']}|"
                f"{book['copies']}\n"
            )


def load_catalog_from_file(filepath: str) -> list[dict]:
    catalog = []

    try:
        with open(filepath, 'r') as file:
            for line in file:
                parts = line.strip().split('|')

                book = {
                    "id": int(parts[0]),
                    "title": parts[1],
                    "author": parts[2],
                    "genre": parts[3],
                    "price": float(parts[4]),
                    "copies": int(parts[5])
                }

                catalog.append(book)
    except FileNotFoundError:
        print("File Not Present")

    return catalog


def main():
    while True:
        # subprocess.call(["cls"], shell=True)
        choice = menu()
        match choice:
            case 1:
                add_book_entry(catalog, id_counter)
            case 2:
                render_catalog(catalog)
            case 3:
                searh_item = input(
                    "Enetr the item from which you want to search: ")
                result = query_books(catalog, searh_item)
                if len(result) == 0:
                    print("NO book found")
                else:
                    render_catalog(result)
            case 4:
                try:
                    modify_id = int(input("Enter the Id you want to modify: "))
                    modify_book_details(catalog, modify_id)
                except IndexError:
                    print("Enter 2 to see list of books")
            case 5:
                try:
                    delete(catalog)
                except IndexError:
                    print("Enter 2 to see list of books")
            case 6:
                sync_catalog_to_file(filepath, catalog)
            case 7:
                load = load_catalog_from_file(filepath)
                print(load)
            case 8:
                break
            case _:
                print("Inter the valid value in integer")

    print("BYE!")


if __name__ == '__main__':
    main()
