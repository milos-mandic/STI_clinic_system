__author__ = 'Milos'

# Core Django
from django.conf.urls import patterns, url, include

# Third-Party
from rest_framework import routers

from .views import STDTestViewSet, PatientRecordViewSet, PatientApprovalViewSet, SendNotificationViewSet

router = routers.DefaultRouter()
router.register('stds', STDTestViewSet)
router.register('records', PatientRecordViewSet)
router.register('approval', PatientApprovalViewSet)
router.register('notification', SendNotificationViewSet)

urlpatterns = patterns(
    '',
    url(r'^', include(router.urls)),
)
