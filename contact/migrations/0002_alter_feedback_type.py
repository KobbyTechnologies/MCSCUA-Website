# Generated by Django 4.1 on 2022-08-25 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='type',
            field=models.IntegerField(choices=[(0, 'Inqury'), (1, 'Suggestions'), (2, 'Complaints')]),
        ),
    ]
