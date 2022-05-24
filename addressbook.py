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
                choice = int(input("1.Add 2.Update 3.Delete 4.Display 5.Sort first name 6.Exit"))
                address_book_opt = {
                    1: self.add_contact_detail,
                    2: self.update_contact_input,
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

            except Exception as e:
                logger.error(e)
                print("Data has not enter in addressbook")
        return self.contact_dict

    def sort_by_name(self, data):
        """

        :param data: contacts
        :return: sorted contacts name
        """
        sorted_data = sorted(data.keys())
        print(sorted_data)
        return sorted(sorted_data)

    def display(self):
        """
        printing addressbook data in console
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
            contact.first_name = input("First name: ")
            contact.last_name = input("Last name: ")
            contact.phone_number = input("Phone number: ")
            contact.email = input("Email: ")
            contact.city = input("City: ")
            contact.state = input("State: ")
            contact.zip_code = input("Zip Code: ")
            contact.address = input("Address: ")
            self.set_contact_dict(contact.first_name, contact)

        except Exception as e:
            logger.error("e")
            print(e)

    def set_contact_dict(self, key, contact):
        self.contact_dict.update({key: contact})

    def get_contact_dict(self):
        return self.contact_dict

    def update_contact_input(self):
        first_name = input("Enter first name you want to update")
        input_opt = int(input("1.first_name 2.last_name 3.email 4.zip_code 5.phone_number 6.address 7.city 8.state"))
        update_data = input("Enter update data ")
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

        self.get_contact_dict().pop(contact.first_name)

        if opt in update_opt:
            update_opt.get(opt)(update_data)

        self.set_contact_dict(contact.first_name, contact)
        print('update successfully')

    def remove(self):
        remove_key = input("Enter first name you want to delete")
        self.contact_dict.pop(remove_key)


