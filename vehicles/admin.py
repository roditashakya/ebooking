from django.contrib import admin

# Register your models here.
from .models import SeatTemplate, TravelDetail, Vehicle, Booking, BookingUser, Seat, Schedule, Search

admin.site.register(SeatTemplate)
admin.site.register(TravelDetail)
admin.site.register(Vehicle)
admin.site.register(Booking)
admin.site.register(BookingUser)
admin.site.register(Seat)
admin.site.register(Schedule)
admin.site.register(Search)