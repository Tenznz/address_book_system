from address_book_system.address_books import AddressBook
from address_book_system.service import Service

if __name__ == "__main__":
    book_details = dict()
    service=Service()
    while True:
        book = AddressBook()
        menu_opt = int(input("1.Create 2.Display 3.Exit"))
        if menu_opt == 3:
            exit()
        book.sort_by(book_details)
        book_name = input("Addressbook name")
        if menu_opt == 1:
            if book.search_in_dict(book_name, book_details):
                print("book name already exist")
            else:
                book_details[book_name] = service.create_addressbook()

        elif menu_opt == 2:
            if book_name in book_details.keys():
                book.display(book_details[book_name])
            else:
                print("not book found")
