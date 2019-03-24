from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class SeatTemplate(models.Model):
    name = models.CharField(max_length=250)
    photo = models.ImageField()
    seat_count = models.IntegerField(default=0)
    seat_name = models.TextField()
    seat_price = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class TravelDetail(models.Model):
    name =models.CharField(max_length=250)
    journey = models.CharField(max_length=250)
    departure = models.DateTimeField(auto_created=True)
    seat_template = models.ForeignKey(SeatTemplate, on_delete=models.DO_NOTHING)
    bus_operator = models.CharField(max_length=250)
    seat_count = models.IntegerField(default=0)
    fare = models.IntegerField(default=0)

    def __str__(self):
        return self.journey


class Vehicle(models.Model):
    name = models.CharField(max_length=250)
    departure = models.DateTimeField(auto_created=True)
    route = models.CharField(max_length=250)
    #seat_template = models.ForeignKey(SeatTemplate, on_delete=models.DO_NOTHING)
    travel = models.ForeignKey(SeatTemplate, on_delete=models.DO_NOTHING)
    fare = models.IntegerField(default=0)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Booking(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    schedule = models.CharField(max_length=250)
    seat_names = models.CharField(max_length=250)
    duration = models.TimeField(auto_created=True)
    total = models.IntegerField(default=1)
    ticket = models.IntegerField(default=0)

    def __str__(self):
        return self.schedule


class BookingUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=250, blank=True)
    phone = models.CharField(max_length=250)
    phone_verified = models.BooleanField()
    email =models.EmailField()
    email_verified = models.BooleanField()
    boarding_points = models.CharField(max_length=250)
    seat_number = models.TextField(default=0)

    def __str__(self):
        return self.user


class Seat(models.Model):
    seat_name = models.CharField(max_length=250)
    selected_seat = models.IntegerField(default=0)
    available_seat = models.IntegerField(default=0)
    booked_seat = models.IntegerField(default=0)
    fare = models.IntegerField(default=0)

    def __str__(self):
        return self.seat_name



class Schedule(models.Model):
    route = models.CharField(max_length=250)
    departure_date = models.DateTimeField(auto_now_add=True)
    availabile_services = models.TextField(blank=True)
    boarding_points = models.TextField(blank=True)
    dropping_points = models.CharField(max_length=250)
    fare = models.IntegerField(default=0)

    def __str__(self):
        return self.route



class Search(models.Model):
    from_address = models.CharField(max_length=250)
    to_address = models.CharField(max_length=250)
    departure_date = models.DateField(auto_created=True)
    return_date = models.DateField(auto_created=True)
    passengers = models.IntegerField(blank=True)

    def __str__(self):
        return self.from_address

