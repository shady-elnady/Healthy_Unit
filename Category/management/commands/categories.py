from django.core.management.base import BaseCommand

from App.models import Category


class Command(BaseCommand):
    data = "Categories"
    help = f"Creates initial {data} model"

    def handle(self, *args, **options):
        categories = [
            {"name": "English", "image": "", "translations": "", "category_parent": 1},
        ]

        for category in categories:
            try:
                Category.objects.create(
                    name=category["name"],
                )
                self.stdout.write(
                    self.style.SUCCESS(f"Successfully insert {self.data} > {category}")
                )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(
                        f"Failed insert {self.data} > {category} , \n \t Error is: \t \t{e}"
                    )
                )
        self.stdout.write(self.style.SUCCESS("Successfully created initial {data}"))
