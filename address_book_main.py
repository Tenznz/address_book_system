import logging

from address_book_system.addressbook import AddressBook

if __name__ == "__main__":
    book_details = dict()

    while True:
        try:
            addressbook = AddressBook()
            menu_opt = int(input("1.Create 2.Display 3.Delete 4.Exit"))
            if menu_opt == 4:
                exit()

            if menu_opt == 1:
                book_name = input("Addressbook name")
                if addressbook.duplicate(book_name, book_details):
                    print("book name already exist")
                else:
                    book_details[book_name] = addressbook.create_addressbook()

            elif menu_opt == 2:
                print(book_details.keys())
                book_name = input("Addressbook name")
                if book_name in book_details.keys():
                    print(book_details[book_name].keys())
                else:
                    print("not book found")
            elif menu_opt == 3:
                book_details.pop(input("Enter Delete Book name"))
        except Exception as e:
            logging.error(e)
            print(e, "not found")
