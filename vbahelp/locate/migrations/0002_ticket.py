# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('time', models.DateTimeField(auto_now=True)),
                ('completed', models.BooleanField(default=False)),
                ('location', models.OneToOneField(to='locate.StudentLocation')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
