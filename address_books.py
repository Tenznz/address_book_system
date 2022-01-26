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
        self.contact_dict = dict()
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
                choice = int(input("1.Add 2.Update 3.Delete 4.Display 5.Exit"))
                self.contact_obj = Contact()
                if choice == 1:
                    self.contact_obj.user_valid_input()
                    self.set_contact_dict(self.contact_obj.get_contact())
                elif choice == 2:
                    first_name = input("Enter first name you want to update")
                    input_opt = int(input("Enter 1.first_name 2 last_name 3.email 4.zip "
                                          "5.phone 6.address 7.city 8.state"))
                    regex_opt = {
                        1: "first_name",
                        2: "last_name",
                        3: "email",
                        4: "zip_code",
                        5: "phone_number",
                        6: "address",
                        7: "city",
                        8: "state"
                    }
                    if input_opt not in regex_opt:
                        print("invalid input")
                    else:
                        update_data = input("Enter update data ")
                        self.update_contact(update_data, regex_opt[input_opt],
                                            self.contact_dict.get(first_name))
                elif choice == 3:
                    self.remove_contact(input("Enter first name you want to delete"))
                elif choice == 4:
                    self.display()
                elif choice == EXIT:
                    break
                else:
                    print("invalid input")

        except Exception as e:
            logger.error(e.with_traceback())

    def update_contact(self, update_data, regex_input, data):
        """
        update contact
        :param update_data: contact input
        :param regex_input:
        :param data: contact detail in dict
        :return:
        """
        if not self.user.validate_regex(update_data, regex_input):
            return

        first_name = data.get("first_name")
        data.pop(regex_input)
        data[regex_input] = update_data
        self.contact_dict[data.get("first_name")] = data
        if regex_input == "first_name":
            self.contact_dict.pop(first_name)
        logger.info(f"{self.contact_dict}")

    # setter
    def set_contact_dict(self, data):
        """
        :return:
        """
        self.contact_dict[data["first_name"]] = data
        logger.info(f"All contact{data.values()}")

    # getter
    def get_contact_dict(self):
        """

        :return: contact_dict
        """
        return self.contact_dict

    def display(self):
        """
        printing contact
        :return:
        """
        print(self.contact_dict)

    def remove_contact(self, first_name):
        """
        deleting contact from addressbook if found
        :return: true or false
        """
        logger.info("remove_contact() is called")
        self.contact_dict.pop(first_name)
