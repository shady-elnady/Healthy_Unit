from django.utils.translation import gettext_lazy as _


class Messages:
    # Phone Nmuber
    PHONE_INVALID_VALIDATION = _(
        "Invalid Phone Number,it must not consist of space and requires country code. eg : +2 01012345678."
    )
    PHONE_UNIQUE_VALIDATION = _("Phone Number must Unique")
    # E-Mail
    EMAIL_INVALID_VALIDATION = _("Invalid E-Mail")
    EMAIL_UNIQUE_VALIDATION = _("Phone Number must Unique")
    EMAIL_NOT_VERIFIED = _("E-mail is not verified.")
    # Display Name
    DISPLAY_NAME_UNIQUE_VALIDATION = _("Display Name must be unique")
    # Name
    NAME_INVALID_VALIDATION = _("Invalid Name , it must conatin 4 Names of parents")
    NAME_UNIQUE_VALIDATION = _("Name must be unique")
    # Password
    PASSWORD_INVALID_VALIDATION = _(
        "Invalid Password, it must contain one or more Upper Case Char, one or more Lower Case Char, one or more from [@, $ ,!, %, *, ?, &]; between 8 to 32 Chars"
    )
    # National ID
    NATIONAL_ID_INVALID_VALIDATION = _(
        "Invalid National ID, it must be 14 Numbers. eg : 11111111111111"
    )
    NATIONAL_ID_UNIQUE_VALIDATION = _("National ID must Unique")
    # User
    USER_NOT_VERIFIED = _("User Account is Not Verified.")
    USER_DISABLED = _("User Account is disabled.")
    USER_NOT_ACTIVATE = _("User Account is Not Activate.")
    USER_NOT_FOUND = _("User Account is Not Found.")
