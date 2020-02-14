from django.db import models

# Create your models here.


class Job(models.Model):
    # image
    image = models.ImageField(upload_to='uploaded-images/')
    # summary
    intro = models.CharField(max_length=100, default='Enter Intro Here...')
    summary = models.CharField(max_length=200)
    category = models.CharField(
        max_length=100, default='Enter category Here...')
    weblink = models.CharField(max_length=200, default='Enter Url Here...')

    def __str__(self):
        return self.intro
