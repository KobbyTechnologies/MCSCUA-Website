# Generated by Django 4.1.7 on 2023-02-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_alter_rateus_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rateus',
            name='rate',
            field=models.CharField(max_length=50),
        ),
    ]