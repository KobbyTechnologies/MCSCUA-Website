from django.utils.safestring import mark_safe
from django.template.defaultfilters import truncatechars
from django.db import models
from blog.models import STATUS
from cloudinary.models import CloudinaryField

class PhotoGallery(models.Model):
    title = models.CharField(max_length=200)
    image = CloudinaryField('image')
    caption = models.TextField(blank=True)
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')

    
    class Meta:
        verbose_name_plural = 'Photo Galleries'

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def photo(self):
        return mark_safe('<img src="{}" width="150px" />'.format(self.image.url))

    photo.short_description = 'Image'
    photo.allow_tags = True

    def __str__(self):
        return self.title


class VideoGallery(models.Model):
    title = models.CharField(max_length=200)
    video = CloudinaryField('image')
    caption = models.TextField( blank=True)
    status = models.IntegerField(choices=STATUS, default=0,help_text = 'Change to Publish for it to be seen')


    class Meta:
        verbose_name_plural = 'Video Galleries'

    @property
    def short_description(self):
        return truncatechars(self.caption, 20)

    def vid(self):
        return mark_safe('<video src="{}" width="150px"></video>'.format(self.video.url))

    vid.short_description = 'Video'
    vid.allow_tags = True

    def __str__(self):
        return self.title
