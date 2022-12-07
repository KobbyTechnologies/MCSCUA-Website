from django.db import models
from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


STATUS = (
    (0, "Draft"),
    (1, "Published")
)


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True, editable=False)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='media', null=True,
                              blank=True, help_text='Image size should be in .jpg or .png')
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    category = models.ForeignKey(
        Category, on_delete=models.RESTRICT, default=1)
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Article'

    @property
    def short_description(self):
        return self.content, 20
        # return truncatechars(self.content, 20)

    def blog_photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    blog_photo.short_description = 'Image'
    blog_photo.allow_tags = True

    def __str__(self):
        return self.title


class Featured(models.Model):
    title = models.CharField(max_length=700)
    image = models.ImageField(upload_to='media')
    url = models.URLField()
    created_on = models.DateTimeField()
    status = models.IntegerField(
        choices=STATUS, default=0, help_text='Change to Publish for it to be seen')

    class Meta:
        verbose_name = 'Featured Article'

    @property
    def short_description(self):
        return (self.title)


    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True
    
    def __str__(self):
        return self.title
