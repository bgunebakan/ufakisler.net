# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ufakisler', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='link',
            field=models.CharField(default=b'0', max_length=50),
            preserve_default=True,
        ),
    ]
