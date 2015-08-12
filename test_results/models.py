from django.db import models
from django_extensions.db.models import TimeStampedModel


class STDTest(TimeStampedModel):
    """
    An example of a test for an STD a patient can take.
    """
    unique_id = models.IntegerField()
    std_name = models.CharField(max_length=80, blank=True, null=True)
    result = models.CharField(max_length=10, choices=(('Positive', 'Positive'),('Negative', 'Negative')))
    test_date = models.DateField(blank=True, null=True)
    result_date = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'STD test'
        verbose_name_plural = 'STD tests'

    def __unicode__(self):
        return u'{0} - {1}'.format(self.std_name, self.unique_id)