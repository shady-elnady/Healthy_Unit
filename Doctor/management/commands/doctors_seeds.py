from django.core.management.base import BaseCommand
from django.core.management import call_command

from Utils.models.Choices import MEDICAL_SPECIALTIES
from Doctor.models import Doctor


class Command(BaseCommand):
    help = "Creates initial Doctors Load Data"

    def handle(self, *args, **options):
        doctors = [
            {
                "name": "Ahmed",
                "display_name": "Ahmed",
                "email": "ahmedshadyelnady@gmail.com",
                "national_id": "55555555555555",
                "phone_number": "+01022222225",
                "password": "Shady@12345",
                "salary": 5000,
                "medical_specialty": MEDICAL_SPECIALTIES.NEPHROLOGY,
            },
        ]
        for doctor in doctors:
            try:
                Doctor.objects.create(
                    name=doctor["name"],
                    display_name=doctor["display_name"],
                    email=doctor["email"],
                    national_id=doctor["national_id"],
                    phone_number=doctor["phone_number"],
                    password=doctor["password"],
                    salary=doctor["salary"],
                    medical_specialty=doctor["medical_specialty"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully Create Doctor with Name > {doctor['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Doctor with Name > {doctor['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Successfully initial Doctors Load Data"))
