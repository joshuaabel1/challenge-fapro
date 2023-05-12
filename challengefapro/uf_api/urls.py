from django.urls import path
from .views import UfValueView

urlpatterns = [
    path('uf-value/<str:date>/', UfValueView.as_view(), name='uf_value'),
]