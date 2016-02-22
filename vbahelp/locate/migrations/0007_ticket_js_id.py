# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0006_auto_20160201_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='js_id',
            field=models.TextField(null=True, max_length=15),
            preserve_default=True,
        ),
    ]
