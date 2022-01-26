from address_book_system.regex_validation import UserValidation


def test_regex_name():
    check = UserValidation()
    assert check.validate_regex("Tenzing", "name")


def test_regex_zip():
    check = UserValidation()
    assert check.validate_regex("123-234", "zip")


def test_regex_email():
    check = UserValidation()
    assert check.validate_regex("dhugkar@gmail.com", "email")


def test_regex_address():
    check = UserValidation()
    assert check.validate_regex("Banglore", "address")


def test_regex_phone():
    check = UserValidation()
    assert check.validate_regex("+91 9564564565", "phone")
