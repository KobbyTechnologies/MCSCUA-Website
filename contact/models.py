
from django.db import models

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
        ('Excellent', 'Excellent'),
        ('Average', 'Average'),
        ('Poor', 'Poor')
    ]

    rate = models.CharField(max_length=50, choices=RATE_CHOICES)

    

    def __str__(self):
        return self.rate
