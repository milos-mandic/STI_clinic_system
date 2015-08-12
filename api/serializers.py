__author__ = 'Milos'

from rest_framework import serializers
from safematch_user.models import *
from test_results.models import STDTest


class STDTestSerializer(serializers.ModelSerializer):
    """
    Class for serializing STDTest.
    """

    class Meta:
        model  = STDTest
        fields = ('unique_id', 'std_name', 'result', 'test_date', 'result_date')


class STDTestPatientRecordSerializer(STDTestSerializer):
    """
    Serializer for STDTest contained in the PatientRecord.
    """

    class Meta:
        model = STDTestSerializer.Meta.model
        fields = ('unique_id', 'std_name', 'result', 'test_date', 'result_date')


class PatientRecordSerializer(serializers.ModelSerializer):
    """
    Serializer that represents PatientRecord.
    """
    tests = STDTestPatientRecordSerializer(many=True)

    class Meta:
        model = PatientRecord
        fields = ('patient', 'tests')


class PatientApprovalSerializer(serializers.ModelSerializer):
    """
    Serializer that represents PatientApproval class.
    """

    class Meta:
        model = PatientApproval
        fields = ('approval', 'last_checkup')

class SendNotificationSerializer(serializers.ModelSerializer):
    """

    """
    class Meta:
        model = SendNotification
        fields = ('something', )