from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from test_results.models import STDTest
from .serializers import *
import commands

class STDTestViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Get article object by article_id
    """
    queryset = STDTest.objects.all()
    serializer_class = STDTestSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class PatientRecordViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """

    """
    queryset = PatientRecord.objects.all()
    serializer_class = PatientRecordSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class PatientApprovalViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """

    """
    queryset = PatientApproval.objects.all()
    serializer_class = PatientApprovalSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

class SendNotificationViewSet(viewsets.ModelViewSet):
    """

    """
    queryset = SendNotification.objects.all()
    serializer_class = SendNotificationSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAuthenticated, )

    def create(self, request, format=None):
        serializer = SendNotificationSerializer(data=request.DATA)
        something = request.DATA.get('something')
        a = commands.getoutput('php simplepush.php')
        print a
        return Response({"error:", "favorite already exists"}, status=status.HTTP_201_CREATED)
