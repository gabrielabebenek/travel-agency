"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from travel_agency_app import views as travel_agency_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', travel_agency_views.ExploreCreateView.as_view(), name='index'),
    path('login/', travel_agency_views.LoginView.as_view(), name="login"),
    path('logout/', travel_agency_views.LogoutView.as_view(), name="logout"),
    path('hotels/', travel_agency_views.HotelView.as_view(), name="hotels"),
    path('hotel/add', travel_agency_views.HotelCreateView.as_view(), name='create-hotel'),
    # path('city-hotels/<int:id>/', travel_agency_views.HotelCityView.as_view(), name="hotels-city"),
    # url(r'^hotels/(?P<city>[-a-zA-Z0-9_]+)/$', travel_agency_views.HotelCityView.as_view(), name="hotels-city"),
    path('hotel/<int:pk>/', travel_agency_views.HotelDetailsView.as_view(), name='hotel-details'),
    path('hotel/<int:id>/reserve/', travel_agency_views.ReserveHotelRoom.as_view(), name='hotel-reservation'),
    path('add-user/', travel_agency_views.AddUserView.as_view(), name='add-user'),
    path('list-users/', travel_agency_views.UserListView.as_view(), name='user-list-view'),
    path('flight/add', travel_agency_views.FlightCreateView.as_view(), name='create-flight'),
    path('travelove/', travel_agency_views.ExploreCreateView.as_view(), name='explore'),
    path('user-hotel-reservations/<int:pk>/', travel_agency_views.UserHotelReservationView.as_view(), name='user-hotel'),
    path('user-flight-reservations/<int:pk>/', travel_agency_views.UserFlightReservationView.as_view(), name='user-flight'),
    path('user-reservations/', travel_agency_views.ReservationsView.as_view(), name='user-reservations'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
