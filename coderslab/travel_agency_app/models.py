from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=64, default='Hotel')
    country = models.CharField(max_length=64)
    city = models.CharField(max_length=64)
    address = models.CharField(max_length=64)
    description = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='hotel/', null=True, blank=True)

    def __str__(self):
        return self.name


BOOKING_TYPE = (
    ('Hotel', 'Hotel'),
    ('Flight', 'Flight'),
)


class Explore(models.Model):
    # continent = models.CharField(max_length=64, default='Asia')
    # country = models.CharField(max_length=64, default='Indonesia')
    # city = models.CharField(max_length=64, default='Bali')
    bookingType = models.CharField(
        max_length=64,
        choices=BOOKING_TYPE,
    )


ROOM_TYPE = (
    ('1 person', '1 person'),
    ('2 people', '2 people'),
    ('3 people', '3 people'),
    ('4 people', '4 people'),
    ('5 people', '5 people'),
)


class HotelBooking(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    bookingStartDate = models.DateField()
    bookingEndDate = models.DateField()
    room = models.CharField(
        max_length=64,
        choices=ROOM_TYPE,
    )


CLASS_TYPE = (
    ('Economy', 'Economy'),
    ('Premium economy', 'Premium economy'),
    ('Business', 'Business'),
    ('First class', 'First class'),
)


class Flight(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fromCountry = models.CharField(max_length=64, default='Poland')
    fromCity = models.CharField(max_length=64, default='Warsaw')
    toCountry = models.CharField(max_length=64, default='Indonesia')
    toCity = models.CharField(max_length=64, default='Bali')
    startDate = models.DateField()
    endDate = models.DateField()
    classType = models.CharField(max_length=64, choices=CLASS_TYPE)


RATING_TYPE = (
    ('1', '*'),
    ('2', '**'),
    ('3', '***'),
    ('4', '****'),
    ('5', '*****'),
)


class Review(models.Model):
    review = models.CharField(max_length=1000)
    rating = models.CharField(max_length=64, choices=RATING_TYPE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    hotel = models.ForeignKey(Hotel, null=True, blank=True, on_delete=models.CASCADE)
