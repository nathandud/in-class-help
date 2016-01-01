# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0003_auto_20150825_1220'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='student_question',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
