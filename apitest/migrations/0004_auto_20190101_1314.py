# Generated by Django 2.1.3 on 2019-01-01 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0003_apis'),
    ]

    operations = [
        migrations.RenameField(
            model_name='apis',
            old_name='apiparmvalue',
            new_name='apiparamvalue',
        ),
        migrations.RenameField(
            model_name='apis',
            old_name='apirul',
            new_name='apiurl',
        ),
    ]