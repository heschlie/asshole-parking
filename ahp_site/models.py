from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class AhpUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField()
    number_of_reports = models.IntegerField()
    submitted_reports = None
    submitted_comments = None


class ReportModel(models.Model):
    title = models.CharField(max_length=255)
    picture = models.OneToOneField('photologue.Photo', on_delete=models.CASCADE)
    photos = models.OneToOneField('photologue.Gallery', on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    violation = models.CharField(max_length=255)
    submit_date = models.DateTimeField(auto_now_add=True)
    reporter = models.ForeignKey('AhpUser', on_delete=models.CASCADE)
    votes = None
