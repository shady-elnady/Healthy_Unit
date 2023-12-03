from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand

from Service.models import Service, ParentService, ServiceRecord


class Command(BaseCommand):
    help = "Service Parent Load Data"

    def handle(self, *args, **options):
        data = [
            {
                "name": "Analysis",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Analysis",
                    "عربي": "تحاليل طبيه",
                    "Française": "Analyse",
                },
            },
            {
                "name": "Radiology",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Radiology",
                    "عربي": "الاشعه",
                    "Française": "Radiologie",
                },
            },
            {
                "name": "Vaccination",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Vaccination",
                    "عربي": "التطعيمات",
                    "Française": "Vaccination",
                },
            },
            {
                "name": "Dental",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Dental",
                    "عربي": "عياده الاسنان",
                    "Française": "Dentaire",
                },
            },
            {
                "name": "Ophthalmology",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Ophthalmology",
                    "عربي": "عياده الرمد",
                    "Française": "Clinique d'Ophtalmologie",
                },
            },
            {
                "name": "Internal Medicine Clinic",
                "managing_director": 1,
                "image": "",
                "translations": {
                    "English": "Internal Medicine Clinic",
                    "عربي": "عياده الباطنيه",
                    "Française": "Clinique de médecine interne",
                },
            },
        ]

        for element in data:
            try:
                ParentService.objects.create(
                    name=element["name"],
                    # managing_director=element["managing_director"],
                    image=element["image"],
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
                        f"Failed Create Parent Service > {element} \n \t The Error is: \n \t \t{e}"
                    )
                )
