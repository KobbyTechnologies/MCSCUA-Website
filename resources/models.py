from operator import truediv
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from blog.models import STATUS
from cloudinary.models import CloudinaryField

# Create your models here.


class Faq(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Frequently Asked Question'

    @property
    def short_description(self):
        return truncatechars(self.answer, 30)

    def __str__(self):
        return self.question


class PubCategory(models.Model):
    category = models.CharField(max_length=255)

    def __str__(self):
        return self.category


class Publication(models.Model):

    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='media')
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(PubCategory, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        verbose_name = 'Resource'

    def __str__(self):
        return self.name


class Privacy(models.Model):
    title = models.CharField(max_length=200, default='Privacy Policy')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='media')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='change to published to be seen')

    class Meta:
        verbose_name = 'Privacy Policy'
        verbose_name_plural = 'Privacy Policy'

    def __str__(self):
        return self.title


class Terms(models.Model):
    title = models.CharField(max_length=200, default='Terms of Service')
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to='media')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='change to published to be seen')

    class Meta:
        verbose_name = 'Terms of Service'
        verbose_name_plural = 'Terms of Service'

    def __str__(self):
        return self.title


BOOLEAN = [
    ('Yes', 'Yes'),
    ('No', 'No')
]


class CustomerSurvey(models.Model):

    organization = models.CharField(max_length=255,)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200, blank=True)
    date_created = models.DateField()
    Quality = models.CharField(
        max_length=255, help_text='Quality of our service')
    integrity = models.CharField(
        max_length=255, help_text='Courtesy/honesty/integrity')
    service_delivery = models.CharField(
        max_length=255, help_text='Service Delivery time')
    problem_solving = models.CharField(
        max_length=255, help_text='Addressing Issues/Problems')
    response = models.CharField(
        max_length=255, help_text='Communication/Response')
    comments = models.TextField(
        blank=True, help_text='Other relevant comments or Information')
    mode_of_response = models.CharField(
        max_length=200, blank=True, help_text='Would you prefer receiving this questionnaire by email or other means?')
    mode_of_response_type = models.CharField(
        max_length=200, blank=True, help_text='If other Kindly specify')
    email = models.EmailField(blank=True)

    def __str__(self):
        return '%s %s %s%s%s' % (self.name, ' - ', '(', self.organization, ')')


class AuditServiceCharter(models.Model):
    organization = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=200)
    date_created = models.DateField()
    receipt_issue = models.CharField(
        max_length=255, help_text='How long does it take to be issued a cess receipt upon payment of cess or License')
    complaint_log = models.CharField(
        max_length=255, help_text='How do you log complaints')
    complaint_address = models.CharField(
        max_length=255, help_text='How long does it take for customer complaints to be addressed?')
    satisfaction = models.BooleanField(
        max_length=255, blank=True, help_text='Are the complaints addressed to your satisfaction?')
    license_payment_processing = models.CharField(
        max_length=255, blank=True, help_text='How long does it take to process a License after payment?')
    automated_license_system = models.BooleanField(
        blank=True, help_text='Would it be convenient for you to have an automated Licensing system?')
    response = models.CharField(
        max_length=255, help_text='Other relevant comments or information:')
    comments = models.TextField(
        blank=True, help_text='Would you prefer receiving this questionnaire by email or other means?')
    mode_of_response = models.CharField(
        max_length=200, blank=True, help_text='if Other Kindly specify')
    email = models.EmailField(blank=True, help_text='Your Email address')

    def __str__(self):
        return '%s %s %s%s%s' % (self.name, ' - ', '(', self.organization, ')')


class LicenceApplication(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    tel = models.CharField(max_length=50, verbose_name='Address and Tel')
    physical_address = models.CharField(max_length=1000)
    reg_no = models.CharField(max_length=50, verbose_name='ID No. /Reg No')
    source_location = models.CharField(
        max_length=255, verbose_name='Name of Ward and Sub-location (Source of sand)')
    destination_location = models.CharField(
        max_length=255, verbose_name='Destination (Place where sand is being taken)')
    quantity = models.CharField(
        max_length=50, verbose_name='Quantity to be taken on daily basis')
    tranportation = models.CharField(
        max_length=255, verbose_name='Mode of transportation')
    vehicle_reg_no = models.CharField(
        max_length=255, blank=True, verbose_name='(Registration Number of Vehicle)')
    capacity = models.CharField(max_length=50, blank=True)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s %s' % (self.first_name, ' ', self.last_name)
