from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS
from datetime import datetime  

# Create your models here.

CATEGORY = [
    (0, 'Board of Directors'),
    (1, "Management Team")
]

class ChairPerson(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(
        max_length=50, blank=True, help_text='Optional')
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media',  null=True,
                              blank=True, help_text='Image size should be in .jpg or .png')
    category = models.IntegerField(
        choices=CATEGORY, default=0, help_text='select Peronel membership title')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ChairPerson'
        verbose_name_plural = 'ChairPerson'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def full_name(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    full_name.short_description = 'Name'
    full_name.allow_tags = True

    def profile_photo(self):
        return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

    profile_photo.short_description = 'Image'
    profile_photo.allow_tags = True

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)


class Personel(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(
        max_length=50, blank=True, help_text='Optional')
    last_name = models.CharField(max_length=50)
    position = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media',  null=True,
                              blank=True, help_text='Image size should be in .jpg or .png')
    category = models.IntegerField(
        choices=CATEGORY, default=0, help_text='select Peronel membership title')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Personel'
        verbose_name_plural = 'Personel'

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def full_name(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

    full_name.short_description = 'Name'
    full_name.allow_tags = True

    def profile_photo(self):
        return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

    profile_photo.short_description = 'Image'
    profile_photo.allow_tags = True

    def __str__(self):
        return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)
# class ChairPerson(models.Model):
#     first_name = models.CharField(max_length=50)
#     middle_name = models.CharField(
#         max_length=50, blank=True, help_text='Optional')
#     last_name = models.CharField(max_length=50)
#     position = models.CharField(max_length=100)
#     description = models.TextField(null=True, blank=True)
#     image = models.ImageField(upload_to='media',  null=True,
#                               blank=True, help_text='Image size should be in .jpg or .png')
#     category = models.IntegerField(
#         choices=CATEGORY, default=0, help_text='select Peronel membership title')
#     status = models.IntegerField(
#         choices=STATUS, default=0, help_text='Change to Publish for it to be seen')
#     pub_date = models.DateTimeField(auto_now_add=True)

#     class Meta:
#         verbose_name = 'ChairPerson'
#         verbose_name_plural = 'ChairPerson'

#     @property
#     def short_description(self):
#         return truncatechars(self.description, 20)

#     def full_name(self):
#         return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

#     full_name.short_description = 'Name'
#     full_name.allow_tags = True

#     def profile_photo(self):
#         return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

#     profile_photo.short_description = 'Image'
#     profile_photo.allow_tags = True

#     def __str__(self):
#         return '%s %s %s' % (self.first_name, self.middle_name, self.last_name)

class MDsMessage(models.Model):
    title = models.CharField(
        max_length=200, help_text="e.g. John's Message", default='Message from the Managing Director')
    message = models.TextField()
    image = models.ImageField(
        upload_to='media', help_text='picture shoulde be at least 512px by 512px and either .jpg or .png')
    name_of_md = models.CharField(
        max_length=255, help_text='Write the full name')
    position = models.CharField(max_length=50, default='Managing Director')
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Published for it to be seen')

    class Meta:
        verbose_name = 'MDs Message'

    @property
    def short_description(self):
        return truncatechars(self.message, 50)

    # def profile_image(self):
    #     return mark_safe('<img src="{}" width="100px" />'.format(self.image.url))

    # profile_image.short_description = 'Image'
    # profile_image.allow_tags = True

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=200, default='Background Infomation')
    description = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Background Info'
        verbose_name_plural = 'Background Info'

    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Functions(models.Model):
    title = models.CharField(max_length=200, default='Mandate & Functions')
    content = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Mandate & Function'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Objectives(models.Model):
    title = models.CharField(max_length=200, default='Strategic Plan')
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='media', blank=True, null=False)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Strategic Plan'
        verbose_name_plural = 'Strategic Plan'


    def __str__(self):
        return self.title


class Mission(models.Model):
    title = models.CharField(max_length=200, default='Our Mission')
    statement = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Our Mission'
        verbose_name_plural = 'Our Mission'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Vision(models.Model):
    title = models.CharField(max_length=200, default='Our Vision')
    statement = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Our Vision'
        verbose_name_plural = 'Our Vision'

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class CoreValues(models.Model):
    title = models.CharField(max_length=200, default='Core Values')
    statement = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')


    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Department(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    @property
    def short_content(self):
        return truncatechars(self.content, 30)

    def __str__(self):
        return self.title


class ServiceCharter(models.Model):
    title = models.CharField(max_length=200, default='Service Charter')
    content = models.TextField(blank=True)
    file = models.FileField(upload_to='media', blank=True, null=False)
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name_plural = 'Service charter'


    def __str__(self):
        return self.title
