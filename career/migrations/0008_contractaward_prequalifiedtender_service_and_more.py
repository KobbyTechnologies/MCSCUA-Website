# Generated by Django 4.1 on 2022-11-03 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career', '0007_jobadvert_how_to_apply'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractAward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Contract Awards [year]', help_text='At the [year] replace with the tendering year', max_length=255)),
                ('ref_number', models.CharField(max_length=255, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
        migrations.CreateModel(
            name='PrequalifiedTender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='MSCSUA Pre-Qualified Suppliers [year]', help_text='At the [year] replace with the tendering year', max_length=255)),
                ('ref_number', models.CharField(max_length=255, unique=True)),
                ('file', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField()),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0, help_text='Change to Publish for it to be seen')),
            ],
        ),
        migrations.AlterModelOptions(
            name='tender',
            options={'ordering': ['-pub_date'], 'verbose_name': 'Advertised Tender'},
        ),
        migrations.CreateModel(
            name='SupplierRegistrationDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownership', models.CharField(choices=[('Kenyan', 'Kenyan'), ('Multi-National majority owned by Kenyan', 'Multi-National majority owned by Kenyan'), ('Multi-National Others', 'Multi-National Others')], max_length=512)),
                ('company_name', models.CharField(max_length=255)),
                ('KRA_pin', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('physical_address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_address', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('full_name', models.CharField(max_length=255)),
                ('mobile_number', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('company_certificate_reg', models.FileField(upload_to='')),
                ('KRA_pin_certificate', models.FileField(upload_to='')),
                ('KRA_compliance_certificate', models.FileField(upload_to='')),
                ('company_memorandum_directors_page', models.FileField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('services', models.ManyToManyField(to='career.service')),
            ],
        ),
    ]
