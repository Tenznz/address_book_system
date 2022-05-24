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
        self._first_name = ""
        self._last_name = ""
        self._phone_number = ""
        self._address = ""
        self._email = ""
        self._city = ""
        self._state = ""
        self._zip_code = ""

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if self.user.validate_regex(first_name, "first_name"):
            self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if self.user.validate_regex(last_name, "last_name"):
            self._last_name = last_name

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        if self.user.validate_regex(phone_number, "phone_number"):
            self._phone_number = phone_number

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        if self.user.validate_regex(address, "address"):
            self._address = address

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if self.user.validate_regex(email, "email"):
            self._email = email

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        if self.user.validate_regex(state, "state"):
            self._state = state

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, city):
        if self.user.validate_regex(city, "city"):
            self._city = city

    @property
    def zip_code(self):
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        if self.user.validate_regex(zip_code, "zip_code"):
            self._zip_code = zip_code

    def set_email(self, email):
        if self.user.validate_regex(email, "email"):
            self._email = email

    def set_address(self, address):
        if self.user.validate_regex(address, "address"):
            self._address = address

    def set_phone_number(self, phone_number):
        if self.user.validate_regex(phone_number, "phone_number"):
            self._phone_number = phone_number

    def set_last_name(self, last_name):
        if self.user.validate_regex(last_name, "last_name"):
            self._last_name = last_name

    def set_first_name(self, first_name):
        if self.user.validate_regex(first_name, "first_name"):
            self._first_name = first_name

    def set_zip_code(self, zip_code):
        if self.user.validate_regex(zip_code, "zip_code"):
            self._zip_code = zip_code

    def set_city(self, city):
        if self.user.validate_regex(city, "city"):
            self._city = city

    def set_state(self, state):
        if self.user.validate_regex(state, "state"):
            self._state = state

    def __str__(self):
        return "first name: " + self._first_name, "last name: " + self._last_name, "phone number: " \
               + self._phone_number, "address: " + self._address, "city: " + self._city, "state: " \
               + self._state, "zip: " + self._zip_code, "email: " + self._email
