# Generated by Django 2.0.7 on 2018-07-21 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_layer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='layer',
            old_name='high',
            new_name='hight',
        ),
    ]
