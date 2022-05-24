import logging

from multi_addressbook import MultiAddressbook


def main():
    books = MultiAddressbook()
    while True:
        try:
            menu_opt = int(input("1.Create 2.Display 3.open 4.Delete 5.Exit"))

            menu = {
                1: books.add_addressbook,
                2: books.display_addressbook,
                3: books.update_addressbook,
                4: books.delete_addressbook,
                5: exit
            }
            menu.get(menu_opt)()
        except Exception as e:
            logging.error(e)
            print(e, "not found")


if __name__ == "__main__":
    main()
