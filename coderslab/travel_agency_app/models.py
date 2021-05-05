
from django.contrib.auth.models import User
from django.db import models


# class User(models.Model):
#     username = models.CharField(max_length=64)
#     email = models.CharField(max_length=64, unique=True)
#     password = models.CharField(max_length=64)

    # @property
    # def name(self):
    #     return "{} {}".format(self.first_name, self.last_name)
    #
    # def __str__(self):
    #     return self.username

# class CustomUser(AbstractUser):
#     def __str__(self):
#         return self.username


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
    continent = models.CharField(max_length=64, default='Asia')
    country = models.CharField(max_length=64, default='Indonesia')
    city = models.CharField(max_length=64, default='Bali')
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
    # user = models.ManyToManyField(User, through="UserHotel")
    # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    bookingStartDate = models.DateField()
    bookingEndDate = models.DateField()
    room = models.CharField(
        max_length=64,
        choices=ROOM_TYPE,
    )


# class UserHotel(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, null=True, blank=True)
#     hotel_reservation = models.ForeignKey(HotelBooking, on_delete=models.CASCADE, null=True, blank=True)


CLASS_TYPE = (
    ('economy', 'economy'),
    ('premium economy', 'premium economy'),
    ('business', 'business'),
    ('first class', 'first class'),
)


class Flight(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fromCountry = models.CharField(max_length=64, default='Poland')
    fromCity = models.CharField(max_length=64, default='Warsaw')
    toCountry = models.CharField(max_length=64, default='Indonesia')
    toCity = models.CharField(max_length=64, default='Bali')
    startDate = models.DateField()
    endDate = models.DateField()
    classType = models.CharField(max_length=64, choices=CLASS_TYPE)


# class Reservations(models.Model):
#     # user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     hotel_booking = models.ForeignKey(HotelBooking, on_delete=models.CASCADE, null=True, blank=True)
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE, null=True, blank=True)
