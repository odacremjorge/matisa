# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('empleado', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleado',
            name='user',
            field=models.OneToOneField(related_name='empleado', null=True, default=None, to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE),
        ),
    ]
