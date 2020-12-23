from django.urls import path

from .views import VictimDetailView


app_name = 'victims'

urlpatterns = [
    path('<slug:slug>/', VictimDetailView.as_view(), name='detail'),
]
