from django.urls import path
from .views import AirplaneListCreateView

urlpatterns = [
    path('fuel_stats/', AirplaneListCreateView.as_view(), name='airplane-stats-view'),
]
