from django.test import TestCase
from rest_framework.test import APIRequestFactory
from .views import endpoints, suggestions

class EndpointsViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_endpoints_view(self):
        request = self.factory.get('/invalid')
        response = endpoints(request)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.data,
            {
                "suggestions": "/suggestions",
                "swagger documentation": "/swagger",
                "redoc documentation": "/redoc"
            }
        )


class SuggestionsViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_suggestions_view(self):
        request = self.factory.get('/suggestions', {'q': 'London'})
        response = suggestions(request)
        self.assertEqual(response.status_code, 200)


    def test_no_suggestions_view(self):
        request = self.factory.get('/suggestions', {'q': 'Balabulu'})
        response = suggestions(request)
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(
            response.data,
            {
                "suggestions": []
            }
        )

