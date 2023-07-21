from django.db import models

# Create your models here.


class Booking(models.Model):
    name = models.CharField(max_length=200)
    reservation_date = models.DateField()
    no_of_guests = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.name}: {self.reservation_date}'


class Menu(models.Model):
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=5)

    def __str__(self):
        return f'{self.title}: {self.price:.2f}'
