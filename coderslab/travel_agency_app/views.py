from django.contrib.auth import get_user_model, logout
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    FormView,
    RedirectView,
)
from django.urls import reverse_lazy, reverse
from .forms import (
    HotelForm,
    ReserveHotelRoomForm,
    AddUserForm,
    ExploreForm,
    FlightForm,
    LoginForm,
)
from .models import (
    Hotel,
    HotelBooking,
    Explore,
    Flight,
)
User = get_user_model()


class LoginView(LoginRequiredMixin, FormView):
    login_url = '/login/'
    form_class = LoginForm
    template_name = 'travel_agency_app/loginuser.html'
    success_url = reverse_lazy('index')
    permission_required = 'auth.change_user'

    def form_valid(self, form):
        form.login(self.request)
        return super().form_valid(form)


class LogoutView(RedirectView):
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)

class AddUserView(CreateView):
    model = User
    form_class = AddUserForm
    template_name = 'adduser.html'
    success_url = reverse_lazy('user-list-view')


class UserListView(ListView):
    model = User


class HotelView(ListView):
    model = Hotel

    # def get_context_data(self, **kwargs):
    #     hotels = Hotel.objects.filter(city=self.kwargs['city'])


class HotelCreateView(CreateView):
    model = Hotel
    form_class = HotelForm
    success_url = reverse_lazy('hotels')


class HotelDetailsView(DetailView):
    model = Hotel
    template_name = "view_hotel.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        hotels = Hotel.objects.filter(id=kwargs['object'].pk)
        context = {'hotels': hotels}
        return super().get_context_data(**context)


class ExploreCreateView(CreateView):
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
                response['Location'] += '?city=' + city
                return response
            elif bookingType == "Flight":
                return redirect('create-flight')


class ReserveHotelRoom(CreateView):
    model = HotelBooking
    form_class = ReserveHotelRoomForm
    template_name = 'reserve_hotel_room2.html'

    def get_success_url(self):
        return reverse('user-hotel', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(ReserveHotelRoom, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class FlightCreateView(CreateView):
    model = Flight
    form_class = FlightForm
    template_name = 'flight.html'

    def get_success_url(self):
        return reverse('user-flight', kwargs={'pk': self.object.pk})

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super(FlightCreateView, self).get_form_kwargs(*args, **kwargs)
        return kwargs


class UserHotelReservationView(DetailView):
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


class UserFlightReservationView(DetailView):
    model = Flight
    template_name = "userflight_list.html"
    pk_url_kwarg = 'pk'

    def get_context_data(self, **kwargs):
        users = Flight.objects.filter(id=kwargs['object'].pk)
        context = {'users': users}
        return super().get_context_data(**context)


class ReservationsView(ListView):
    template_name = "user-reservations_list.html"

    def get_context_data(self, **kwargs):
        context = super(ReservationsView, self).get_context_data(**kwargs)
        context['flight'] = Flight.objects.filter(user=self.request.user)
        context['hotelbooking'] = HotelBooking.objects.filter(user=self.request.user)
        return context
