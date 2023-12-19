from django.core.management.base import BaseCommand
from django.core.management import call_command

from Employee.models import Employee


class Command(BaseCommand):
    help = "Creates initial Employees Load Data"

    def handle(self, *args, **options):
        employees = [
            {
                "name": "Shady El Nady4",
                "display_name": "Shady El Nady4",
                "email": "shadyelnady4@gmail.com",
                "national_id": "44444444444444",
                "phone_number": "+01022222224",
                "password": "shady12345",
                "salary": 4000,
            },
        ]
        for employee in employees:
            try:
                Employee.objects.create(
                    name=employee["name"],
                    display_name=employee["display_name"],
                    email=employee["email"],
                    national_id=employee["national_id"],
                    phone_number=employee["phone_number"],
                    password=employee["password"],
                    salary=employee["salary"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully Create Employee with Name > {employee['name']}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Employee with Name > {employee['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Successfully initial Employees Load Data"))
