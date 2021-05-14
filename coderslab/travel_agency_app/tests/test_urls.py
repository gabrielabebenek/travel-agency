from django.urls import reverse, resolve

# run : (env) gabriela@gabriela-Legion-Y540-15IRH:~/workspace/travel-agency/coderslab$ py.test
class TestUrls:

    def test_detail_url(self):
        path = reverse('hotel-details', kwargs={'pk': 1})
        assert resolve(path).view_name == 'hotel-details'