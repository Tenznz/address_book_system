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

        :return: addressbook_dict
        """

        logger.info("create_addressbook() is called")

        EXIT = 6

        while True:
            try:
                logger.info("Enter in addressbook menu")
                choice = int(input("1.Add 2.Update 3.Delete 4.Display 5.Sort first name 6.Exit"))
                self.contact_obj = Contact()
                if choice == 1:
                    first_name = self.contact_obj.user_valid_input()
                    if not self.search_in_dict(first_name, self.contact_obj.get_contact()):
                        self.set_contact_dict(self.contact_obj.get_contact())
                elif choice == 2:
                    first_name = input("Enter first name you want to update")
                    regex_opt = self.get_option()
                    update_data = input("Enter update data ")
                    self.update_contact(update_data, regex_opt,
                                        self.contact_dict.get(first_name))
                elif choice == 3:
                    self.remove_contact(input("Enter first name you want to delete"))
                elif choice == 4:
                    self.display(self.get_contact_dict())
                elif choice == 5:
                    # sort_opt = self.get_option()
                    contact = self.get_contact_dict()
                    # self.sort_by(sort_opt, contact)
                    self.sort_by(contact)
                elif choice == EXIT:
                    break
                else:
                    print("invalid input")

            except Exception:
                logger.error("Error in create_addressbook")
                print("Data has not enter in addressbook")
        return self.contact_dict

    # def sort_by(self, sort_opt, data):
    def sort_by(self, data):
        # for i in len(data.keys()):
        #     for j in len(data.keys()):
        #         temp = data[sort_opt]
        #     data[sort_opt] > temp
        #     print(data[sort_opt])
        sorted_data = sorted(data.keys())
        print(sorted_data)
        return sorted_data

    def update_contact(self, update_data, regex_input, data):
        """
        update contact
        :param update_data: contact input
        :param regex_input:
        :param data: contact detail in dict
        :return:
        """
        logger.info("update_contact() is called")
        logger.info("before uppdate: {}".format(data))
        if not self.user.validate_regex(update_data, regex_input):
            return

        first_name = data.get("first_name")
        data.pop(regex_input)

        data[regex_input] = update_data
        self.contact_dict[data.get("first_name")] = data

        if regex_input == "first_name":
            self.contact_dict.pop(first_name)
        logger.info(f"after update: {self.contact_dict}")

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
        logger.info("get_contact_dict() is called")
        return self.contact_dict

    def display(self, data):
        """
        printing contact
        :return:
        """
        logger.info("display() is called\ndata: {}".format(data))
        print(data)

    def remove_contact(self, first_name):
        """
        deleting contact from addressbook if found
        :return: true or false
        """
        logger.info("remove_contact() is called")
        self.contact_dict.pop(first_name)

    def search_in_dict(self, key, data):
        """
        Checking for duplicate
        :param data:
        :param key:
        :return:
        """
        if key in data:
            return True
        else:
            return False

    def get_option(self):
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
        return regex_opt[input_opt]
