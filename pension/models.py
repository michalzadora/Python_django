import datetime
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Room(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="Opis")

    def __str__(self):
        return self.name


class Reservation(models.Model):

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    reservation_date = models.DateField('Reservation date', default=timezone.now)
    date_from = models.DateField("From")
    date_to = models.DateField("To")
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    def __str__(self):
        return "Reservation date: {} from {} {} login as {}  ".format(self.reservation_date, self.name, self.surname, self.user)


class Comment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '<Name: {}, ID: {}>'.format(self.name, self.id)
