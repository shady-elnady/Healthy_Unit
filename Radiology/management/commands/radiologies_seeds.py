from django.core.management.base import BaseCommand

from Service.models import Service
from Radiology.models import Radiology


class Command(BaseCommand):
    help = "Radiology Load Data"

    def handle(self, *args, **options):
        data = [
            {
                "name": "X-ray",
                "translations": {
                    "English": "X-ray",
                    "عربي": "أشعه أكس",
                    "Française": "Dollar",
                },
            }
        ]

        for element in data:
            try:
                Radiology.objects.create(
                    name=element["name"],
                    parent=Service.objects.get(name="Radiology"),
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
                        f"Failed Create Radiology > {element} \n The Error is: \n \t{e}"
                    )
                )
