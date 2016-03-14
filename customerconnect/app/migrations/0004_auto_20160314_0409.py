# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_customer_address1'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address2',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='city',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='country',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='postal_code',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='customer',
            name='state',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
