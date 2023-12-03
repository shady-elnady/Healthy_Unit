from django.core.management.base import BaseCommand
from django.core.management import call_command

from Address.models.Country import Country
from Address.models.City import City


class Command(BaseCommand):
    help = "Creates initial Address Load Data"

    def handle(self, *args, **options):
        load_data = [
            "countries.json",
            "governorates.json",
            "cities.json",
        ]
        for data in load_data:
            try:
                call_command("loaddata", data)
                self.stdout.write(self.style.SUCCESS(f"Successfully {data} Load Data"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Load Data Failed from {data} , \n \t Error is: \t \t{e}"
                    )
                )
        my_countries = [
            {
                "name": "Egypt",
                "capital": 1,
            },
            {
                "name": "United Arab Emirates",
                "capital": 6,
            },
            {
                "name": "France",
                "capital": 7,
            },
        ]
        for my_country in my_countries:
            try:
                country = Country.objects.get(
                    name=my_country["name"],
                )
                country.capital = City.objects.get(id=my_country["capital"])
                country.save()
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Successfully Update Capital of {my_country['name']}"
                    )
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed Update Capital of {my_country['name']} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Successfully initial Address Load Data"))
