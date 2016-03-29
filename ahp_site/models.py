from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Report(models.Model):
    title = models.CharField(max_length=255)
    picture = models.OneToOneField('photologue.Photo',
                                   on_delete=models.CASCADE)
    photos = models.OneToOneField('photologue.Gallery',
                                  on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                              null=True)
    lon = models.DecimalField(max_digits=9, decimal_places=6, blank=True,
                              null=True)
    violation = models.CharField(max_length=255)
    submit_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL,
                                 on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    votes = None

    def __str__(self):
        return self.title


class Vehicle(models.Model):
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=100)
    type = None

    def __str__(self):
        return '{}, {}'.format(self.make, self.model)


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment = models.TextField()
    parent_report = models.ForeignKey(Report,
                                      on_delete=models.CASCADE)
    submit_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Comment by {}'.format(self.user)
