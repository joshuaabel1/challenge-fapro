from django.urls import path
from .views import UfValueView

urlpatterns = [
    path('uf_value/<str:date>/', UfValueView.as_view(), name='uf_value'),
]