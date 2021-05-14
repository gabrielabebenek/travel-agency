from travel_agency_app.views import (
    ReservationsView,
    HotelView,
    HotelCreateView,
    FlightCreateView,
    ReviewCreateView,
    ReviewView,
)
from django.test import RequestFactory
from django.contrib.auth.models import AnonymousUser, User

# 302 Found
# The RequestFactory shares the same API as the test client.
# However, instead of behaving like a browser, the RequestFactory
# provides a way to generate a request instance that can be used as
# the first argument to any view.

def test_details_requires_login():
    request = RequestFactory().get('/user-reservations/')
    request.user = AnonymousUser()
    response = ReservationsView.as_view()(request)
    assert response.status_code == 302

#     rf jest instancją django.test.RequestFactory, która jest wykorzystywana
#     do pisania testów widoków bez przechodzenia przez wszystkie middleware.
#     Dzięki temu narzędziowi możemy przetestować konkretną zmienną lub metodę
#     w klasie widoku.
def test_details_hotel(rf):
    request = rf.get('/hotels')
    request.user = AnonymousUser()
    response = HotelView.as_view()(request)
    assert response.status_code == 302

def test_create_hotel(rf):
    request = rf.get('/hotels/add')
    request.user = AnonymousUser()
    response = HotelCreateView.as_view()(request)
    assert response.status_code == 302

def test_create_flight(rf):
    request = rf.get('/flight/add')
    request.user = AnonymousUser()
    response = FlightCreateView.as_view()(request)
    assert response.status_code == 302

def test_flight(rf):
    request = rf.get('/flight/add')
    request.user = AnonymousUser()
    response = FlightCreateView.as_view()(request)
    assert response.status_code == 302

def test_hotel_reservation(rf):
    request = rf.get('/user-hotel-reservations/<int:pk>/')
    request.user = AnonymousUser()
    response = FlightCreateView.as_view()(request)
    assert response.status_code == 302

def test_create_review(rf):
    request = rf.get('/review/add/')
    request.user = AnonymousUser()
    response = ReviewCreateView.as_view()(request)
    assert response.status_code == 302

def test_review_view(rf):
    request = rf.get('/user-review')
    request.user = AnonymousUser()
    response = ReviewView.as_view()(request)
    assert response.status_code == 302


