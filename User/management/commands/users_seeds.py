from django.core.management.base import BaseCommand
from django.core.management import call_command

from User.models.User import User


class Command(BaseCommand):
    help = "Creates initial Users Load Data"

    def handle(self, *args, **options):
        users = [
            {
                "name": "Shady El Nady",
                "email": "shadyelnady0@gmail.com",
                "national_id": "22222222222222",
                "phone_number": "+01022222222",
                "password": "shady12345",
            },
            {
                "name": "Shady El Nady1",
                "email": "shadyelnady1@gmail.com",
                "national_id": "33333333333333",
                "phone_number": "+01022222223",
                "password": "shady12345",
            },
        ]
        for user in users:
            try:
                User.objects.create_user(
                    name=user["name"],
                    email=user["email"],
                    national_id=user["national_id"],
                    phone_number=user["phone_number"],
                    password=user["password"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully  Create User with Name > {user['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create User with Name > {user['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Successfully initial Users Load Data"))
