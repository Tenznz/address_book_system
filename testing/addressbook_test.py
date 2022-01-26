from address_book_system.address_books import AddressBook
from address_book_system.contacts import Contact

# logging.basicConfig(filename="addressbook.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)

data = {
    "first_name": "Ten",
    "last_name": "Duk",
    "phone_number": "+91 7657657656",
    "address": "Ejipura",
    "city": "Bangalore",
    "state": "Karnataka",
    "zip_code": "654-654",
    "email": "dhugkar@gmail.com"
}
update_data = {
    "first_name": "Ten",
    "last_name": "Duk",
    "phone_number": "+91 7657657656",
    "address": "Methok",
    "city": "Bangalore",
    "state": "Karnataka",
    "zip_code": "654-654",
    "email": "dhugkar@gmail.com"
}


def test_add_contact():
    """
    testing add contact correctly
    :return:
    """
    contact_obj = Contact()
    contact_obj.add_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    assert contact_obj.get_contact()["first_name"] == "Ten"
    assert contact_obj.get_contact()["phone_number"] == "+91 7657657656"
    assert contact_obj.get_contact() == data


def test_fail_add_contact():
    contact_obj = Contact()
    contact_obj.add_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    # assert contact_obj.get_contact()["first_name"] == "Ten"
    # assert contact_obj.get_contact()["phone_number"] == "+91 7657657656"
    assert not contact_obj.get_contact() == {
        "first_name": "Tn",
        "last_name": "Duk",
        "phone_number": "+91 7657657656",
        "address": "Ejipura",
        "city": "Bangalore",
        "state": "Karnataka",
        "zip_code": "654-654",
        "email": "dhugkar@gmail.com"
    }


def test_set_contact():
    address_book_obj = AddressBook()
    # before = len(address_book_obj.get_contact_dict())
    address_book_obj.set_contact_dict(data)
    # after = len(address_book_obj.get_contact_dict())
    assert address_book_obj.get_contact_dict()["Ten"] == data


def test_remove_contact():
    address_book_obj = AddressBook()
    address_book_obj.set_contact_dict(data)
    assert len(address_book_obj.get_contact_dict()) == 1
    address_book_obj.remove_contact("Ten")
    assert len(address_book_obj.get_contact_dict()) == 0


def test_update_contact():
    address_book_obj = AddressBook()
    address_book_obj.set_contact_dict(data)
    address_book_obj.update_contact("Methok", "address", data)
    assert address_book_obj.get_contact_dict() == {"Ten": update_data}

    # def test_update_contact():
#
#     address_book_obj = AddressBook()
#
#     address_book_obj.set_contact_dict(data)
#     address_book_obj.update_contact("Methok", "first_name", data)
#     assert
