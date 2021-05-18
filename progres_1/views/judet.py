from progres_1.models import judet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_judete(request):
    if request.method == 'GET':
        judete = judet.Judet.get_judete()
        return Response(judete)