"""
Management utility to create superusers.
"""
import getpass
import os
import sys

from django.contrib.auth import get_user_model
from django.contrib.auth.management import get_default_username
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from django.core.management.base import BaseCommand, CommandError
from django.db import DEFAULT_DB_ALIAS
from django.utils.functional import cached_property
from django.utils.text import capfirst


PASSWORD_FIELD = "password"


class Command(BaseCommand):
    help = "Used to create a superuser."
    requires_migrations_checks = True
    stealth_options = ("stdin",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.UserModel = get_user_model()
        self.username_field = self.UserModel._meta.get_field(
            self.UserModel.USERNAME_FIELD
        )

    def add_arguments(self, parser):
        parser.add_argument(
            "--%s" % self.UserModel.USERNAME_FIELD,
            help="Specifies the login for the superuser.",
        )
        parser.add_argument(
            "--noinput",
            "--no-input",
            action="store_false",
            dest="interactive",
            help=(
                "Tells Django to NOT prompt the user for input of any kind. "
                "You must use --%s with --noinput, along with an option for "
                "any other required field. Superusers created with --noinput will "
                "not be able to log in until they're given a valid password."
                % self.UserModel.USERNAME_FIELD
            ),
        )
        parser.add_argument(
            "--database",
            default=DEFAULT_DB_ALIAS,
            help='Specifies the database to use. Default is "default".',
        )
        for field_name in self.UserModel.REQUIRED_FIELDS:
            field = self.UserModel._meta.get_field(field_name)
            if field.many_to_many:
                if (
                    field.remote_field.through
                    and not field.remote_field.through._meta.auto_created
                ):
                    raise CommandError(
                        "Required field '%s' specifies a many-to-many "
                        "relation through model, which is not supported." % field_name
                    )
                else:
                    parser.add_argument(
                        "--%s" % field_name,
                        action="append",
                        help=(
                            "Specifies the %s for the superuser. Can be used "
                            "multiple times." % field_name,
                        ),
                    )
            else:
                parser.add_argument(
                    "--%s" % field_name,
                    help="Specifies the %s for the superuser." % field_name,
                )

    def execute(self, *args, **options):
        self.stdin = options.get("stdin", sys.stdin)  # Used for testing
        return super().execute(*args, **options)

    def handle(self, *args, **options):
        national_id = input("national_id: ")
        email = input("email: ")
        phone_number = input("phone_number: ")
        password = input("password: ")

        try:
            self.UserModel.objects.create_superUser(
                national_id=national_id,
                email=email,
                phone_number=phone_number,
                password=password,
            )
            self.stdout.write(self.style.SUCCESS("Successfully Create Super Admin"))
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(
                    f"Failed Create Super Admin >  \n \t Error is: \t \t{e}"
                )
            )
