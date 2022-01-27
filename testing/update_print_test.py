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
# print(f"before update : {address_book_obj.get_contact_dict()}")
address_book_obj.update_contact("Methok", "address", data)
mdata = address_book_obj.get_contact_dict()
# print(f"After update: {address_book_obj.get_contact_dict()}")
n_data = {
    "Ten": data,
    "methok": mdata
}
# ndata={data,mdata}
address_book_obj.sort_by(data)
# print(n_data.copy())
