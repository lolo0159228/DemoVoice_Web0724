# Generated by Django 2.2.3 on 2019-09-14 08:32

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190914_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voice',
            name='SongID',
        ),
        migrations.AddField(
            model_name='voice',
            name='id',
            field=models.AutoField(auto_created=True, default=builtins.id, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]