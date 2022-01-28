from address_book_system.addressbook import AddressBook
from address_book_system.contacts import Contact


def test_add_contact():
    contact_obj = Contact()
    contact_obj.set_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    assert contact_obj.get_first_name() == "Ten"


def test_set_contact():
    address_book_obj = AddressBook()
    contact_obj = Contact()
    contact_obj.set_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    before = len(address_book_obj.get_contact_dict())
    address_book_obj.set_contact_dict("Ten", contact_obj)
    after = len(address_book_obj.get_contact_dict())
    assert before != after


def test_remove_contact():
    address_book_obj = AddressBook()
    contact_obj = Contact()
    contact_obj.set_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    address_book_obj.set_contact_dict("Ten", contact_obj)
    assert len(address_book_obj.get_contact_dict()) == 1
    address_book_obj.remove_contact_details("Ten")
    assert len(address_book_obj.get_contact_dict()) == 0


def test_update_contact():
    address_book_obj = AddressBook()
    contact_obj = Contact()
    contact_obj.set_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")

    address_book_obj.set_contact_dict("Ten", contact_obj)
    # 1.first_name 2.last_name 3.email 4.zip_code 5.phone_number 6.address 7.city 8.state"
    address_book_obj.update_contact("Methok", 1, contact_obj)
    assert contact_obj.get_first_name() == "Methok"


def test_sort_by():
    address_book_obj = AddressBook()
    contact_obj = Contact()
    contact_obj.set_contact("Ten", "Duk", "+91 7657657656", "Ejipura", "Bangalore", "Karnataka", "654-654",
                            "dhugkar@gmail.com")
    address_book_obj.set_contact_dict("Ten", contact_obj)
    contact_obj.set_contact("Methok", "Lass", "+91 9657657656", "Loaa", "Bangalore", "Karnataka", "624-354",
                            "mwthok@gmail.com")

    address_book_obj.set_contact_dict("Methok", contact_obj)
    sorted_data = address_book_obj.sort_by_name(address_book_obj.get_contact_dict())
    expected = ['Methok', 'Ten']
    assert sorted_data == expected
