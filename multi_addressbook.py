from address_book_system.addressbook import AddressBook


class MultiAddressbook:

    def __init__(self):
        self.book_details = dict()

    def add_addressbook(self):
        addressbook = AddressBook()
        book_name = input("Addressbook name")
        if book_name in self.book_details:
            print("book name already exist")
        else:
            self.book_details.update({book_name: addressbook.create_addressbook()})

    def delete_addressbook(self):
        key = input("Delete_name")
        self.book_details.pop(key)
        print('delete successfully')

    def display_addressbook(self):
        print([book for book in self.book_details])
        address_book_name = input('Enter update addressbook')
        data = self.book_details.get(address_book_name)
        print([contact.__str__() for name, contact in data.items()])

    def update_addressbook(self):
        addressbook = AddressBook()
        address_book_name = input('Enter addressbook name')
        data = self.book_details.get(address_book_name)
        for key, value in data.items():
            addressbook.set_contact_dict(key, value)
        new_contacts = addressbook.create_addressbook()
        self.book_details.update({address_book_name:new_contacts})
