from tabnanny import verbose
from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from blog.models import STATUS

# Create your models here.


class ProjectCategory(models.Model):
    category = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length = 255)

    class Meta:
        verbose_name_plural = 'Project Categories'

    def __str__(self):
        return self.category


class Project(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField()
    image = models.ImageField(upload_to='media')
    slug = models.SlugField(max_length = 255, unique = True)
    category = models.ForeignKey(ProjectCategory, on_delete = models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='change to publish to be seen')

    @property
    def short_description(self):
        return truncatechars(self.description, 50)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'image'
    photo.allow_tag = True

    def __str__(self):
        return self.title
