import logging

from address_book_system.contacts import Contact
from address_book_system.regex_validation import UserValidation

logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class AddressBook:
    def __init__(self):
        self.contactlist = list()
        self.user = UserValidation()
        self.contact_obj = Contact()

    def create_addressbook(self):
        """
        Create address book
        :return:
        """
        logger.info("create_addressbook() is called")

        EXIT = 5

        try:
            while True:
                logger.info("Enter in addressbook menu")
                choice = int(input("1.Added contact 2.Update 3.Delete 4.Display 5.Exit"))
                self.contact_obj = Contact()
                if choice == 1:
                    self.contact_obj.user_valid_input()
                    self.set_contactlist()
                # elif choice == 2:
                #     address_book.update_contact(input("Enter First Name which you want edit"),
                #                                 address_book.user_input())
                # elif choice == 3:
                #     address_book.delete_contact(input("Enter first name you want to delete"))
                elif choice == 4:
                    self.display()
                elif choice == EXIT:
                    break
                else:
                    print("invalid input")

        except Exception as e:
            logger.error(e)
            print(e)

    def set_contactlist(self):
        """
        printing contact
        :return:
        """
        self.contactlist.append(self.contact_obj.get_contact().values())
        logger.info(f"All contact{self.contact_obj.get_contact().values()}")
        print(len(self.contactlist))

    def display(self):
        """
        printing contact
        :return:
        """
        print(self.contactlist)

