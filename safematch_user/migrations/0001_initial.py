# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('test_results', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatientProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('name', models.CharField(max_length=80, null=True, blank=True)),
                ('surname', models.CharField(max_length=80, null=True, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('location', models.CharField(max_length=80, null=True, blank=True)),
                ('unique_id', models.IntegerField()),
                ('user', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Patient',
                'verbose_name_plural': 'Patients',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('patient', models.ForeignKey(related_name='patient', to='safematch_user.PatientProfile')),
            ],
            options={
                'verbose_name_plural': "Patient's medical record",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatientSTDTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('record', models.ForeignKey(to='safematch_user.PatientRecord')),
                ('test', models.ForeignKey(to='test_results.STDTest')),
            ],
            options={
                'verbose_name': "Patient's test",
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patientrecord',
            name='tests',
            field=models.ManyToManyField(related_name='tests', through='safematch_user.PatientSTDTest', to='test_results.STDTest'),
            preserve_default=True,
        ),
    ]
