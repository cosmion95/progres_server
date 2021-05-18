from progres_1.models import localitate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def get_localitati(request):
    try:
        localitati = localitate.Localitate.get_localitati(request.data)
        return Response(localitati, status=status.HTTP_200_OK)
    except Exception as e:
        error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
        print(e)
        data = {"error": error_msg}
        return Response(data=data, status=status.HTTP_400_BAD_REQUEST)

