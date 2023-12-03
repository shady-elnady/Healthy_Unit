from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.conf import settings


class Command(BaseCommand):
    help = "Creates initial models"

    def handle(self, *args, **options):
        works = [
            "makemigrations",
            "migrate",
            "collectstatic",
        ]
        for work in works:
            try:
                call_command(work)
                self.stdout.write(self.style.SUCCESS(f"Successfully {work}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{work} Failed  \n \t \t Error is: {e}")
                )

        ##
        load_data = [
            "languages.json",
            "currencies.json",
            # "categories.json",
        ]
        for data in load_data:
            try:
                call_command("loaddata", data)
                self.stdout.write(self.style.SUCCESS(f"Successfully {data} Load Data"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Load Data Failed from {data} , \n \t Error is: \n \t \t{e}"
                    )
                )
        ##
        works = [
            "address_seeds",
            "parent_services_seeds",
            # "services_seeds",
            "analysis_seeds",
            "radiologies_seeds",
            "vaccinations_seeds",
            "users_seeds",
            "employees_seeds",
            "doctors_seeds",
        ]
        for work in works:
            try:
                call_command(work)
                self.stdout.write(self.style.SUCCESS(f"Successfully {work}"))
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(f"{work} Failed >\n \t Error is: {e}")
                )

        call_command("superUser")
        call_command("runserver")
