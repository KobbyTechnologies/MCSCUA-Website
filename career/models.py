from random import choices
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from blog.models import STATUS
from datetime import date
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField
# Create your models here.


class JobAdvert(models.Model):
    POSITION_TYPE = [
        ('Permanent', 'Permanent'),
        ('Contract', 'Contract'),
        ('Internship', 'Internship'),
        ('Attachment', 'Attachment')
    ]
    JOB_STATUS = [
        ('open', 'open'),
        ('closed', 'closed')
    ]

    title = models.CharField(max_length=200)
    job_ID = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200)
    job_description = models.TextField()
    resposibilities = models.TextField()
    qualification = models.TextField()
    how_to_apply = models.TextField(blank=True)
    advert_file = models.FileField(upload_to='media', blank=True)
    pub_date = models.DateTimeField(
        auto_now_add=True, help_text='Date Published')
    deadline = models.DateField(
        default=date.today, blank=True, help_text='deadline for application')
    job_status = models.CharField(
        choices=JOB_STATUS, max_length=20, default='open')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')
    job_type = models.CharField(choices=POSITION_TYPE, default='Contract',
                                max_length=200, help_text='Choose the appropriate job type to advertise')

    class Meta:
        verbose_name = 'Job Advert'

    @property
    def short_description(self):
        return truncatechars(self.job_description, 50)

    def __str__(self):
        return self.title


class Tender(models.Model):
    TENDER_STATUS = [
        ('open', 'open'),
        ('closed', 'closed')
    ]
    title = models.CharField(max_length=200)
    ref_number = models.CharField(max_length=50, unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField()
    tender_status = models.CharField(
        choices=TENDER_STATUS, max_length=20, default='open')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        ordering = ['-pub_date']
        verbose_name= 'Advertised Tender'

    @property
    def short_description(self):
        return truncatechars(self.description, 30)

    def __str__(self):
        return self.title

class ContractAward(models.Model):
    title = models.CharField(
        max_length=255, default='Contract Awards [year]', help_text='At the [year] replace with the tendering year')
    ref_number = models.CharField(max_length=255, unique=True)
    file = models.FileField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    def __str__(self):
        return self.ref_number


class PrequalifiedTender(models.Model):
    title = models.CharField(
        max_length=255, default='MSCSUA Pre-Qualified Suppliers [year]', help_text='At the [year] replace with the tendering year')
    ref_number = models.CharField(max_length=255, unique=True)
    file = models.FileField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    def __str__(self):
        return self.ref_number

class Service(models.Model):
    title = models.CharField(max_length= 255)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    def __str__(self):
        return self.title


class SupplierRegistrationDetails(models.Model):
    OWNERSHIP = [
        ('Kenyan', 'Kenyan'),
        ('Multi-National majority owned by Kenyan', 'Multi-National majority owned by Kenyan'),
        ('Multi-National Others', 'Multi-National Others'),
    ]
    
    ownership = models.CharField(max_length= 512, choices=OWNERSHIP)
    company_name = models.CharField(max_length=255)
    KRA_pin = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=255)
    country = CountryField()
    physical_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    services = models.ManyToManyField(Service)
    full_name  = models.CharField(max_length=255)
    mobile_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    company_certificate_reg = models.FileField()
    KRA_pin_certificate = models.FileField()
    KRA_compliance_certificate = models.FileField()
    company_memorandum_directors_page = models.FileField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name


