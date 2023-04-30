from django.urls import path
from . import views
app_name = "testdjango"

urlpatterns = [
    path("<month>", views.monthly_challenge)
]
