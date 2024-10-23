from django.db import models

class Booking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    reservation_date = models.DateField()
    reservation_slot = models.TimeField()
    num_people = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.reservation_date} - {self.reservation_slot}'
