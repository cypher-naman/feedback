# Generated by Django 2.1.1 on 2018-10-01 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='section',
            new_name='Section_name',
        ),
    ]
