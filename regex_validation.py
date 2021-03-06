import re


class UserValidation:
    def __init__(self):
        pass

    def validate_regex(self, string, regex_keys):
        """

        :param regex_keys:
        :param string:
        :return: true false
        """
        regex = {
            "phone_number": "^[+][0-9]{1,2}?[\\s,-][7-9]{1}[0-9]{9}$",
            "city": "^[A-Z]{1}[a-z]{2,}$",
            "state": "^[A-Z]{1}[a-z]{2,}$",
            "last_name": "^[A-Z]{1}[a-z]{2,}$",
            "first_name": "^[A-Z]{1}[a-z]{2,}$",
            "email": "^[0-9a-zA-Z+-._]+@[0-9a-zA-Z]+.[a-zA-Z]{2,3}.([a-zA-z]{2,3})",
            "address": "^[A-Z]{1}[a-z]{2,}$",
            "zip_code": '^[0-9]{3}?[\\s,-]{0,1}[0-9]{3,}$'
        }
        if re.search(regex.get(regex_keys), string):
            return True
        else:
            raise Exception("invalid regex")