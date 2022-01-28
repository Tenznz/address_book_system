import logging

from address_book_system.regex_validation import UserValidation

logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Contact:
    def __init__(self):
        self.user = UserValidation()
        self.first_name = ""
        self.last_name = ""
        self.phone_number = ""
        self.address = ""
        self.email = ""
        self.city = ""
        self.state = ""
        self.zip_code = ""

    def get_first_name(self):
        return self.first_name

    def set_first_name(self, first_name):
        if self.user.validate_regex(first_name, "first_name"):
            self.first_name = first_name

    def get_last_name(self):
        return self.last_name

    def set_last_name(self, last_name):
        if self.user.validate_regex(last_name, "last_name"):
            self.last_name = last_name

    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        if self.user.validate_regex(phone_number, "phone_number"):
            self.phone_number = phone_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        if self.user.validate_regex(address, "address"):
            self.address = address

    def get_email(self):
        return self.email

    def set_email(self, email):
        if self.user.validate_regex(email, "email"):
            self.email = email

    def get_state(self):
        return self.state

    def set_state(self, state):
        if self.user.validate_regex(state, "state"):
            self.state = state

    def get_city(self):
        return self.city

    def set_city(self, city):
        if self.user.validate_regex(city, "city"):
            self.city = city

    def get_zip_code(self):
        return self.zip_code

    def set_zip_code(self, zip_code):
        if self.user.validate_regex(zip_code, "zip_code"):
            self.zip_code = zip_code

    def set_contact(self, first_name, last_name, phone_number, address, city, state, zip_code, email):
        self.set_first_name(first_name)
        self.set_last_name(last_name)
        self.set_phone_number(phone_number)
        self.set_email(email)
        self.set_city(city)
        self.set_state(state)
        self.set_zip_code(zip_code)
        self.set_address(address)

    def __str__(self):
        return "first name: " + self.first_name, "last name: " + self.last_name, "phone number: " \
               + self.phone_number, "address: " + self.address, "city: " + self.city, "state: " \
               + self.state, "zip: " + self.zip_code, "email: " + self.email
