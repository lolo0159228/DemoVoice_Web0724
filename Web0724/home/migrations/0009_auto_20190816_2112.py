# Generated by Django 2.2.3 on 2019-08-16 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_voice_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voice',
            name='File',
            field=models.FileField(upload_to='home/static/uploads'),
        ),
    ]
