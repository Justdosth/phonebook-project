from django.urls import path
from .views import contact_list, add_contact

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('add_contact/', add_contact, name='add_contact'),
]
