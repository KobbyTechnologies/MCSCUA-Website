# Generated by Django 4.1 on 2022-09-05 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0015_corevalue_alter_aboutus_options_alter_aboutus_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corevalue',
            name='title',
            field=models.CharField(default='Core Values', max_length=200),
        ),
    ]