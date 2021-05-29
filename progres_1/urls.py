from django.urls import path
from progres_1.views import client, judet, localitate, domeniu, punct_lucru

urlpatterns = [

    #CLIENT
    path('client/register_client/', client.register_client),
    path('client/validare_cont_client/<str:token>/', client.validare_cont_client),
    path('client/generare_cod_inregistrare/<str:token>/', client.generare_cod_inregistrare),

    path('client/login/', client.login),
    path('client/validare_login/<str:token>/', client.validare_login),
    path('client/generare_cod_login/<str:token>/', client.generare_cod_login),

    path('client/validare_rezervare/<str:token>', client.validare_rezervare),
    path('client/get_client_from_email/<str:token>/', client.get_client_from_email),
    path('client/get_salt/', client.get_salt),


    #NOMENCLATOARE
    path('nomenclatoare/get_judete/', judet.get_judete),
    path('nomenclatoare/get_localitati/', localitate.get_localitati),
    path('nomenclatoare/get_domenii/<str:token>/', domeniu.get_domenii),


    #TERT
    path('tert/get_puncte_lucru/<str:token>/', punct_lucru.get_puncte_lucru),
    path('tert/get_program_punct/<str:token>/', punct_lucru.get_program_punct),
    path('tert/get_urmatoarea_zi_lucratoare/<str:token>/', punct_lucru.get_urmatoarea_zi_lucratoare),
    path('tert/get_procent_ocupare/<str:token>/', punct_lucru.get_procent_ocupare),
    path('tert/get_program_neeligibil/<str:token>/', punct_lucru.get_program_neeligibil),
    path('tert/get_tipuri_rezervare/<str:token>/', punct_lucru.get_tipuri_rezervare),


    #REZERVARE
    path('rezervare/verificare_timp_ales/<str:token>/', punct_lucru.verificare_timp_ales),
    path('rezervare/inregistrare_rezervare/<str:token>/', client.inregistrare_rezervare),
    path('rezervare/get_detalii_rezervare/<str:token>/', client.get_detalii_rezervare),
    path('rezervare/anulare_rezervare_client/<str:token>/', client.anulare_rezervare),



    # path('validate_registration/<user_id>', validate_user_registration),
    # path('generate_user_registration_token/<user_id>', generate_user_registration_token),
]