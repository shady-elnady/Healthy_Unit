from django.core.management.base import BaseCommand

from Service.models import Service
from Analysis.models import Analysis


class Command(BaseCommand):
    help = "Analysis Load Data"

    def handle(self, *args, **options):
        data = [
            {
                "name": "Glucose",
                "symbol": "Glo",
                "min_normal": 1.5,
                "max_normal": 25.5,
                "unit": "m",
                "translations": {
                    "English": "Glucose",
                    "عربي": "الجلوكوز",
                    "Française": "Glucose",
                },
            },
            {
                "name": "Cholestrol",
                "symbol": "Cheo",
                "min_normal": 1.5,
                "max_normal": 25.5,
                "unit": "m",
                "translations": {
                    "English": "Cholestrol",
                    "عربي": "الكولسترول",
                    "Française": "Cholestérol",
                },
            },
        ]

        for element in data:
            try:
                Analysis.objects.create(
                    name=element["name"],
                    symbol=element["symbol"],
                    min_normal=element["min_normal"],
                    max_normal=element["max_normal"],
                    unit=element["unit"],
                    parent=Service.objects.get(name="Analysis"),
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
                        f"Failed Create Analysis > {element} \n \t The Error is: \n \t \t{e}"
                    )
                )
