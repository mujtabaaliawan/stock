from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from core.authentications.sender_authentication import SenderAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# from django_q.tasks import async_task
from core.tasks import dataupdate


class DataUpdater(APIView):

    parser_classes = [JSONParser]
    authentication_classes = [SenderAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        dataupdate(request.data)
        # async_task(dataupdate, request.data)
        return Response(status=status.HTTP_200_OK)
