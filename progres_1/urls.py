from django.urls import path
from .views import get_clienti, register_client, login, get_puncte_lucru,\
        inregistrare_rezervare, validare_rezervare, get_judete, get_localitati

urlpatterns = [
    path('get_clienti/', get_clienti),
    path('get_puncte_lucru/<str:client_token>/', get_puncte_lucru),
    path('register_client/', register_client),
    path('get_judete/', get_judete),
    path('get_localitati/', get_localitati),
    path('inregistrare_rezervare/<str:client_token>/', inregistrare_rezervare),
    path('validare_rezervare', validare_rezervare),
    path('login/', login),
    # path('validate_registration/<user_id>', validate_user_registration),
    # path('generate_user_registration_token/<user_id>', generate_user_registration_token),
]