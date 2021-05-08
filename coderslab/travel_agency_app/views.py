from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.urls import reverse_lazy, reverse
from .forms import (
    HotelForm,
    ReserveHotelRoomForm,
    ExploreForm,
    FlightForm,
)
from .models import (
    Hotel,
    HotelBooking,
    Explore,
    Flight,
)
User = get_user_model()


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'


class HotelView(LoginRequiredMixin, ListView):
    model = Hotel


class HotelCreateView(LoginRequiredMixin, CreateView):
    model = Hotel
    form_class = HotelForm
    success_url = reverse_lazy('hotels')


class HotelDetailsView(LoginRequiredMixin, DetailView):
    model = Hotel
    template_name = "view_hotel.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        hotels = Hotel.objects.filter(id=kwargs['object'].pk)
        context = {'hotels': hotels}
        return super().get_context_data(**context)


class ExploreCreateView(LoginRequiredMixin, CreateView):
    model = Explore
    form_class = ExploreForm
    template_name = 'explore.html'
    # success_url = reverse_lazy('hotels')

    def get(self, request, *args, **kwargs):
        context = {'form': self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            bookingType = form.cleaned_data['bookingType']
            city = form.cleaned_data['city']
            if bookingType == "Hotel":
                response = redirect('hotels')
                # response['Location'] += '?city=' + city
                return response
            elif bookingType == "Flight":
                return redirect('create-flight')


class ReserveHotelRoom(LoginRequiredMixin, CreateView):
    model = HotelBooking
    form_class = ReserveHotelRoomForm
    template_name = 'reserve_hotel_room2.html'

    def get_success_url(self):
        return reverse('user-hotel', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ReserveHotelRoom, self).get_form_kwargs(*args, **kwargs)
        kwargs['request'] = self.request
        return kwargs


class FlightCreateView(LoginRequiredMixin, CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flight.html'

    def get_success_url(self):
        return reverse('user-flight', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(FlightCreateView, self).get_form_kwargs(*args, **kwargs)
        kwargs['request'] = self.request
        return kwargs


class UserHotelReservationView(LoginRequiredMixin, DetailView):
    model = HotelBooking
    template_name = "userhotel_list.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        users = HotelBooking.objects.filter(id=kwargs['object'].pk)
        context = {'users': users}
        return super().get_context_data(**context)
    # def get(self, request, id):
    #     hotel = Hotel.objects.get(id=id)
    #     reservations = hotel.userhotel_set.filter(user_id=1)
    #     return render(request, "userhotel_list.html", context={"hotel": hotel, "reservations": reservations})


class UserFlightReservationView(LoginRequiredMixin, DetailView):
    model = Flight
    template_name = "userflight_list.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        users = Flight.objects.filter(id=kwargs['object'].pk)
        context = {'users': users}
        return super().get_context_data(**context)


class ReservationsView(LoginRequiredMixin, ListView):
    model = HotelBooking
    template_name = 'reservations_list.html'
    context_object_name = 'reservations'

    def get_queryset(self):
        return self.model.objects.all().filter(user_id=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(ReservationsView, self).get_context_data(**kwargs)
        context['flights'] = Flight.objects.filter(user_id=self.request.user)
        return context
