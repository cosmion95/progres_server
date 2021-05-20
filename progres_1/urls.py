from django.urls import path
from progres_1.views import client, judet, localitate, domeniu, punct_lucru

urlpatterns = [

    #CLIENT
    path('client/register_client/', client.register_client),
    path('client/login/', client.login),
    path('client/validare_cont_client/<str:token>/', client.validare_cont_client),
    path('client/generare_cod_inregistrare/<str:token>/', client.generare_cod_inregistrare),
    path('client/inregistrare_rezervare/<str:token>/', client.inregistrare_rezervare),
    path('client/validare_rezervare/<str:token>', client.validare_rezervare),
    path('client/get_client_from_email/<str:token>/', client.get_client_from_email),

    #NOMENCLATOARE
    path('nomenclatoare/get_judete/', judet.get_judete),
    path('nomenclatoare/get_localitati/', localitate.get_localitati),
    path('nomenclatoare/get_domenii/<str:token>/', domeniu.get_domenii),

    #TERT
    path('terti/get_puncte_lucru/<str:token>/', punct_lucru.get_puncte_lucru),
    path('terti/get_program_punct/<str:token>/', punct_lucru.get_program_punct),
    path('terti/get_urmatoarea_zi_lucratoare/<str:token>/', punct_lucru.get_urmatoarea_zi_lucratoare),
    path('terti/get_procent_ocupare/<str:token>/', punct_lucru.get_procent_ocupare),









    # path('validate_registration/<user_id>', validate_user_registration),
    # path('generate_user_registration_token/<user_id>', generate_user_registration_token),
]