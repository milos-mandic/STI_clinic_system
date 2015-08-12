# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='STDTest',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(default=django.utils.timezone.now, verbose_name='created', editable=False, blank=True)),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(default=django.utils.timezone.now, verbose_name='modified', editable=False, blank=True)),
                ('unique_id', models.IntegerField()),
                ('std_name', models.CharField(max_length=80, null=True, blank=True)),
                ('result', models.CharField(max_length=10, choices=[(b'Positive', b'Positive'), (b'Negative', b'Negative')])),
                ('test_date', models.DateField(null=True, blank=True)),
                ('result_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'STD test',
                'verbose_name_plural': 'STD tests',
            },
            bases=(models.Model,),
        ),
    ]
