from progres_1.models import domeniu, client
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def get_domenii(request, token):
    if token is None or len(token) < 32 or client.Client.check_token(token, 'D', 'D', None) == 'N':
        return Response(data={"error": "Nu aveti autorizare pentru a viziona continutul"},
                        status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'GET':
        try:
            domenii = domeniu.Domeniu.get_domenii()
            return Response(domenii)
        except Exception as e:
            error_msg = str(e).split(' ', 1)[1].split('\n', 1)[0]
            print(e)
            data = {"error": error_msg}
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)