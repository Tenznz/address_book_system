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
        self.contact_dict = {}
        self.contact_obj = Contact()

    def sort_by(self, data):
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
        user = UserValidation()
        logger.info("update_contact() is called")
        logger.info("before uppdate: {}".format(data))
        if not user.validate_regex(update_data, regex_input):
            return

        first_name = data.get("first_name")
        data.pop(regex_input)

        data[regex_input] = update_data
        self.get_contact_dict()[data.get("first_name")] = data

        if regex_input == "first_name":
            self.get_contact_dict().pop(first_name)
        logger.info(f"after update: {self.contact_dict}")

    def display(self, data):
        """
        printing dictionary data in console
        :param data: dict input
        :return:
        """
        logger.info("display() is called\ndata: {}".format(data))
        print(data)

    def remove_contact(self, first_name):
        """
        deleting contact from addressbook if found
        :return:
        """
        logger.info("remove_contact() is called")
        self.contact_dict.pop(first_name)

    def search_in_dict(self, key, data):
        """
        Checking for duplicate
        :param data: dictionary
        :param key: first name
        :return: boolean
        """
        if key in data:
            return True
        else:
            return False

    def get_option(self, input_opt):
        """
        :param input_opt: int input
        :return: String
        """
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
        return: contact_dict
        """
        logger.info("get_contact_dict() is called")
        return self.contact_dict
