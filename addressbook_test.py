import logging

from address_book_system.contacts import Contact

# logging.basicConfig(filename="addressbook.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)


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
    assert contact_obj.get_contact() == {
        "first_name": "Ten",
        "last_name": "Duk",
        "phone_number": "+91 7657657656",
        "address": "Ejipura",
        "city": "Bangalore",
        "state": "Karnataka",
        "zip_code": "654-654",
        "email": "dhugkar@gmail.com"
    }


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
