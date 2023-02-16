from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS
from cloudinary.models import CloudinaryField

# Create your models here.


class Carousel(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=100, blank=True,
                             default='Our Sand, Our livelihood')
    caption = models.TextField(max_length=100, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Published for it to be seen')

    class Meta:
        verbose_name_plural = 'Carousel'

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def __str__(self):
        return self.title


class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Patner(models.Model):
    name = models.CharField(max_length=100, primary_key=True, unique=True)
    image = CloudinaryField('image')
    caption = models.TextField(blank=True)
    url = models.URLField(max_length=200)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def org_photo(self):
        return mark_safe('<img src="{}" width="80px" />'.format(self.image.url))

    org_photo.short_description = 'Image'
    org_photo.allow_tags = True

    def __str__(self):
        return self.name


class CallToActionPanel(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    image = CloudinaryField('image')
    description = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Empowerment(models.Model):
    title = models.CharField(max_length=200)
    message = models.TextField()
    image = CloudinaryField('image')
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='change to published to show front end')

    class Meta:
        ordering = ['-pub_date']

    @property
    def short_description(self):
        return truncatechars(self.message, 30)

    def bg_photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    bg_photo.short_description = 'Image'
    bg_photo.allow_tags = True

    def save(self, *args, **kwargs):
        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
