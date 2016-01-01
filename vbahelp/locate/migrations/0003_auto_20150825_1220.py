# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0002_ticket'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentlocation',
            name='xcoord',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='studentlocation',
            name='ycoord',
            field=models.DecimalField(decimal_places=2, max_digits=10),
            preserve_default=True,
        ),
    ]
