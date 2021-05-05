from bootstrap_datepicker_plus import DatePickerInput
import datetime
from django import forms
from django.contrib.auth import get_user_model, authenticate, login
from .models import Hotel, HotelBooking, Explore, Flight


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data['username']
        password = cleaned_data['password']
        user = authenticate(username=username, password=password)
        if user is None:
            self.add_error(None, 'Podaj poprawny login lub haslo')

    def login(self, request):
        user = authenticate(**self.cleaned_data)
        return login(request, user)


class AddUserForm(forms.ModelForm):
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
            model = get_user_model()
            fields = ['username', 'password', 'first_name', 'last_name', 'email']
            widgets = {'password': forms.PasswordInput}

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['password'] != cleaned_data['password2']:
            self.add_error('password', 'Podaj poprawne haslo')
        if get_user_model().objects.filter(username=cleaned_data['username']):
            self.add_error('username', 'uzytkownik istnieje')



class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('name', 'country', 'city', 'address', 'description', 'image',)
        labels = {
            'name': 'name',
            'country': 'country',
            'image': 'image',
        }


class ExploreForm(forms.ModelForm):
    class Meta:
        model = Explore
        fields = ('continent', 'country', 'city', 'bookingType',)


class ReserveHotelRoomForm(forms.ModelForm):


    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['bookingStartDate'] < datetime.date.today():
            self.add_error('bookingStartDate', 'Incorrect date')
        if cleaned_data['bookingEndDate'] < datetime.date.today():
            self.add_error('bookingEndDate', 'Incorrect date')


    class Meta:
        model = HotelBooking
        fields = ('hotel', 'bookingStartDate',  'bookingEndDate', 'room')
        widgets = {
        'bookingStartDate' : DatePickerInput(format='%Y-%m-%d'),
        'bookingEndDate': DatePickerInput(format='%Y-%m-%d'),
        }

class FlightForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data['startDate'] < datetime.date.today():
            self.add_error('startDate', 'Incorrect date')
        if cleaned_data['endDate'] < datetime.date.today():
            self.add_error('endDate', 'Incorrect date')


    class Meta:
        model = Flight
        fields = ('fromCountry', 'fromCity',  'toCountry', 'toCity', 'startDate', 'endDate', 'classType')
        widgets = {
        'startDate' : DatePickerInput(format='%Y-%m-%d'),
        'endDate': DatePickerInput(format='%Y-%m-%d'),
        }


