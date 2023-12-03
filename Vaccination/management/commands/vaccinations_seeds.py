from django.core.management.base import BaseCommand

from Service.models import Service
from Vaccination.models import Vaccination


class Command(BaseCommand):
    help = "Vaccination Load Data"

    def handle(self, *args, **options):
        data = [
            {
                "name": "Virus B",
                "translations": {
                    "English": "Virus B",
                    "عربي": "فيرس بى",
                    "Française": "Virus B",
                },
            }
        ]

        for element in data:
            try:
                Vaccination.objects.create(
                    name=element["name"],
                    parent=Service.objects.get(name="Vaccination"),
                    translations=element["translations"],
                )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully Create Service >> {element['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Create Vaccination > {element} \n The Error is: \n \t{e}"
                    )
                )
