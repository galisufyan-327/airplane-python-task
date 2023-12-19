from django.db import models
import math

class Airplane(models.Model):
    id = models.IntegerField(primary_key=True)
    passengers = models.IntegerField()

    def fuel_capacity(self):
        return 200 * self.id

    def fuel_consumption_per_minute(self):
        return (0.80 * math.log10(self.id)) + (0.002 * self.passengers)