import logging

from address_book_system.contacts import Contact

logging.basicConfig(filename="addressbook.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class AddressBook:
    def __init__(self):
        self.contact_dict = dict()

    def create_addressbook(self):
        """

        :return: contact_dict
        """
        logger.info("create_addressbook() is called")

        while True:
            try:
                logger.info("Enter in addressbook menu")
                choice = self.menu_opt()
                address_book_opt = {
                    1: self.add_contact_detail,
                    2: self.update_contact_detail,
                    3: self.remove,
                    4: self.display,
                    5: lambda: self.sort_by_name(self.contact_dict)
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
        return self.contact_dict

    def menu_opt(self):
        return int(input("1.Add 2.Update 3.Delete 4.Display 5.Sort first name 6.Exit"))

    def input_opt(self):
        return int(input("1.first_name 2.last_name 3.email 4.zip_code 5.phone_number 6.address 7.city 8.state"))

    # def sort_by(self):
    #     opt = self.menu_opt()
    #     contact = self.get_contact_dict().values()
    #     get_opt = {
    #         1: contact.get_first_name,
    #         2: contact.get_last_name,
    #         3: contact.get_email,
    #         4: contact.get_zip_code,
    #         5: contact.get_phone_number,
    #         6: contact.get_address,
    #         7: contact.get_city,
    #         8: contact.get_state
    #     }
    #     sort_data = get_opt.get(opt)()
    def sort_by_name(self, data):
        sorted_data = sorted(data.keys())
        print(sorted_data)
        return sorted(sorted_data)

    def duplicate(self, key, data):
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

    def display(self):
        """
        printing dictionary data in console
        :param data: dict input
        :return:
        """
        if bool(self.contact_dict):
            print("Address Book is")
            for values in self.contact_dict.values():
                print(values.__str__())

    def add_contact_detail(self):
        """
        taking input checking valid or invalid
        :return: firstname
        """
        contact = Contact()
        try:
            first_name = input("First name: ")
            contact.set_first_name(first_name)
            last_name = input("Last name: ")
            contact.set_last_name(last_name)
            phone_number = input("Phone number: ")
            contact.set_phone_number(phone_number)
            email = input("Email: ")
            contact.set_email(email)
            city = input("City: ")
            contact.set_city(city)
            state = input("State: ")
            contact.set_state(state)
            zip_code = input("Zip Code: ")
            contact.set_zip_code(zip_code)
            address = input("Address: ")
            contact.set_address(address)
            self.set_contact_dict(first_name, contact)

        except Exception as e:
            logger.error("e")
            print(e)

    def set_contact_dict(self, key, contact):
        self.contact_dict[key] = contact

    def get_contact_dict(self):
        return self.contact_dict

    def update_contact_detail(self):
        first_name = input("Enter first name you want to update")
        update_data = input("Enter update data ")
        input_opt = self.input_opt()
        self.update_contact(update_data, input_opt,
                            self.contact_dict[first_name])

    def update_contact(self, update_data, opt, contact):
        """
        update contact
        :param contact: contact object
        :param update_data: contact input
        :param opt:
        :return:
        """
        logger.info("update_contact() is called")
        logger.info("before update: {}".format(contact.__str__()))
        update_opt = {
            1: contact.set_first_name,
            2: contact.set_last_name,
            3: contact.set_email,
            4: contact.set_zip_code,
            5: contact.set_phone_number,
            6: contact.set_address,
            7: contact.set_city,
            8: contact.set_state
        }
        self.get_contact_dict().pop(contact.get_first_name())
        if opt in update_opt:
            update_opt.get(opt)(update_data)
        self.set_contact_dict(contact.get_first_name(), contact)
        logger.info("after update: {}".format(contact.__str__()))

    def remove(self):
        remove_key = input("Enter first name you want to delete")
        self.remove_contact_details(remove_key)

    def remove_contact_details(self, key):
        self.contact_dict.pop(key)

    def search(self, data):
        print(data.keys())
        print(data.__str__())
