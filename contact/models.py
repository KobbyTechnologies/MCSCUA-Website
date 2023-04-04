
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

TYPE_CHOICES = [
    (0, 'Inqury'),
    (1, 'Suggestions'),
    (2, 'Complaints')
]


class Feedback(models.Model):
    type = models.IntegerField(choices=TYPE_CHOICES)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject


class RateUs(models.Model):
    RATE_CHOICES = [
        (0, 'Excellent'),
        (1, 'Average'),
        (2, 'Poor')
    ]

    rate = models.IntegerField(choices=RATE_CHOICES)
