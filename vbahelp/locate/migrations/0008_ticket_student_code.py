# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0007_ticket_js_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='student_code',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
