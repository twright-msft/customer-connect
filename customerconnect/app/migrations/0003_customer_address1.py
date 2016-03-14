# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_customer_assignment'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='address1',
            field=models.CharField(max_length=200, null=True),
            preserve_default=True,
        ),
    ]
