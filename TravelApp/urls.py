from django.urls import path
from . import views

urlpatterns = [
    # path('',views.destination,''),
    # path('', views.registrationpage, ''),
    # path('', views.PhoneNumberView.as_view(), ''),
    path('', views.phone_number_view, ''),
]
