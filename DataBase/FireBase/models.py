# from django.db import models

# Create your models here.

from FireBase.FireBaseORM import models


class TModel(models.Model):
    name = models.TextField()
    type_test = models.TextField(db_column="type")

    class Meta:
        db_table = "test"

    def __str__(self):
        return str(self.name)
