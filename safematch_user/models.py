from django.db import models
from django.conf import settings
from django_extensions.db.models import TimeStampedModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class PatientProfile(TimeStampedModel):
    """
    Contains basic patient's information.
    """
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name='profile')
    name = models.CharField(max_length=80, blank=True, null=True)
    surname = models.CharField(max_length=80, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=80, blank=True, null=True)
    unique_id = models.IntegerField()

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"

    def __unicode__(self):
        return u"{0} {1} - {2}".format(self.name, self.surname, self.unique_id)


class PatientSTDTest(TimeStampedModel):
    """
    User STD Results
    """
    test = models.ForeignKey('test_results.STDTest')
    record = models.ForeignKey('PatientRecord')

    class Meta:
        verbose_name = "Patient's test"

    def __unicode__(self):
        return u"{} - {}".format(self.test, self.record)


class PatientRecord(TimeStampedModel):
    """
    Collects all the user's STD tests.
    """
    patient = models.ForeignKey('PatientProfile', related_name='patient')
    tests = models.ManyToManyField('test_results.STDTest', related_name='tests',
                                   through='PatientSTDTest')

    class Meta:
        verbose_name_plural = "Patient's medical record"

    def __unicode__(self):
        return u'{0} record'.format(self.patient)

class PatientApproval(TimeStampedModel):
    """
    Final approval if the patient is safe.
    """
    approval = models.BooleanField(default=False)
    last_checkup = models.DateField(blank=True, null=True)


class SendNotification(TimeStampedModel):
    """

    """
    something = models.CharField(max_length=80, blank=True, null=True)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# @receiver(post_save, sender=PatientRecord)
# def approve_patient(sender, instance=None, created=False, **kwargs):
    """
    When we update the PatientRecord, we need to calculate if he is safe.
    """
