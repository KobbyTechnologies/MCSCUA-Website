# Generated by Django 4.1 on 2022-08-04 06:34

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0002_remove_faq_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
