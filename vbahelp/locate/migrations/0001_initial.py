# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassroomLayout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('file_upload', models.ImageField(upload_to='layouts/')),
                ('filename', models.TextField(max_length=30)),
                ('title', models.TextField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='StudentLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('xcoord', models.DecimalField(decimal_places=4, max_digits=10)),
                ('ycoord', models.DecimalField(decimal_places=4, max_digits=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
