from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from unittest.mock import patch
from decimal import Decimal

from .utils.get_uf import get_uf_value


class UfValueViewTests(APITestCase):
    def setUp(self):
        self.client = APIClient()


    @patch('uf_api.views.get_uf_value')
    def test_get_uf_value_success(self, mock_get_uf_value):
        date = '2013-01-01'
        uf_value = '22.837,06'
        mock_get_uf_value.return_value = uf_value
        response = self.client.get(reverse('uf_value', args=[date]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"date": date, "uf_value": uf_value})


    def test_get_uf_value_date_before_2013(self):
        date = '2012-12-31'
        response = self.client.get(reverse('uf_value', args=[date]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "The minimum date that can be queried is 01-01-2013."})


    def test_get_uf_value_incorrect_date_format(self):
        date = 'incorrect_date_format'
        response = self.client.get(reverse('uf_value', args=[date]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Incorrect date format. Please use the format YYYY-MM-DD."})


    @patch('uf_api.views.get_uf_value')
    def test_get_uf_value_failure(self, mock_get_uf_value):
        date = '2021-01-01'
        mock_get_uf_value.return_value = None
        response = self.client.get(reverse('uf_value', args=[date]))
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {"error": "Failed to retrieve UF value for the specified date."})

