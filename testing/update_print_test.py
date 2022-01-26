from address_book_system.address_books import AddressBook

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
address_book_obj = AddressBook()
address_book_obj.set_contact_dict(data)
address_book_obj.update_contact("Methok", "address", data)
print(address_book_obj.get_contact_dict())