from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS
from ckeditor.fields import RichTextField

# Create your models here.


class Carousel(models.Model):
    image = models.ImageField(upload_to='media', help_text='Image size should be 2646px X 1330px')
    title = models.CharField(max_length=100)
    caption = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    status = models.IntegerField(choices=STATUS, default=0, help_text = 'Change to Publish for it to be seen')

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
    name =  models.CharField(max_length=100, primary_key=True)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0, help_text = 'Change to Publish for it to be seen')

    @property
    def short_description(self):
        return truncatechars(self.name)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def __str__(self):
        return self.name


class CallToActionPanel(models.Model):
    title = models.CharField(max_length=200, primary_key=True)
    image = models.ImageField()
    description = RichTextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0, help_text = 'Change to Publish for it to be seen')

    @property
    def short_description(self):
        return truncatechars(self.description, 20)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def __str__(self):
        return self.title