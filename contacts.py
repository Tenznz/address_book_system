import logging


logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Contact:
    def __init__(self):
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
