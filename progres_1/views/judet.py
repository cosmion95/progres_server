from progres_1.models import judet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_judete(request):
    if request.method == 'GET':
        try:
            judete = judet.Judet.get_judete()
            return Response(judete)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)