# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('locate', '0005_auto_20150826_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('major', models.TextField(max_length=50)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='location',
        ),
        migrations.AddField(
            model_name='studentlocation',
            name='ticket',
            field=models.ForeignKey(null=True, to='locate.Ticket'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ticket',
            name='student',
            field=models.ForeignKey(null=True, to='locate.Student'),
            preserve_default=True,
        ),
    ]
