import logging

from address_book_system.regex_validation import UserValidation

logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Contact:
    def __init__(self):
        self.regex = UserValidation()
        self.contact = {}

    # setter
    def set_contact(self, contact):
        self.contact = contact

    # getter
    def get_contact(self):
        return self.contact

    def add_contact(self, first_name, last_name, phone_number, address, city, state, zip_code, email):
        """
        Adding to contact dict
        :return:
        """
        logger.info("user_input() input from user")

        self.contact["first_name"] = first_name
        self.contact["last_name"] = last_name
        self.contact["phone_number"] = phone_number
        self.contact["address"] = address
        self.contact["city"] = city
        self.contact["state"] = state
        self.contact["zip_code"] = zip_code
        self.contact["email"] = email
        logger.info(f"{self.contact}")

    def user_valid_input(self):

        try:
            first_name = input("First name: ")
            if not self.regex.validate_regex(first_name, "name"):
                return ""
            last_name = input("Last name: ")
            if not self.regex.validate_regex(last_name, "name"):
                return ""
            phone_number = input("Phone number: ")
            if not self.regex.validate_regex(phone_number, "phone"):
                return ""
            email = input("Email: ")
            if not self.regex.validate_regex(email, "email"):
                return ""
            city = input("City: ")
            if not self.regex.validate_regex(city, "address"):
                return ""
            state = input("State: ")
            if not self.regex.validate_regex(state, "address"):
                return ""
            zip_code = input("Zip Code: ")
            if not self.regex.validate_regex(zip_code, "zip"):
                return ""
            address = input("Address: ")
            if not self.regex.validate_regex(address, "address"):
                return ""

            self.add_contact(first_name, last_name, phone_number, address, city, state, zip_code, email)
        except Exception as e:
            logger.error("e")
            print(e)
