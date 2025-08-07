from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Room(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    room_type = models.CharField(max_length=50)
    sleep_places = models.PositiveIntegerField()
    day_price = models.DecimalField(max_digits=8, decimal_places = 2)
    ocuppied = models.BooleanField(default = True)


    def __str__(self):
        return f"{self.name} ({self.room_type})"

    def formatted_price(self):
        return f"{self.day_price} грн/доба"
class Booking(models.Model):
    user = models.ForeignKey(User, verbose_name="Користувач", on_delete=models.CASCADE)
    room = models.ForeignKey(Room, verbose_name="Кімната", on_delete=models.CASCADE)
    date_from = models.DateField("З дати")
    date_to = models.DateField("До дати")
    is_confirmed = models.BooleanField("Підтверджено", default=False)

    def __str__(self):
        return f"Бронювання: {self.room.name} з {self.date_from} по {self.date_to} для {self.user.username}"

