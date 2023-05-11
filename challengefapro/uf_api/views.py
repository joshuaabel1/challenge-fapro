from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers.serializers import UfValueSerializer
import requests
from bs4 import BeautifulSoup
import datetime

from .utils.get_uf import get_uf_value


class UfValueView(APIView):
    def get(self, request, date, format=None):
        try:
            date_dt = datetime.datetime.strptime(date, "%Y-%m-%d").date()
            min_date = datetime.date(2013, 1, 1)

            if date_dt < min_date:
                return Response({"error": "The minimum date that can be queried is 01-01-2013."},
                                status=status.HTTP_400_BAD_REQUEST)

            uf_value = get_uf_value(date)

            if uf_value:
                uf_value_data = {"date": date_dt, "uf_value": uf_value}
                serializer = UfValueSerializer(uf_value_data)
                return Response(serializer.data)
            else:
                return Response({"error": "Failed to retrieve UF value for the specified date."},
                                status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response({"error": "Incorrect date format. Please use the format YYYY-MM-DD."},
                            status=status.HTTP_400_BAD_REQUEST)
