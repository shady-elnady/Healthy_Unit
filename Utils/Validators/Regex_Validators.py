import re
from django.core.validators import EmailValidator, RegexValidator
from django.utils.translation import gettext_lazy as _

from Utils.Assets.messages import Messages


class RegexValidators:
    """
    Class to hold regexes for User models in userapp.
    """

    # 'john.doe@email.com'
    EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    EMAIL_OTHER_REGEX = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b"

    # 'john.doe@email.com'
    NAME_REGEX = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

    ## prithoo: Full ISO Spec 10 to 12 digit phone number (+(ISD)(STD)(AREA)(SUBSCRIBER)):
    ##  8811098879, 881-109-8879, +918811098879, +91-881-109-8879, +91-361-222-0324, +913612220324
    ## confirmed on 'https://regex101.com/'
    PHONE_REGEX_ISD = re.compile(
        r"^(\+[0-9]{0,2})?([\s.-])?(\+\d{1,2}\s)?\(?\d{3}\)?([\s.-])?\d{3}([\s.-])?\d{4}$"
    )
    ## Normal 10-digit phone number ((STD)(AREA)(SUBSCRIBER))
    PHONE_REGEX = re.compile(
        r"^([\s.-])?(\+\d{1,2}\s)?\(?\d{3}\)?([\s.-])?\d{3}([\s.-])?\d{4}$"
    )
    ## Example phone number (+201061656112)
    MY_PHONE_REGEX = re.compile(
        r"^\+?1?\d{9,15}$",
    )
    ##
    NATIONAL_ID_REGEX = re.compile(
        r"^\d{14}$",
    )

    # >=1 UC char, >=1 LC char, >=1 NUM char >=[@, $ ,!, %, *, ?, &]; between 8 to 32 chars; confirmed on 'https://regex101.com/'
    PASSWORD_REGEX = re.compile(
        r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,32}$"
    )

    @staticmethod
    def phone_number_regex(cls) -> "RegexValidator":
        return RegexValidator(
            regex=cls.MY_PHONE_REGEX,
            message=Messages.PHONE_INVALID_VALIDATION,
            code="400",
        )

    @staticmethod
    def name_regex(cls) -> "RegexValidator":
        return RegexValidator(
            regex=cls.NAME_REGEX,
            message=Messages.NAME_INVALID_VALIDATION,
            code="400",
        )

    @staticmethod
    def password_regex(cls) -> "RegexValidator":
        return RegexValidator(
            regex=cls.PASSWORD_REGEX,
            message=Messages.PASSWORD_INVALID_VALIDATION,
            code="400",
        )

    @staticmethod
    def national_id_regex(cls) -> "RegexValidator":
        return RegexValidator(
            regex=cls.NATIONAL_ID_REGEX,
            message=Messages.NATIONAL_ID_INVALID_VALIDATION,
            code="400",
        )

    @staticmethod
    def email_regex(cls) -> "EmailValidator":
        return (
            EmailValidator(
                message=Messages.EMAIL_INVALID_VALIDATION,
                code="400",
            ),
        )

    @staticmethod
    def check_is_email(cls, unknown: str) -> bool:
        # for E-Mail
        if cls.EMAIL_REGEX.fullmatch(unknown):
            return True
        else:
            return False

    @staticmethod
    def check_is_mobile(cls, unknown: str) -> bool:
        # for Mobile Number
        if cls.MY_PHONE_REGEX.fullmatch(unknown):
            return True
        else:
            return False

    @staticmethod
    def check_is_nationalID(cls, unknown: str) -> bool:
        # for National ID
        if cls.MY_PHONE_REGEX.fullmatch(unknown):
            return True
        else:
            return False
