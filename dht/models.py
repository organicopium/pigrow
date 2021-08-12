from django.db import models

# Create your models here.

class DHT22Measure(models.Model):
    humidity = models.DecimalField(max_digits=3, decimal_places=2)
    temperature = models.DecimalField(max_digits=3, decimal_places=2)
    ts = models.DateTimeField()

    def __str__(self):
        return "{}%, {}°c {}".format(self.humidity, self.temperature, self.ts())
