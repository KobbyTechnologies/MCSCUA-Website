# Generated by Django 4.1 on 2022-08-18 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_calltoactionpanel_status_alter_carousel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calltoactionpanel',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
