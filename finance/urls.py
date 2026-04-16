from django.urls import path
from .views import finance_home

urlpatterns = [
    # This just points to your home page view. No includes!
    path('', finance_home, name='finance_home'),
]