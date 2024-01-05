from django.db import models
from django.contrib.auth.models import User


# Create your models here.

NUM_TABLES = ((4, "2"), (4, "4"), (6, "6"))
TIME_SLOTS = (
    (1, "12:00 - 15:00"),
    (2, "17:00 - 19:00"),
    (3, "19:00 - 21:00"),
)


class Table(models.Model):
    """Modèle pour une table de restaurant"""

    table_number = models.IntegerField(unique=True)
    table_num_seats = models.IntegerField(choices=NUM_TABLES, default=2)

    class Meta:
        ordering = ["table_number"]

    def __str__(self):
        return str(self.table_number)
