# Generated by Django 4.1 on 2022-09-07 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0006_alter_jobadvert_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobadvert',
            name='how_to_apply',
            field=models.TextField(blank=True),
        ),
    ]
