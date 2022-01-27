import logging

from address_book_system.address_books import AddressBook
from address_book_system.contacts import Contact
from address_book_system.regex_validation import UserValidation

logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Service:
    def __init__(self):
        self.user = UserValidation()
        self.contact_obj = Contact()
        self.addressbook_obj = AddressBook()

    def create_addressbook(self):
        """

        :return: addressbook_dict
        """

        logger.info("create_addressbook() is called")

        while True:
            try:
                logger.info("Enter in addressbook menu")
                choice = int(input("1.Add 2.Update 3.Delete 4.Display 5.Sort first name 6.Exit"))
                address_book_opt = {
                    1: self.add_contact_detail,
                    2: self.update_contact_detail,
                    3: self.remove_contact_details,
                    4: lambda: self.addressbook_obj.display(self.addressbook_obj.get_contact_dict()),
                    5: lambda: self.addressbook_obj.sort_by(self.addressbook_obj.get_contact_dict())
                }
                if choice == 6:
                    break
                if choice in address_book_opt:
                    address_book_opt.get(choice)()
                else:
                    print("invalid in put")

            except Exception:
                logger.error("Error in create_addressbook")
                print("Data has not enter in addressbook")
        return self.addressbook_obj.contact_dict

    def user_valid_input(self):
        """
        taking input checking valid or invalid
        :return: firstname
        """

        try:
            first_name = input("First name: ")
            if not self.user.validate_regex(first_name, "first_name"):
                return ""
            last_name = input("Last name: ")
            if not self.user.validate_regex(last_name, "last_name"):
                return ""
            phone_number = input("Phone number: ")
            if not self.user.validate_regex(phone_number, "phone_number"):
                return ""
            email = input("Email: ")
            if not self.user.validate_regex(email, "email"):
                return ""
            city = input("City: ")
            if not self.user.validate_regex(city, "city"):
                return ""
            state = input("State: ")
            if not self.user.validate_regex(state, "state"):
                return ""
            zip_code = input("Zip Code: ")
            if not self.user.validate_regex(zip_code, "zip_code"):
                return ""
            address = input("Address: ")
            if not self.user.validate_regex(address, "address"):
                return ""
            self.contact_obj.add_contact(first_name, last_name, phone_number, address, city, state, zip_code, email)
            return first_name
        except Exception as e:
            logger.error("e")
            print(e)

    def add_contact_detail(self):
        first_name = self.user_valid_input()
        if not self.addressbook_obj.search_in_dict(first_name, self.contact_obj.get_contact()):
            self.addressbook_obj.set_contact_dict(self.contact_obj.get_contact())

    def update_contact_detail(self):
        first_name = input("Enter first name you want to update")
        input_opt = int(input("Enter 1.first_name 2 last_name 3.email 4.zip "
                              "5.phone 6.address 7.city 8.state"))
        regex_opt = self.addressbook_obj.get_option(input_opt)
        update_data = input("Enter update data ")
        self.addressbook_obj.update_contact(update_data, regex_opt,
                                            self.addressbook_obj.get_contact_dict().get(first_name))

    def remove_contact_details(self):
        self.addressbook_obj.remove_contact(input("Enter first name you want to delete"))
