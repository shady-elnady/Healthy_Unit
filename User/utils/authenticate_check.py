import re


def check_is_email(unknown: str):
    # Make a regular expression
    # for validating an Email
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"
    # pass the regular expression
    # and the string into the fullmatch() method
    if re.fullmatch(regex, str(unknown)):
        return True
    else:
        return False


def check_is_mobile(unknown: str):
    # for Mobile Number
    regex = r"^\+?1?\d{9,15}$"
    if re.fullmatch(regex, str(unknown)):
        return True
    else:
        return False


def check_is_nationalID(unknown: str):
    # for National ID
    regex = r"^\d{14}$"
    if re.fullmatch(regex, str(unknown)):
        return True
    else:
        return False
