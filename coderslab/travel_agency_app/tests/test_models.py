from mixer.backend.django import mixer
from travel_agency_app.models import Hotel
from django.urls import reverse
import pytest


def test_with_authenticated_client(client, django_user_model):
    username = "user1"
    password = "bar"
    user = django_user_model.objects.create_user(username=username, password=password)
    client.login(username=username, password=password)
    response = client.get('/travelove')
    assert response.status_code == 301



@pytest.mark.django_db
class TestModels:

    def test_hotel_models(self):
        # generate model instance and save to db
        hotel = mixer.blend(Hotel)

        print(hotel.name)
        print(hotel.country)

        # generate few pieces
        # hotels = mixer.cycle(4).blend('travel_agency_app.hotel')



