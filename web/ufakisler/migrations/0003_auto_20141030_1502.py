# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ufakisler', '0002_project_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='link',
            field=models.CharField(max_length=50),
        ),
    ]
